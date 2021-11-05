import os
from base64 import b64decode, b64encode
from datetime import date

from ghapi.actions import github_token
from ghapi.all import GhApi
from IPython.display import Markdown

OWNER = "Quansight-Labs"
REPO = "jupyter-a11y-mgmt"

# ------------------------------------------------------------------

# On GitHub Actions "ACCESS_TOKEN" should be a personal access token with r/w permissions to *other* repos
token = (
    github_token() if "ACCESS_TOKEN" not in os.environ else os.environ["ACCESS_TOKEN"]
)

# Initialize the GH API and our markdown
api = GhApi(token=token)

# Grab the report template
template = api.repos.get_content(OWNER, REPO, "team_updates/template.md")
template = b64decode(template.content).decode("utf-8")

# Get the team update issue and the comments
issues = api.issues.list_for_repo(OWNER, REPO, labels="type: team-update", state="open")

if issues:
    for issue in issues:
        issue_comments = api.issues.list_comments(
            OWNER, REPO, issue_number=issue.number
        )
        issue_url = issue.url
    if issue_comments:
        summary = (
            "\n".join(
                [
                    f"- **@{comment.user.login}** \n\n {comment.body} \n---\n"
                    for comment in issue_comments
                ]
            )
            + "\n\n"
            + f"See the original issue at: <{issue.url}>"
            + "\n\n"
        )
    else:
        summary = "Nothing to report"


# Replace template
template = template.replace("{{ INSERT PERSONAL UPDATES }}", summary)

report_date = date.today().strftime("%d-%m-%Y")

template = template.replace("{{ date }}", report_date)

# Encode the markdown document

encoded_template = b64encode(bytes(template, "utf-8")).decode("utf-8")

resp = api.repos.create_or_update_file_contents(
    owner=OWNER,
    repo=REPO,
    message="🤖 weekly team update",
    content=encoded_template,
    path=f"team_updates/{report_date}.md",
    branch="master",
)
