# Module 1: Contribute to an open-source project on GitHub

## Unit 1: Introduction
Open-source software relies heavily on the community for its long-term sustainability. One way to contribute to open-source projects is by making contributions to the project's repository and conducting code reviews.

Suppose you've been using open-source libraries for your projects and at work for quite some time. In the spirit of open source, you've decided to contribute back to some of these libraries and frameworks.

## Unit 2: Identify where you can help
Open-source software can be freely used, modified, and shared by anyone. Using open-source software, anyone can view, modify, and distribute a project for any purpose. The idea behind open-source software is that sharing code leads to better, more reliable software.

There are many ways to contribute to open-source projects. Making your first contribution can often be a scary experience, but it shouldn't be. Open source is a place for everyone, and contributions happen at all levels.

### Find an open-source project that needs contributions
You can get started by thinking about the projects you already use, or want to use. Contributing is easier when you're familiar with the project and its community.

Perhaps while reading a project's README file, you find a broken link or some typos. Maybe you noticed something isn't working as expected, or the documentation is out of date. These are all great opportunities to help and contribute to the project.

One important tip: All kinds of contributions are valuable. Your level of experience or knowledge of the project doesn't matter here. We all have something we can contribute. Be confident in yourself. The most important thing here is the will to help.

### Use GitHub search
You can also use GitHub search to explore topics and related projects. Head to GitHub search, and enter your topic word.

Let's say you're interested in machine learning.
You can then narrow your search by selecting Topics in the left sidebar.
From there, you can find repositories relevant to your search keyword and repositories curated by community members.

### Familiarize yourself with an open-source project
Something worth mentioning here is that every open-source community is different. After you've found a project, you'll need to familiarize yourself with the project and its participation guidelines.

Most projects will have these documents at the top level of the repository:
- LICENSE: The project must contain an open-source license. If the project doesn't have a license, it's not open source.
- README: The README file usually serves as the welcome page for the project. It generally provides information on how to get started using the project. It's also common for it to add information on how to engage with the community.
- CONTRIBUTING: As its name suggests, this document provides guidance on how to contribute to the project. It usually describes how the contribution process works, and includes details on how to set up your development environment.
- CODE_OF_CONDUCT: The code of conduct sets ground rules for community members. By doing so, it helps make the community a safe and welcoming environment for all.

Although not all projects have CONTRIBUTING or CODE_OF_CONDUCT documents, having these documents is a good indication of how friendly and welcoming a project is.

Open-source contributors and maintainers come from all over the world. Projects usually have multiple communication channels to organize discussions and ask for help. A good way to familiarize yourself with the community is by reading through some of these communication channels:

- Issue tracker: Where folks discuss issues and tasks related to the project. To find the issues in GitHub, you can go to the main page of the repository on GitHub and add /issues to the end of the URL, for example: https://github.com/jupyter/notebook/issues.
- Pull request: Where folks discuss and review changes to the project. You can find it in GitHub by adding pulls to the project's URL, for example, https://github.com/jupyter/notebook/pulls.
- Chat channels and forums: Some projects use chat channels, such as Slack, Gitter, and IRC, or forums like Discourse for conversations and discussions.

### Identify tasks to work on
You've found a project, you've read the contribution guidelines, and now you're ready to contribute.

Perhaps you've already identified something to work on, such as fixing broken links or updating the docs. A good way to find beginner-friendly issues to help with is by visiting the project's /contribute URL, for example: https://github.com/jupyter/notebook/contribute.

You'll notice that most of the issues displayed in the contribute URL will have labels such as good-first-issue, help wanted, beginner-friendly, and so on. Labels are often used to provide top-level information of the issue and the type of help needed.

You can head to the labels page, for example: https://github.com/jupyter/notebook/labels. Then, select issues that have labels like help wanted, discussion, or other labels relevant to the type of contribution in which you're interested.

As you explore issues, you might also notice that some have other issues or pull requests linked.

### Sponsor a project
There are many ways to contribute to open source. You can financially support the folks who build and maintain the open-source ecosystem through code, leadership, mentorship, design, and beyond.

Open source heavily relies on volunteer work. GitHub Sponsors allow you to fund projects and individuals to help them keep doing their open-source work, while giving them the recognition they deserve.

If a project is eligible for sponsorship through GitHub Sponsors, you'll find a Sponsor button on the project's main page.

You can select the sponsorship tier and if you want your contribution to be public.

### Unit recap
In this unit, you learned how to get started with open-source contributions. You now know how to choose a project to work on and use GitHub issues and labels to identify tasks to work on.

