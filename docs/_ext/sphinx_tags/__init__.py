"""Sphinx extension to create tags for documentation pages.

Adapted from <https://github.com/melissawm/sphinx-tags>
"""
import os
import re
from fnmatch import fnmatch
from pathlib import Path
from typing import List

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.errors import ExtensionError
from sphinx.util.docutils import SphinxDirective
from sphinx.util.logging import getLogger
from sphinx.util.rst import textwidth

__version__ = "0.3.1"

logger = getLogger("sphinx-tags")


class TagLinks(SphinxDirective):
    """Custom directive for adding tags to Sphinx-generated files.

    Loosely based on https://stackoverflow.com/questions/18146107/how-to-add-blog-style-tags-in-restructuredtext-with-sphinx

    See also https://docutils.sourceforge.io/docs/howto/rst-directives.html

    """

    # Class attributes
    required_arguments = 0
    optional_arguments = 1  # Arbitrary, split on seperator
    final_argument_whitespace = True
    has_content = True
    final_argument_whitespace = True
    option_spec = {
        'hide_intro_text': directives.unchanged,
    }

    # Custom attributes
    separator = ","

    def run(self):
        if not (self.arguments or self.content):
            raise ExtensionError("No tags passed to 'tags' directive.")

        tagline = []
        # normalize white space and remove "\n"
        if self.arguments:
            tagline.extend(self.arguments[0].split())
        if self.content:
            tagline.extend((" ".join(self.content)).strip().split())

        tags = [tag.strip() for tag in (" ".join(tagline)).split(self.separator)]

        tag_dir = Path(self.env.app.srcdir) / self.env.app.config.tags_output_dir
        result = nodes.paragraph()
        result["classes"] = ["tags-list"]

        if 'hide_intro_text' not in self.options:
            result += nodes.inline(text=f"{self.env.app.config.tags_intro_text} ")

        count = 0

        current_doc_dir = Path(self.env.doc2path(self.env.docname)).parent
        relative_tag_dir = Path(os.path.relpath(tag_dir, current_doc_dir))

        for tag in tags:
            count += 1
            # We want the link to be the path to the _tags folder, relative to
            # this document's path where
            #
            #  - self.env.app.config.tags_output_dir
            # |
            #  - subfolder
            #   |
            #    - current_doc_path

            file_basename = _normalize_tag(tag)

            result += nodes.reference(refuri=f"/tags/{file_basename}", text=file_basename)
            tag_separator = f"{self.separator} "

            # if self.env.app.config.tags_create_badges:
            #     result += self._get_badge_node(tag, file_basename, relative_tag_dir)
            #     tag_separator = " "
            # else:
            #     result += self._get_plaintext_node(tag, file_basename, relative_tag_dir)

            if not count == len(tags):
                result += nodes.inline(text=tag_separator)

        # register tags to global metadata for document
        self.env.metadata[self.env.docname]["tags"] = tags

        return [result]

    def _get_plaintext_node(
        self, tag: str, file_basename: str, relative_tag_dir: Path
    ) -> List[nodes.Node]:
        """Get a plaintext reference link for the given tag"""
        link = relative_tag_dir / f"{file_basename}.html"
        return nodes.reference(refuri=str(link), text=tag)

    def _get_badge_node(
        self, tag: str, file_basename: str, relative_tag_dir: Path
    ) -> List[nodes.Node]:
        """Get a sphinx-design reference badge for the given tag"""
        from sphinx_design.badges_buttons import XRefBadgeRole

        # Required to set Inliner state, since we're directly creating a role object.
        # Typically this would be done when parsing the role from document text.
        text_nodes, messages = self.state.inline_text("", self.lineno)

        # Ref paths always use forward slashes, even on Windows
        tag_ref = f"{tag} <{relative_tag_dir.as_posix()}/{file_basename}>"
        tag_color = self._get_tag_color(tag)
        tag_badge = XRefBadgeRole(tag_color)
        return tag_badge(
            name=f"bdg-ref-{tag_color}",
            rawtext=tag,
            text=tag_ref,
            lineno=self.lineno,
            inliner=self.state.inliner,
        )[0]

    def _get_tag_color(self, tag: str) -> str:
        """Check for a matching user-defined color for a given tag.
        Defaults to theme's primary color.
        """
        tag_colors = self.env.app.config.tags_badge_colors or {}
        for pattern, color in tag_colors.items():
            if fnmatch(tag, pattern):
                return color
        return "primary"


