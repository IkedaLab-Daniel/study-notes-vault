# Module 4: Configure Code Scanning

## Unit 1: Introduction
Imagine that you're the GitHub administrator for a project, and you want to make sure that the code doesn't include any security vulnerabilities or errors. It can be very time consuming to manually check your code base, especially if it's large. Your company just purchased a GitHub Advanced Security license that helps save time and effort by allowing you to use code scanning. With code scanning, you receive alerts indicating any problematic code. Then, you can quickly find the problem areas and make the necessary changes. In order to enable code scanning, you need to know what tools are available and what their features are. You also need to understand how often to perform code scanning and the types of events you can use to trigger scans.

This module introduces you to code scanning and its features. You'll learn how to implement code scanning using CodeQL, third-party tools, and GitHub Actions. You'll also learn about the different ways you can configure code scanning to optimize your experience.

## Unit 2: What is Code Scanning?
Code scanning uses CodeQL to analyze the code in a GitHub repository to find security vulnerabilities and coding errors. Code scanning is available for all public repositories, and for private repositories owned by organizations where GitHub Advanced Security is enabled. If code scanning finds a potential vulnerability or error in your code, GitHub displays an alert in the repository's Security tab. After you fix the code that triggered the alert, GitHub closes the alert.

You can use code scanning to find, triage, and prioritize fixes for existing problems in your code. Code scanning also prevents developers from introducing new problems. You can schedule scans for certain days and times, or trigger scans when a specific event occurs in the repository, such as a push.

### About code scanning with CodeQL
CodeQL is the code analysis engine GitHub developed to automate security checks. You can analyze your code using CodeQL and display the results as code scanning alerts. There are three main ways to set up CodeQL analysis for code scanning:

- Use default setup to quickly configure CodeQL analysis for code scanning on your repository. The default setup handles choosing the languages to analyze, query suite to run, and events that trigger scans with the option to manually configure the languages and query suites. This setup option runs code scanning as a GitHub Action.
- Use advanced setup to add the CodeQL workflow directly to your repository. Adding the CodeQL workflow directly into your repository generates a customizable workflow file, which uses the github/codeql-action to run the CodeQL CLI as a GitHub Action.
- Run the CodeQL CLI directly in an external CI system and upload the results to GitHub.

CodeQL treats code like data, allowing you to find potential vulnerabilities in your code with greater confidence than traditional static analyzers. You generate a CodeQL database to represent your codebase, then run CodeQL queries on that database to identify problems in the codebase. The query results are shown as code scanning alerts in GitHub when you use CodeQL with code scanning.

CodeQL supports both compiled and interpreted languages, and it can find vulnerabilities and errors in code written in the following supported languages:

- C or C++
- C#
- Go
- Java/Kotlin
- JavaScript/TypeScript
- Python
- Ruby
- Swift

### Enable CodeQL in your repository with the Default Setup
If you have write permissions to a repository, you can set up or configure code scanning for that repository.
Follow these steps to set up code scanning using the CodeQL GitHub Actions workflow:

1. On GitHub.com, navigate to the repository's main page.
2. Under your repository name, select Security.
3. Select Set up code scanning. If this option isn't available, ask an organization owner or repository administrator to enable GitHub Advanced Security.
4. In the Set up drop-down, select Default.
5. Review the default options. If needed, select the Edit button in the bottom left corner of the new window to customize how CodeQL runs.
The on:pull_request and on:push triggers are the default for code scanning are each useful for different purposes. You'll learn more about these triggers in the Configure Code Scanning unit.
6. Select Enable CodeQL once you're ready to turn on code scanning.
In the default CodeQL analysis workflow, code scanning is configured to analyze your code each time you either push a change to any protected branches or raise a pull request against the default branch. Once the push is made, code scanning runs automatically.

In the previous section, we enabled code scanning using the default setup, which runs code scans as a GitHub Action without needing to maintain a workflow file. The other option is Advanced setup, which generates the default workflow file you can edit for advanced configuration and more steps. We'll cover using the advanced setup for configuring code scanning in a later unit.

Running code scanning with GitHub Actions affects your monthly billing minutes. If you want to use GitHub Actions beyond the storage or minutes included in your account, you'll be billed for more usage.




