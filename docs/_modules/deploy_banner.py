import os

def banner():
    git_branch = os.environ.get("BRANCH")
    deploy_name = os.environ.get("DEPLOY_NAME")
    pull_request = os.environ.get("PULL_REQUEST")
    review_id = os.environ.get("REVIEW_ID")
    build_id = os.environ.get("BUILD_ID")

    knowledge_hub_url = "https://docs.dea.ga.gov.au/"
    github_url = "https://github.com/GeoscienceAustralia/dea-docs"
    deploy_logs_url = "https://app.netlify.com/sites/dea-docs/deploys"

    pull_request_banner = f'You are viewing <strong>{deploy_name}</strong>, not the official <a href="{knowledge_hub_url}">DEA Knowledge Hub</a>. View the <a href="{deploy_logs_url}?filter={git_branch}">deploy logs</a> or <a href="{github_url}/tree/{git_branch}">git branch</a>.'

    demo_banner = f'You are viewing <strong>Pull Request #{review_id}</strong>, not the official <a href="{knowledge_hub_url}">DEA Knowledge Hub</a>. View the <a href="{deploy_logs_url}/{build_id}">latest deploy log</a> or the <a href="{github_url}/pull/{review_id}">pull request</a>.'

    if pull_request == "true":
        return pull_request_banner
    else:
        return demo_banner

