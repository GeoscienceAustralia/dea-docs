// Sets behaviours for headings.
// The rules in this script occur in a specific order and each will overwrite properties set in the previous one.

document.addEventListener("DOMContentLoaded", function (event) {
    // Convert the 'rubric' headings to H2 headings

    (function() {
        let rubrics = document.querySelectorAll("p.rubric");

        for (let i = 0; i < rubrics.length; i++) {
            let rubric = rubrics[i];
            let h2 = document.createElement("h2");
            h2.id = rubric.id;
            h2.class = rubric.class;
            h2.innerHTML = rubric.innerHTML;
            rubric.parentNode.replaceChild(h2, rubric);
        }
    })();

    // Add a 'data-anchor-id' property based on the Section ID.

    (function() {
        let sections = document.querySelectorAll("section[id]");

        for (let i = 0; i < sections.length; i++) {
            let section = sections[i];
            let id = section.id;
            let maybeHeading = section.querySelector("* > h2, * > h3");

            if (maybeHeading) {
                maybeHeading.dataset.anchorId = id;
            }
        }
    })();

    // Add a 'data-anchor-id' property based on the heading's own ID.

    (function() {
        let headings = document.querySelectorAll("h2, h3");

        for (var i = 0; i < headings.length; i++) {
            let heading = headings[i];
            let id = heading.id;

            if (id) {
                heading.dataset.anchorId = id;
            }
        }
    })();

    // Add a 'data-anchor-id' from the custom ID element above the heading.

    (function() {
        let headings = document.querySelectorAll("h2, h3");

        for (var i = 0; i < headings.length; i++) {
            let heading = headings[i];
            let maybeCustomIdElement = heading.previousSibling;

            if (maybeCustomIdElement && maybeCustomIdElement.nodeName === "SPAN" && maybeCustomIdElement.hasAttribute("id")) {
                heading.dataset.anchorId = maybeCustomIdElement.id;
            }
        }
    })();

    // Clicking on a heading will add its anchor ID to the URL. E.g. /example/#introduction

    (function() {
        let headings = document.querySelectorAll("h2[data-anchor-id], h3[data-anchor-id]");

        for (var i = 0; i < headings.length; i++) {
            let heading = headings[i];
            let anchorId = heading.dataset.anchorId;

            heading.addEventListener("click", function() {
                console.log(anchorId);
                window.location.hash = `#${anchorId}`
            });
        }
    })();

    // Clicking on a product tab will add its tab ID to the URL. E.g. /example/?tab=overview

    (function() {
        let tabs = document.querySelectorAll(".product-page .sd-tab-label");
        let tabUrlParam = new URLSearchParams(window.location.search).get("tab");
        let overviewTabId = tabs[0].id;

        if(!tabUrlParam) {
            window.history.pushState("", "", `?tab=${overviewTabId}${window.location.hash}`);
        } else {
            document.querySelector(`.sd-tab-set > #${tabUrlParam}`).click();
        }

        for (let i = 0; i < tabs.length; i++) {
            let tab = tabs[i];
            let tabId = tab.id;

            if (tabId) {
                tab.addEventListener("click", function() {
                    window.history.pushState("", "", `?tab=${tabId}`);
                });
            }
        }
    })();
});