class Tag:
    """A tag contains entries"""

    def __init__(self, name):
        self.items = []
        self.name = name
        self.file_basename = _normalize_tag(name)

    def create_file(
        self,
        items,
        extension,
        tags_output_dir,
        srcdir,
        tags_page_title,
        tags_page_header,
    ):
        """Create file with list of documents associated with a given tag in
        toctree format.

        This file is reached as a link from the tag name in each documentation
        file, or from the tag overview page.

        If we are using md files, generate and md file; otherwise, go with rst.

        Parameters
        ----------

        tags_output_dir : Path
            path where the file for this tag will be created
        items : list
            list of files associated with this tag (instance of Entry)
        extension : {["rst"], ["md"], ["rst", "md"]}
            list of file extensions used.
        srcdir : str
            root folder for the documentation (usually, project/docs)
        tags_page_title: str
            the title of the tag page, after which the tag is listed (e.g. "Tag: programming")
        tags_page_header: str
            the words after which the pages with the tag are listed (e.g. "With this tag: Hello World")
        tag_intro_text: str
            the words after which the tags of a given page are listed (e.g. "Tags: programming, python")


        """
        # Get sorted file paths for tag pages, relative to /docs/_tags
        tag_page_paths = sorted([i.relpath(srcdir) for i in items])
        ref_label = f"sphx_tag_{self.file_basename}"

        content = []
        if "md" in extension:
            filename = f"{self.file_basename}.md"
            content.append(f"({ref_label})=")
            content.append(f"# {self.name}")
            content.append("")
            content.append(f"{tags_page_header} &lsquo;{self.name}&rsquo;.")
            content.append("")
            content.append("[&laquo; View all tags](/tags-list/)")
            content.append("")

            for path in tag_page_paths:
                formatted_path = "/" + re.sub(r'index\/$', "", re.sub(r'\.[a-zA-Z0-9]+$', "", path))
                content.append(f"{{doc}}`{formatted_path}`")
                content.append("")

        else:
            filename = f"{self.file_basename}.rst"
            header = self.name
            content.append(f".. _{ref_label}:")
            content.append("")
            content.append(header)
            content.append("#" * textwidth(header))
            content.append("")
            content.append(f"{tags_page_header} &lsquo;{self.name}&rsquo;.")
            content.append("")
            content.append("`&laquo; View all tags </tags-list/>`_")
            content.append("")

            for path in tag_page_paths:
                formatted_path = "/" + re.sub(r'index\/$', "", re.sub(r'\.[a-zA-Z0-9]+$', "", path))
                content.append(f":doc:`{formatted_path}`")
                content.append("")

        content.append("")
        with open(
            os.path.join(srcdir, tags_output_dir, filename), "w", encoding="utf8"
        ) as f:
            f.write("\n".join(content))


class Entry:
    """Tags to pages map"""

    def __init__(self, entrypath: Path, tags: list):
        self.filepath = entrypath
        self.tags = tags

    def assign_to_tags(self, tag_dict):
        """Append ourself to tags"""
        for tag in self.tags:
            if tag not in tag_dict:
                tag_dict[tag] = Tag(tag)
            tag_dict[tag].items.append(self)

    def relpath(self, root_dir) -> str:
        """Get this entry's path relative to the given root directory"""
        return Path(os.path.relpath(self.filepath, root_dir)).as_posix()


def _normalize_tag(tag: str) -> str:
    """Normalize a tag name to use in output filenames and tag URLs.
    Replace whitespace and other non-alphanumeric characters with dashes.

    Example: 'Tag:with (special   characters) ' -> 'tag-with-special-characters'
    """
    return re.sub(r"[\s\W]+", "-", tag).lower().strip("-")


