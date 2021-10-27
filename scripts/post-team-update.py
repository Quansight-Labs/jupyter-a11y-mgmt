import os
import sys
from base64 import b64decode
from datetime import date

from ghapi.actions import github_token
from ghapi.all import GhApi

OWNER = "Quansight-Labs"
REPO = "jupyter-a11y-mgmt"

# ------------------------------------------------------------------


def get_session():
    # On GitHub Actions "ACCESS_TOKEN" should be a personal access token with r/w permissions to *other* repos
    token = (
        github_token()
        if "ACCESS_TOKEN" not in os.environ
        else os.environ["ACCESS_TOKEN"]
    )
    # Initialize the GH API and our markdown
    api = GhApi(token=token)
    print("Logged in the GH API 🎉")

    return api


# The base template is defined here: https://github.com/Quansight-Labs/jupyter-a11y-mgmt/blob/main/.github/ISSUE_TEMPLATE/team-update.md
# It has placeholders for lists of issues, and these will be automatically filled in below, then a new issue will be created.


def process_template(api):
    # Grab our issue template
    template = api.repos.get_content(
        OWNER, REPO, ".github/ISSUE_TEMPLATE/team-update.md"
    )
    template = b64decode(template.content).decode("utf-8")

    # This removes the header bracketed by ---
    template = "---".join(template.split("---")[2:]).strip()
    template = get_triage_issues(api, template)
    return template


def get_triage_issues(api, template):
    ## Needs Triage
    issues = api.issues.list_for_repo(OWNER, REPO, labels="status: needs triage")
    if issues:
        needs_triage = (
            "\n".join([f"* [{issue.title}]({issue.html_url})" for issue in issues])
            + "\n\n"
        )
    else:
        needs_triage = "No issues need triage! 🎉\n\n"
    return template.replace("{{INSERT NEEDS TRIAGE ISSUES HERE}}", needs_triage)


def open_issue(api, template):
    # Now create an issue with this content
    resp = api.issues.create(
        OWNER,
        REPO,
        title=f"Team update - {date.today():%b %d, %Y}",
        body=template,
        labels=["type: team-update", "type: internal-pm"],
    )
    issue_url = f"https://github.com/{resp.url.split('repos/')[-1]}"
    print(f"Finished posting team update to {issue_url} !")
    return issue_url


# ------------------------------------------------------------------

if __name__ == "__main__":
    api = get_session()
    template = process_template(api)
    issue_url = open_issue(api, template)
    sys.stdout.write(issue_url)