Here's a handy checklist to use when you interact with a project for the first time:

- Does it have a license?
-  Are issues and pull request discussions used actively by maintainers and contributors?
- Does the project use labels like help wanted or good first issue for newcomers?
- Does the project have a code of conduct?
- Does the project have clear Contributing Guidelines?

Finally, remember that all contributions are welcome, and the open-source ecosystem greatly benefits from your ideas and participation. There are many ways to contribute to open source, from submitting code or engaging in project discussions to sponsoring projects through GitHub Sponsors.
 
## Unit 3: Contribute to an open-source repository
After you identify an area where you can contribute, the next step is to prepare your contribution. We'll review here how you can communicate your intent to participate in a project, forge a pull request, and improve your chances of getting it accepted.

When it comes to contributing work to an open-source project, communication is a key success factor. You might find it uncomfortable to communicate with others on your proposed changes or improvements. Often, this dialogue will lead to discussions and compromises on your original vision.

Avoiding active communication with others who are involved in an open-source project means risking your time working on tasks that someone else is already working on. Or, you might work on features or improvements that don't align with the project's values or best practices. In either case, everyone's time is wasted. Conversely, committing to active communication ensures that your work will be well received and impactful.

How can you ensure success when you communicate with other project members about new features and changes? First, try to keep an open mind. Be open to feedback and practice patience. Open-source project maintainers most likely have a day job and a private life to tend to. If you don't get an answer immediately, wait a little longer before you ping the maintainers.

### Communicate your intent to maintainers
You should always start by communicating your intent to contribute before you do any actual work. Unless indicated otherwise in the README file, the issue tracker is usually the best place for doing that.

- If you want to work on an existing issue, check that nobody is assigned to it by looking at the Assignees section. Also check the Linked pull requests section. A linked pull request means somebody is already working on it. Look through the comments to see if someone stated their interest to work on the issue. If everything's clear, post a comment on the issue to indicate your interest to work on it. That way, you're telling people who might come later that someone's working on the issue. Also, if needed, maintainers can reply to you with guidance and advice.

- If you want to work on a new feature or a bug that's not already present in the issue tracker, create a new issue. Make sure to follow the issue template if one is proposed, and clearly express your intent to work on the issue. If it's a new feature proposition or if the issue requires many changes, make sure to get the maintainers' approval before you move on to the next step.

### Create a pull request on a GitHub repository
After you've communicated your intent to help the project, you're now ready to start working on your actual contribution.

Your contribution will take the form of a pull request or PR. A pull request is a special place on GitHub that contains a few things:
- A title and description for your changes.
- One or more commits that constitute the changes you're proposing.
- Comments, where everyone can participate in a discussion about the changes.
- Code reviews, where you can find detailed feedback on your changes and eventually commit suggestions.
- Status checks that come, for example, from automated tests that the maintainers might have put in place. Status checks can serve different purposes. For example, they can ensure that your changes follow the project's rules, or that your changes don't break the code.

After a pull request is created, it can be updated with new commits, comments, or code reviews. This process continues until the project maintainers approve and merge the pull request or reject the changes and close the pull request. When your pull request is merged, it means that your changes have been integrated into the project's codebase.

### Pass the status checks
After you've created the pull request, you might see a section with status checks at the bottom, like this:

These status checks are automated checks that the maintainers have put in place to ensure a consistent quality of the project.

To get your pull request accepted, it needs to pass all automated checks. If one is failing like in the preceding screenshot, select the Details button to learn more about the failure and to find out what you need to do to fix it.

If you're unsure about what to do with a failing check, you can always use the comments to ask for the maintainers' guidance or help to fix it.

### Ask for guidance or reviews on pull requests
You might be unsure about some changes you made and want to get the maintainers' opinions. The best way to do that is to comment directly on the pull requests. If you consider your changes a work-in-progress, you also have the option to create a draft pull request instead to ask for guidance or help from other contributors.

After the project maintainers come by your pull request, they can reply to the conversation or directly review your changes. There are multiple possible outcomes following a pull request review:

- Your changes are approved. Congratulations!
- Your pull request requires some changes. Don't get discouraged! Look closely at the feedback provided. If you make the requested changes, there's a good chance that your pull request will be accepted. If you push new commits to your branch, the pull request will automatically update with the new changes.
- The reviewer made some comments. It usually means that more details are needed about your changes or the motivation behind it.

### Respond to comments on your pull request
Remember to always be respectful in all your exchanges and to follow the code of conduct. It's likely that before your changes can be accepted, there will be an ongoing discussion with the maintainers or other contributors.

