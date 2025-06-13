# Module 6: Manage repository changes by using pull requests on GitHub

## Unit 1: Introduction
Change is inevitable, especially in software repositories. Project improvements often require the coordination of many people working together in parallel to produce the right output. Responsibly tracking and merging those changes is a complex and substantial challenge.

Fortunately, pull requests offer the right balance of control and convenience. Whether you're interested in making changes, reviewing changes, or understanding the effect of changes across the repository, pull requests are the way GitHub users collaborate on code.

### Learning objectives

- Review branches and their importance to pull requests.
- Define what a pull request is.
- Learn how to create a pull request.
- Understand the different pull request statuses.
- Walk through how to merge a pull request to a base branch.

## Unit 2: What are pull requests?

### Branches
First, let’s define what branches are, why they’re important to developers, and how they’re related to pull requests.

Branches are isolated workspaces where you can develop your work without affecting others in the repository. They allow you to develop features, fix bugs, and safely experiment with new ideas in a contained area of your repository.

Developers working on independent branches is a common concept in modern software development. By having their own branch, a developer can make any changes, called commits, without worrying about how their commits affect other developers working on their own branches.

### Merging branches
Although having each developer work on a separate branch is great for individual productivity, it opens a new challenge. At some point, each developer's branch needs to be merged into a common branch, like main. As projects scale, there can be many merges that need to happen, and it becomes increasingly important to track and review each merge. Needing to keep track of multiple changes to a project is where pull requests come in.

### What is a pull request?
A pull request is a way to document branch changes and communicate that the changes from the developer’s branch are ready to be merged into the base (main) branch. Pull requests enable stakeholders to review and discuss the proposed changes to ensure that the code quality in the base branch is kept as high as possible.

In order for the two branches to be merged, they must be different from one another:

- The compare branch is the developer’s own branch, which contains the specific changes they made.
- The base branch, also referred to as the main branch, is the branch that the changes need to be merged into.

The most common use of compare is to compare branches, such as when you're starting a new pull request. You're always taken to the branch comparison view when starting a new pull request.

### Create a pull request

1. On GitHub.com, navigate to the main page of the repository.
2. In the Branch menu, select the branch that contains your commits.
3. Above the list of files, in the yellow banner, select the Compare & pull request button to create a pull request for the associated branch.
4. In the base branch dropdown menu, select the branch you'd like to merge your changes into. Then select the compare branch dropdown menu to select the branch you made your changes in.
5. Enter a title and description for your pull request.
6. To create a pull request that’s ready for review, select the Create Pull Request button. To create a draft pull request, select the dropdown and select Create Draft Pull Request, then select Draft Pull Request.

### Pull request statuses
- Draft pull request - When you create a pull request, you can choose to either create a pull request that’s ready for review or a draft pull request. A pull request with a draft status can’t be merged, and code owners aren’t automatically requested to review draft pull requests.

- Open pull request - An open status means the pull request is active and not yet merged to the base branch. You can still make commits and discuss and review potential changes with collaborators.

- Closed pull request - You can choose to close a pull request without merging it into the base/main branch. This option can be handy if the changes proposed in the branch are no longer needed, or if another solution is proposed in another branch.

- Merged pull request - The merged pull request status means that the updates and commits from the compare branch were combined with the base branch. Anyone with push access to the repository can complete the merge.

### Merge a pull request
1. Under your repository name, select Pull requests.
2. In the Pull requests list, select the pull request you'd like to merge.
3. Scroll down to the bottom of the pull request. Depending on the merge options enabled for your repository, you can:
    - Merge all of the commits into the base branch by selecting the Merge pull request button. If the Merge pull request option isn’t shown, select the merge dropdown menu, choose the Create a merge commit option, and then select the Create a merge commit button.
    - Squash and merge allows you to take all of your commits and combine them into one. This option can help you keep your repository history more readable and organized. Select the Squash and merge option, and then select the Squash and merge button.
    - The Rebase and merge option allows you to make commits without a merge commit. This option enables you to skip a merge by maintaining a linear project history. Select the merge dropdown menu, then choose the Rebase and merge option, and then select the Rebase and merge button.
4. If prompted, enter a commit message, or accept the default message.
5. If you have more than one email address associated with your account on GitHub.com, select the email address dropdown menu and select the email address to use as the Git author email address. Only verified email addresses appear in this dropdown menu. If you enabled email address privacy, then a no-reply GitHub email is the default commit author email address.
6. Select Confirm merge, Confirm squash and merge, or Confirm rebase and merge.
7. Optionally, you can delete the compare branch to keep the list of branches in your repository tidy.