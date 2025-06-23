# Module 2: Introduction to Git
## Unit 1: Introduction
### Learning objectives
In this module, you’ll:

- Identify the fundamental features of GitHub.
- Learn about repository management.
- Gain an understanding of the GitHub flow, including branches, commits, and pull requests.
- Explore the collaborative features of GitHub by reviewing issues and discussions.
- Recognize how to manage your GitHub notifications and subscriptions.

## Unit 2: What is GitHub
GitHub is a cloud-based platform that uses Git, a distributed version control system, at its core. The GitHub platform simplifies the process of collaborating on projects and provides a website, command-line tools, and overall flow that allows developers and users to work together.

As we learned earlier, GitHub provides an AI powered developer platform to build, scale, and deliver secure software. Let’s break down each one of the core pillars of the GitHub Enterprise platform, AI, Collaboration, Productivity, Security, and Scale.

### AI
Generative AI is dramatically transforming software development as we speak. The GitHub Enterprise platform is enhancing collaboration through AI-powered pull requests and issues, productivity through Copilot, and security by automating security checks faster.

### Collaboration
Collaboration is at the core of everything GitHub does. We know inefficient collaboration results in wasted time and money. We counteract that with a suite of seamless tools that allow collaboration to happen effortlessly.

Repositories, Issues, Pull Requests, and other tools help to enable developers, project managers, operation leaders, and others at the same company. It enables them to work faster together, cut down approval times, and ship more quickly.

### Productivity
Productivity is accelerated with automation that the GitHub Enterprise Platform provides. With built-in CI/CD (Continuous Integration and Continuous Delivery) tools directly integrated into the workflow, the platform gives users the ability to set tasks and forget them, taking care of routine administration and speeding up day-to-day work. This gives your developers more time to focus on what matters most, creating innovative solutions.

### Security
GitHub focuses on integrating security directly into the development process from the start. GitHub Enterprise platform includes native, first-party security features that minimize security risk with a built-in security solution. Plus, your code remains private within your organization. At the same time, you're able to take advantage of security overview and Dependabot.

### Scale
GitHub is the largest developer community of its kind with real-time data on over 100M+ developers, 330M+ repositories, and countless deployments. We’ve been able to understand the shifting needs of developers and make changes to our product to match.

This has translated into an incredible scale that is unmatched and unparalleled by any other company on the planet. Everyday we're gaining more insights from this impressive community and evolving the platform to meet their needs.

In essence, the GitHub Enterprise Platform focuses on the developer experience. It has the scale to provide industry-changing insights, collaboration capabilities for transformative efficiency, the tools for increased productivity, security at every step, and AI to power it all to new heights in a single, integrated platform.

## Introduction to Repositories

### What is a repository?
A repository contains all of your project's files and each file's revision history. It's one of the essential parts that helps you collaborate with people. You can use repositories to manage your work, track changes, store revision history, and work with others. 

### How to create a repository
You can create a new repository on your personal account or any organization where you have sufficient permissions.

Let’s tackle creating a repository from github.com.

1. In the upper-right corner of any page, use the drop-down menu, and select New repository.
2. Use the Owner drop-down menu to select the account you want to own the repository.
3. Type a name for your repository, and an optional description.
4. Choose a repository visibility.
- Public repositories are accessible to everyone on the internet.
- Private repositories are only accessible to you, people you explicitly share access with, and, for organization repositories, certain organization members.
5. Select Create repository and congratulations! You just created a repository!

### How to add file to your repository
Files in GitHub can do a handful of things, but the main purpose of files is to store data and information about your project. It's worth knowing in order to add a file to a repository that you must first have minimum Write access within the repository you want to add a file.

1. On GitHub.com, navigate to the main page of the repository.
2. In your repository, browse to the folder where you want to create a file by selecting the creating a new file link or uploading an existing file.
3. Once added, above the list of files select the Add file ᐁ drop-down menu. Then select Create new file.
4. In the file name field, type the name and extension for the file. To create subdirectories, type the / directory separator.
5. In the file contents text box, type content for the file.
6. To review the new content, above the file contents, select Preview.
7. Select Commit changes.
8. In the Commit message field, type a short and meaningful commit message that describes the change you made to the file. You can attribute the commit to more than one author in the commit message.
9. If you have more than one email address associated with your account on GitHub.com, select the email address drop-down menu. Then select the email address to use as the Git author email address. Only verified email addresses appear in this drop-down menu. If you enabled email address privacy, then `[username]`@users.noreply.github.com is the default commit author email address.
10. Below the Commit message fields, decide whether to add your commit to the current branch or to a new branch. If your current branch is the default branch, you should choose to create a new branch for your commit, and then create a pull request.
11. Select Commit changes or Propose changes.

### What is gists
Similarly to repositories, gists are a simplified way to share code snippets with others.
Every gist is a Git repository, which you can fork and clone and be made either public or secret. Public gists are displayed publicly where people can browse new ones as they’re created. Public gists are also searchable. Conversely, secret gists aren't searchable, but they aren’t entirely private. If you send the URL of a secret gist to a friend, they'll be able to see it.

### What are wikis?
Every repository on GitHub.com comes equipped with a section for hosting documentation, called a wiki. You can use your repository's wiki to share long-form content about your project, such as how to use it, how you designed it, or its core principles. While a README file quickly tells what your project can do, you can use a wiki to provide additional documentation.

It’s worth a reminder that if your repository is private, only people who have at least read access to your repository will have access to your wiki.




