// This function handles redirect logic

async function handler(event) {
    const request = event.request;
    const uri = event.request.uri;
    const deaToolsSourceCodePattern = /dea_tools\/(.*)\.py$/g;
    const indexHtmlPattern = /\/index\.html$/g;
    const filetypeExtensionsPattern = /\.(html|rst|md|ipynb|py)$/g;

    const status301MovedPermanently = {
        statusCode: 301,
        statusDescription: "Moved Permanently"
    };

    // Redirect DEA Tools source code URLs to the relevant 'automodule' page generated from the source code.
    // E.g. "../Tools/dea_tools/coastal.py" => "/notebooks/Tools/gen/dea_tools.coastal/"
    // E.g. "../Tools/dea_tools/app/animations.py" => "/notebooks/Tools/gen/dea_tools.app.animations/"

    if (deaToolsSourceCodePattern.test(uri)) {
        const sourceCodePath = uri.match(deaToolsSourceCodePattern)[0];
        const automoduleName = sourceCodePath.replaceAll("/", ".");
        const automoduleUri = `/notebooks/Tools/gen/dea_tools.${automoduleName}/`;

        return Object.assign(status301MovedPermanently, {
            headers: {
                location: {
                    value: automoduleUri
                }
            }
        });
    }

    // Redirect URLs ending in "index.html" to end in "/" instead. E.g. /page/index.html => /page/

    if (indexHtmlPattern.test(uri)) {
        return Object.assign(status301MovedPermanently, {
            headers: {
                location: {
                    value: uri.replace(indexHtmlPattern, "/")
                }
            }
        });
    }

    // Redirect URLs ending in certain extensions (".html", ".rst", and others) to end in "/" instead. E.g. /example.html => /example/

    if (filetypeExtensionsPattern.test(uri)) {
        return Object.assign(status301MovedPermanently, {
            headers: {
                location: {
                    value: uri.replace(filetypeExtensionsPattern, "/")
                }
            }
        });
    }

    return request;
}
