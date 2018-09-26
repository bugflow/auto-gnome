from gnome.policies import Policy
from gnome.gh import Repo, Issue, gh


class SyncProjectMilestones(Policy):
    def dispatch_gnome(self):
        headers = self.callback.headers()
        event = headers['X-GitHub-Event']

        if event not in ('project_card'):
            return

        payload = self.callback.payload()
        card = payload['project_card']
        if not payload['action'] == 'deleted':
            if 'content_url' in card:
                # Is a ticket
                repo_name = payload['repository']['full_name']
                issue_url = card['content_url']
                issue_number = issue_url.split('/')[-1]
                repo = Repo(repo_name)
                gh_issue = repo._repo.get_issue(int(issue_number))
                issue = Issue(repo, gh_issue)

                # Project details
                project_url = payload['project_card']['project_url']
                project_id = project_url.split('/')[-1]
                project = gh.get_project(int(project_id))
                project_name = project.name

                if project.state == 'closed':
                    return

                if gh_issue.milestone \
                        and gh_issue.milestone.title == project_name:
                    print('Milestone already set - aborting')
                    return

                issue.move_to_milestone(project_name)