Contributing to open source requires patience. Sometimes you don't get immediate feedback. Don't reach out to the maintainers privately via email, X, or any other means hoping to get a faster answer. This behavior is considered harmful. Discussing things publicly also gives other contributors or passersby the opportunity to learn about the process behind the changes and the best practices to follow.

## Unit 4: Exercise - Create your first pull request

### Describe your changes
To write a good commit message, and subsequently your pull request, follow these practices:

For the body of your message and pull request, continue to use present tense. Make sure to include the motivation for the change. Contrast your change with the previous behavior. Use the space at your disposal to explain the what and why versus the how.

Your commit message is only as much to the point as the content that you're about to submit. Commit or submit for review small, isolated sets of changes. This practice increases the likelihood of your changes getting merged into the project.

### Add granularity
Before you submit your pull request, check the sidebar for ways to complete your PR. Select Reviewers or Assignees if you're familiar with the project's team structure. Add labels when there's guidance on using labels in, for instance, the CONTRIBUTING.md file. You can use labels as a visual clue for what you're trying to accomplish. A maintainer might also add a label or multiple labels.

Optionally, you can link issues in the sidebar, where successfully merging a pull request might close the corresponding issue. You can also customize your subscription to notifications on the thread. Some PRs receive many comments, reviews, and CI/CD-related notifications. You can choose from:
- Not subscribed: Only receive notifications when you participated or were @mentioned
- Subscribed: Receive all notifications for this pull request
- Custom: Only be notified for the events you select

## Unit 5: Next steps

### Get involved in the community
You'll find frequent contributors to the project in the comment section for issues and pull requests. Or, you can select Insights in the repository's navigation, and then select Contributors to find other active community members. Visit their GitHub profiles. Sometimes they'll suggest ways to get in touch with them.

You can also follow organizations and enterprises on GitHub to stay in touch. Your personal dashboard shows public activity for every enterprise, user, or organization you follow.

You can also find like-minded folks by attending meetups or conferences on open-source topics. Or, you can meet people if the project or ecosystem is large enough around the project you're interested in. Find archives with talk recordings for past events, podcasts, newsletters, and mailing lists.

Some projects have centralized communication, which is often referenced on the project's website or in the README file. There might be a Discord server, a Slack community, Gitter, IRC, or even regular "office hours."

### Code reusability

Code, and solutions, can sometimes be reused across projects. Have you solved a very scoped issue for one project? Chances are other projects can benefit from it as well. You can:

- Publish as a stand-alone library (dependency).
- Mirror the project with your added functionality.
- Create a GitHub Action for others to include in their workflow.

The first option is probably the best course of action when your bit of code is like a plug-in that could be used across web-development projects. Mirroring or forking a project with the addition of your code is useful when you're solving a narrow use case for a small subset of customers, or even a single customer. Consider that you'll need to keep your fork up to date with the upstream repository if you want to benefit from (for instance) security patches.

GitHub Actions are packaged scripts that automate tasks in a software-development workflow in GitHub. The two different types of actions are container actions and JavaScript actions. You can submit your action to the GitHub Marketplace for discoverability. GitHub Marketplace connects you to developers who want to extend and improve their GitHub workflows. Use this platform to publish actions and share apps with other users for free.

For all three of the suggested paths, consider that you're now a maintainer of a project. People will come to you with praise, questions, and complaints. Are you ready for such a commitment?

If your project takes off, people's apps might depend on your bit of code. Can you involve more people to take some of the potential load off? Do you have time to add documentation, triage issues, and review suggestions from people you've likely never met before? Consider your "bandwidth," and instead set expectations in your project's README file. Or, you can release your code in a public gist or a blog post. Code doesn't need to be on GitHub to be open source, after all.

## Unit 6: Quiz

## Unit 7: Summary
In this module, you wanted to take part in the open-source community by learning how to provide support and contribute to open-source projects using GitHub.

You learned how to find projects to contribute to on GitHub. You discovered how to familiarize yourself with the project and its guidelines. You learned how to use the issue tracker and labels to find tasks to work on. You also learned that via GitHub Sponsors you can financially support your favorite projects and open-source contributors.

After discovering where you can provide help, you learned how to use GitHub to create your first contribution and submit a pull request. You learned that it's important to write a succinct description of the changes you make to a project. Use imperative, present tense, and explain what and why and not how. These good practices will increase the likelihood of your changes getting merged. Finally, you learned how to communicate effectively with project maintainers and how to conduct code reviews.