def tagpage(tags, outdir, title, extension, tags_index_header):
    """Creates Tag overview page.

    This page contains a list of all available tags.

    """

    tags = list(tags.values())

    if "md" in extension:
        content = []
        content.append("(tagoverview)=")
        content.append("")
        content.append(f"# {title}")
        content.append("")
        content.append(tags_index_header)
        content.append("")
        content.append("```{toctree}")
        content.append(":glob:")
        content.append("tags/*")
        content.append("```")
        content.append("")
        # for tag in sorted(tags, key=lambda t: t.name):
        #     content.append(f"[{tag.name} ({len(tag.items)})](/tags/{tag.name})")
        #     content.append("")

        # toctree for this page
        # content.append("```{toctree}")
        # content.append("---")
        # content.append(f"caption: {tags_index_header}")
        # content.append("maxdepth: 1")
        # content.append("---")
        # for tag in sorted(tags, key=lambda t: t.name):
        #     content.append(f"{tag.name} ({len(tag.items)}) <{tag.file_basename}>")
        # content.append("```")
        content.append("")
        filename = os.path.join(outdir, "tags-list.md")
    else:
        content = []
        content.append(":orphan:")
        content.append("")
        content.append(".. _tagoverview:")
        content.append("")
        content.append(title)
        content.append("#" * textwidth(title))
        content.append("")
        content.append(".. toctree::")
        content.append("   :glob:")
        content.append("")
        content.append("   tags/*")
        content.append("")
        content.append("")
        # # toctree for the page
        # content.append(".. toctree::")
        # content.append(f"    :caption: {tags_index_header}")
        # content.append("    :maxdepth: 1")
        content.append("")
        # for tag in sorted(tags, key=lambda t: t.name):
        #     content.append(f"`{tag.name} ({len(tag.items)}) </tags/{tag.name}>`_")
        content.append("")
        filename = os.path.join(outdir, "tags-list.rst")

    with open(filename, "w", encoding="utf8") as f:
        f.write("\n".join(content))


def assign_entries(app):
    """Assign all found entries to their tag."""
    pages = []
    tags = {}

    for docname in app.env.found_docs:
        doctags = app.env.metadata[docname].get("tags", None)
        if doctags is None:
            continue  # skip if no tags
        entry = Entry(app.env.doc2path(docname), doctags)
        entry.assign_to_tags(tags)
        pages.append(entry)

    return tags, pages


def update_tags(app):
    """Update tags according to pages found"""
    if app.config.tags_create_tags:
        tags_output_dir = Path(app.config.tags_output_dir)

        if not os.path.exists(os.path.join(app.srcdir, tags_output_dir)):
            os.makedirs(os.path.join(app.srcdir, tags_output_dir))

        for file in os.listdir(os.path.join(app.srcdir, tags_output_dir)):
            if file.endswith("md") or file.endswith("rst"):
                os.remove(os.path.join(app.srcdir, tags_output_dir, file))

        # Create pages for each tag
        tags, pages = assign_entries(app)

        for tag in tags.values():
            tag.create_file(
                [item for item in pages if tag.name in item.tags],
                app.config.tags_extension,
                tags_output_dir,
                app.srcdir,
                app.config.tags_page_title,
                app.config.tags_page_header,
            )

        # Create tags overview page
        tagpage(
            tags,
            os.path.join(app.srcdir),
            app.config.tags_overview_title,
            app.config.tags_extension,
            app.config.tags_index_header,
        )
        logger.info("Tags updated", color="white")
    else:
        logger.info(
            "Tags were not created (tags_create_tags=False in conf.py)", color="white"
        )


def setup(app):
    """Setup for Sphinx."""

    # Create config keys (with default values)
    # These values will be updated after config-inited

    app.add_config_value("tags_create_tags", False, "html")
    app.add_config_value("tags_output_dir", "tags", "html") # Note: Don't change this setting from the default.
    app.add_config_value("tags_overview_title", "Tags overview", "html")
    app.add_config_value("tags_extension", ["rst"], "html")
    app.add_config_value("tags_intro_text", "Tags:", "html")
    app.add_config_value("tags_page_title", "My tags", "html")
    app.add_config_value("tags_page_header", "With this tag", "html")
    app.add_config_value("tags_index_header", "Here is a list of all tags that are used on the site.", "html")
    app.add_config_value("tags_create_badges", False, "html")
    app.add_config_value("tags_badge_colors", {}, "html")

    # internal config values
    app.add_config_value(
        "remove_from_toctrees",
        [
            app.config.tags_output_dir,
        ],
        "html",
    )

    # Update tags
    # TODO: tags should be updated after sphinx-gallery is generated, and the
    # gallery is also connected to builder-inited. Are there situations when
    # this will not work?
    app.connect("builder-inited", update_tags)
    app.add_directive("tags", TagLinks)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
        "env_version": 1,
    }
