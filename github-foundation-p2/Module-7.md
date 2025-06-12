# Module 7: Search and organize repository history by using GitHub

## Unit 1: Introduction
GitHub projects support virtually unlimited scale. The upside of this scale is that your projects can grow to include countless files, commits, issues, pull requests, and more. The downside is, well, the same.

Suppose you're a developer working on a rapidly growing project. As more contributors come on board, they're able to add features and fix bugs at an incredible rate. However, every one of those changes likely includes a lot of contextual information buried in issues, discussions, commits, and pull requests. While that information seems fresh in everyone's mind at the time, the risk of losing that context as time passes could cost you some significant productivity down the road. What happens when a bug is reported that traces back to work that hasn't been touched for more than a year? Fortunately, GitHub offers a few ways to help you quickly ramp up for any task.

### Learning objectives

- Find relevant issues and pull requests.
- Search history to find context.
- Make connections within GitHub to help others find things.

## Unit 2: How to search and organize repository history by using GitHub
Here, we'll discuss how you can use filters, blame, and cross-linking to search and organize repository history.

Put yourself in the position of a developer who has just joined a large project. Someone just posted a new issue reporting a bug related to the web app's sidebar, and you've been assigned to fix it. You've already read through the report a few times and understand the problem being described, so now you need to figure out how to get started with the fix.

As a new team member, you're not yet familiar with the codebase. You also haven't been part of the planning discussions, code reviews, or anything else that would provide you with the context you need to start implementation. You'll first need to acquire that background knowledge to best determine the right fix.

### Searching GitHub
Although you weren't around for the events that led to the sidebar's implementation, many of those events live on in the project's history. Searching the project's repository for "sidebar" will give you a starting point.

There are two search methods available on GitHub: the global search at the top of the page and the scoped search available on certain repository tabs. They support the same syntax and function in the same way, but with some key differences.

#### Global search
The global search lets you use the complete search syntax to search across all of GitHub.

The search results are comprehensive and include everything from code to issues to the Marketplace (and even users). This is the best way to find mentions of key terms across multiple result types and repositories.

The filter clause is:pr filters out issues returned from the issues/pull requests store. Some filter clauses, such as is:pr, are only supported by certain search providers and ignored by others. For example, the code-search provider doesn't support that clause, so it will ignore it and return the same code results either way.

In our scenario, using the global search scoped to the current repository is a good way to find code and commits that mention the term "sidebar". You'll also likely get hits for issues and pull requests, although they're not as easy to filter further in the global search results view.

#### Context search
Context searches are available on certain tabs, such as Issues and Pull requests. These searches are scoped into the current repository and only return results of that type. The benefit to this scoping is that it allows the user interface to expose known type-specific filters such as authors, labels, projects, and more.

Using the context search is the preferred option when you're looking for something in the current repository. In our scenario, this is a good way to find search results mentioning "sidebar," which you could then easily refine using the filter dropdowns.

### Using search filters
There are an infinite number of ways to search using the complete search syntax. However, most searches only make use of a few common filters. While these are often available from context search dropdowns, it's sometimes more convenient to type them in directly.

### What is git blame?
Despite its ominous name, git blame is a command that displays the commit history for a file. It makes it easy for you to see who made what changes and when. This makes it much easier to track down other people who have worked on a file in order to seek out their input or participation.

Some Git systems alias git praise onto git blame to avoid the implication of judgment.

### Blame in GitHub
GitHub extends the basic git blame functionality with a more robust user interface.

In our scenario, there are a few ways you might get to this view. You might've found some sidebar code from the global search and selected the Blame option to see who worked on it last, or maybe you found a pull request and tracked that back to the last commit that seems related to the bug description. However you got here, the blame view is an effective way to locate a subject matter expert for the task at hand.

### Cross-linking issues, commits, and more
Part of what makes GitHub great for collaborative software projects is its support for linking disparate pieces of information together. Some of this happens automatically, such as when you create a pull request from a series of commits on a branch. Other times, you can use the interface to manually link pull requests or projects to issues using the dropdown options.

### Autolinked references
To make it even easier to cross-link different items throughout your project, GitHub offers a shorthand syntax. For example, if you leave a comment like Duplicate of #8, GitHub will recognize that #8 is an issue and create the appropriate link for you.

GitHub also links commits for you if you paste in the first seven or more characters of its ID.

In our scenario, these links could prove very valuable for ramping up if someone thought ahead to leave the context. For example, the sidebar's current state might have had some known issues related to a JavaScript dependency. If the issue with that dependency was discussed in another issue that didn't explicitly mention "sidebar," then it would be difficult to find. However, if someone had thought ahead to link the issue in the discussion, then it could save you a lot of time now. Keep that in mind the next time you're documenting issues and pull requests.


### Looping in users with @mention
Besides linking issues and commits, it's often helpful to associate other people with discussions. The easiest way to do this is by using an @mention. This kind of mention notifies the mentioned user so that they can participate in the discussion. It's also a good way to identify people associated with issues long after they have been closed.

