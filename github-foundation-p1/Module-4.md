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

### About Billing for Actions
Code scanning uses GitHub Actions, and each run of a code-scanning workflow consumes minutes for GitHub Actions. GitHub Actions usage is free for both public repositories and self-hosted runners. For private repositories, each GitHub account receives a certain number of free minutes and storage, depending on the product used with the account. Spending limits control any usage beyond the included amounts. If you're a monthly billed customer, your account has a default spending limit of zero US dollars (USD), which prevents extra usage of minutes or storage for private repositories beyond the amounts included with your account. If you pay your account by invoice, your account will have an unlimited default spending limit. Minutes reset every month, while storage usage doesn't.

## Unit 3: Enable code scanning with third party tools
Instead of running code scanning in GitHub, you can perform analysis elsewhere and then upload the results. Alerts for code scanning that you run externally are displayed in the same way as those you run within GitHub. You can upload Static Analysis Results Interchange Format (SARIF) files generated outside GitHub or with GitHub Actions to see code scanning alerts from third-party tools in your repository.

### About SARIF file uploads for code scanning
GitHub creates code-scanning alerts in a repository using information from SARIF files. You can generate SARIF files using many static analysis-security testing tools, including CodeQL. The results must use SARIF version 2.1.0.

You can upload the results using the code-scanning API, the CodeQL CLI, or GitHub Actions. The best upload method will depend on how you generated the SARIF file.

### Code-scanning API
The code-scanning API lets you retrieve information on code scanning alerts, analyses, databases, and default setup configuration from a repository. Additionally, you can update code-scanning alerts and the default setup configuration. You can use the endpoints to create automated reports for the code-scanning alerts in an organization or upload analysis results generated using offline code-scanning tools.

You can access the GitHub API over HTTPS from https://api.github.com. All data is sent and received as JSON. The API uses custom media types to let consumers choose the format of the data they wish to receive. Media types are specific to resources, allowing them to change independently and support formats that other resources don't.

There's one supported custom media type for the code scanning REST API, application/sarif+json.

You can use this media type with GET requests sent to the /analyses/{analysis_id} endpoint. When you use this media type with this operation, the response includes a subset of the actual data that was uploaded for the specified analysis, rather than the summary of the analysis that's returned when you use the default media type. The response also includes additional data such as the github/alertNumber and github/alertUrl properties. The data is formatted as SARIF version 2.1.0.

The following is an example cURL command using the API to list the code scanning alerts for an organization:

```bash
curl -L \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <YOUR-TOKEN>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/orgs/ORG/code-scanning/alerts
```

### CodeQL CLI
The CodeQL CLI is a standalone product that you can use to analyze code. Its main purpose is to generate a database representation of a codebase, a CodeQL database. Once the database is ready, you can query it interactively, or you can run a suite of queries to generate a set of results in SARIF format and upload the results to GitHub.com. The CodeQL CLI is free to use on public repositories maintained on GitHub.com, and it's available to use on customer owned private repositories with an Advanced Security license. Download the CodeQL bundle from https://github.com/github/codeql-action/releases.

The bundle contains:
- CodeQL CLI product
- A compatible version of the queries and libraries from https://github.com/github/codeql
- Precompiled versions of all the queries included in the bundle

You should always use the CodeQL bundle, because this ensures compatibility and also gives much better performance than a separate download of the CodeQL CLI and checkout of the CodeQL queries.

### Code-scanning analysis with GitHub Actions

To use GitHub Actions to upload a third-party SARIF file to a repository, you'll need a GitHub Actions workflow. A GitHub Actions workflow is an automated process, made up of one or more jobs, configured as a .yml file. Workflows are stored in the .github/workflows directory for your repository.

Your workflow uses the upload-sarif action, which is part of the github/codeql-action repository. This workflow includes input parameters that you can use to configure the upload.

The main input parameter is sarif-file, which configures the file or directory of SARIF files to be uploaded. The directory or file path is relative to the root of the repository.

The upload-sarif action can be configured to run when the push and scheduled event occurs.

This example outlines the elements of the upload-sarif action yml file:
```yml
name: 'Code Scanning : Upload SARIF'
description: 'Upload the analysis results'
author: 'GitHub'
inputs:
  sarif_file:
    description: |
      The SARIF file or directory of SARIF files to be uploaded to GitHub code scanning.
      See https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/
      uploading-a-sarif-file-to-github#uploading-a-code-scanning-analysis-with-github-actions
      for information on the maximum number of results and maximum file size supported by code scanning.
    required: false
    default: '../results'
  checkout_path:
    description: "The path at which the analyzed repository was checked out. 
    Used to relativize any absolute paths in the uploaded SARIF file."
    required: false
    default: ${{ github.workspace }}
  token:
    default: ${{ github.token }}
  matrix:
    default: ${{ toJson(matrix) }}
  category:
    description: String used by Code Scanning for matching the analyses
    required: false
  wait-for-processing:
    description: If true, the Action will wait for the uploaded SARIF to be processed before completing.
    required: true
    default: "false"
runs:
  using: 'node12'
  main: '../lib/upload-sarif-action.js'
```

Each time the results of a new code scan are uploaded, the results are processed and alerts are added to the repository. GitHub uses properties in the SARIF file to display alerts. For example, to prevent duplicate alerts for the same problem, code scanning uses fingerprints to match results across various runs so they only appear once in the latest run for the selected branch. SARIF files created by the CodeQL analysis workflow include this fingerprint data in the partialFingerprints field. If you upload a SARIF file using the upload-sarif action and this data is missing, GitHub attempts to populate the partialFingerprints field from the source files.

If your SARIF file doesn't include partialFingerprints, the upload-sarif action will calculate the partialFingerprints field for you and attempt to prevent duplicate alerts. GitHub can only create partialFingerprints when the repository contains both the SARIF file and the source code used in the static analysis.

SARIF upload supports a maximum of 5,000 results per upload. Any results over this limit are ignored. If a tool generates too many results, you should update the configuration to focus on results for the most important rules or queries.

For each upload, SARIF upload supports a maximum size of 10 MB for the gzip-compressed SARIF file. Any uploads over this limit will be rejected. If your SARIF file is too large because it contains too many results, you should update the configuration to focus on results for the most important rules or queries.

### Upload SARIF files generated outside your repository
You can also create a new workflow that uploads SARIF files after you commit them to your repository. This is useful when the SARIF file is generated as an artifact outside of your repository.

In the following example, the workflow runs anytime commits are pushed to the repository. The action uses the partialFingerprints property to determine if changes have occurred.

In addition to running when commits are pushed, the workflow is scheduled to run once per week. This workflow uploads the results.sarif file located in the root of the repository. You could also modify this workflow to upload a directory of SARIF files. For example, you could place all SARIF files in a directory in the root of your repository called sarif-output and set the action's input parameter sarif_file to sarif-output.
```yml
name: "Upload SARIF"

// Run workflow each time code is pushed to your repository and on a schedule. 
//The scheduled workflow runs every Thursday at 15:45 UTC.

on:
  push:
  schedule:
    - cron: '45 15 * * 4'

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
  steps:
    # This step checks out a copy of your repository.
    - name: Checkout repository
      uses: actions/checkout@v2
    - name: Upload SARIF file
      uses: github/codeql-action/upload-sarif@v1
      with:
        # Path to SARIF file relative to the root of the repository
        sarif_file: results.sarif
```

### Upload SARIF files generated as part of a CI workflow
If you generate your third-party SARIF file as part of a continuous integration (CI) workflow, you can add the upload-sarif action as a step after running your CI tests. If you don't already have a CI workflow, you can create one using a starter workflow in the https://github.com/actions/starter-workflows repository.

In this example, the workflow runs anytime commits are pushed to the repository. The action uses the partialFingerprints property to determine if changes have occurred. In addition to running when commits are pushed, the workflow is scheduled to run once per week.

This example shows the ESLint static analysis tool as a step in a workflow. The Run ESLint step runs the ESLint tool and outputs the results.sarif file. The workflow then uploads the results.sarif file to GitHub using the upload-sarif action.

```yml
  name: "ESLint analysis"

// Run workflow each time code is pushed to your repository and on a schedule.
// The scheduled workflow runs every Wednesday at 15:45 UTC.
on:
  push:
  schedule:
    - cron: '45 15 * * 3'

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
    steps:
      - uses: actions/checkout@v2
      - name: Run npm install
        run: npm install
      // Runs the ESlint code analysis
      - name: Run ESLint
        // eslint exits 1 if it finds anything to report
        run: node_modules/.bin/eslint build docs lib script spec-main -f node_modules/@microsoft/eslint-formatter-sarif/sarif.js -o results.sarif || true
      // Uploads results.sarif to GitHub repository using the upload-sarif action
      - uses: github/codeql-action/upload-sarif@v1
        with:
          // Path to SARIF file relative to the root of the repository
          sarif_file: results.sarif
```

## Unit 4: Configure code scanning
You can configure how GitHub scans the code in your project for vulnerabilities and errors. When you choose your own configuration, you save time and decide the best frequency of code scanning for your project.

As we discussed in the previous units, you can run code scanning on GitHub, using GitHub Actions, or from your continuous integration (CI) system. Selecting the Advanced setup option on GitHub generates a customizable workflow file that you can then commit directly to your repository. You usually don't need to edit this workflow. However, if necessary, you can customize some of the settings.

For example, you can edit GitHub's CodeQL analysis workflow to specify the frequency of scans, the languages or directories to scan, and what CodeQL code scanning looks for in your code. You might also need to edit the CodeQL analysis workflow if you use a specific set of commands to compile your code. CodeQL analysis is just one type of code scanning you can perform in GitHub. The GitHub Marketplace contains several other code scanning workflows.

### Switching from Default to Advanced Code Scanning Setup
If you already have a repository set up to use code scanning using the default setup method, you can switch to using the Advanced setup in the settings. Navigate to the Code scanning section under Settings > Code security and analysis, and then select the three dots overflow icon (...). In the drop-down, select Switch to advanced. Then, follow the prompts to disable CodeQL, and re-enable it with the advanced setup's generated workflow file.

### Edit code-scanning workflow
GitHub saves workflow files in the .github/workflows directory of your repository. You can find a workflow you have added by searching for its file name. For example, by default, the workflow file for CodeQL code scanning is called codeql-analysis.yml. Follow these steps to edit a workflow file:
1. To open the workflow editor, select the Edit icon in the upper-right corner of the file view.
2. Make your edits.
3. After you have edited the file, select Commit changes and complete the Commit changes form. You can choose to commit directly to the current branch, or create a new branch and start a pull request.

### Configure Frequency
A common edit to the workflow file is to adjust the frequency with which code scanning occurs. You can configure the CodeQL analysis workflow to scan code on a schedule or when specific events occur in a repository. You can also edit the workflow file to scan code when someone pushes a change and whenever a pull request is created. Adjusting this frequency prevents developers from introducing new vulnerabilities and errors into the code. Scanning code on a schedule informs you about the latest vulnerabilities and errors that GitHub, security researchers, and the community discover. Even when developers aren't actively maintaining the repository.

### Scan on Push
By default, the CodeQL analysis workflow uses the on:push event to trigger a code scan on every push to the default branch of the repository and any protected branches. For code scanning to be triggered on a specified branch, the workflow must exist in that branch. If you scan on push, the results appear in the Security tab for your repository.

Additionally, when an on:push scan returns a result that can be mapped to an open pull request, these alerts automatically appear on a pull request in the same place as other pull request alerts. The alerts are identified by comparing the existing analysis of the head of the branch to the analysis for the target branch.

### Scan on PR
The default CodeQL analysis workflow uses the pull_request event to trigger a code scan on pull requests targeted against the default branch. If a pull request is from a private fork, the pull_request event is only triggered if you've selected the "Run workflows from fork pull requests" option in the repository settings. If you scan pull requests, the results appear as alerts in a pull-request check.

If you use the pull_request trigger, configured to scan the pull request's merge commit rather than the head commit, it produces more efficient and accurate results than scanning the branch head on each push. However, if you use a CI/CD system that can't be configured to trigger on pull requests, you can still use the on:push trigger so that code scanning maps the results to open pull requests on the branch and adds the alerts as annotations on a pull request.

### Define the severities causing pull request check failure
By default, only alerts with the severity level of Error or security severity level of Critical or High cause a pull-request check failure. Pull-request failures don't stop a code scan but represent a blocker when trying to merge code. You can find the list of pull-request failures in the Code scanning alerts tab under your repository's Security. In your repository settings, you can change the levels of alert severities and of security severities that cause a pull request check failure.

1. On GitHub.com, navigate to the repository main page. Under your repository name, select Settings.
2. In the left sidebar, select Code security and analysis.
3. In the Code scanning section under Protection rules, use the drop-down menu to select the severity level you would like to trigger a pull request check failure.

### Avoid unnecessary scans of pull requests
You might want to avoid a code scan being triggered on specific pull requests targeted against the default branch, irrespective of which files have been changed. You can configure this setting by specifying on:pull_request:paths-ignore or on:pull_request:paths in the code-scanning workflow. For example, if the only changes in a pull request are to files with the file extensions .md or .txt you can use the following paths-ignore array.
```yml
on:
   push:
      branches: [main, protected]
   pull_request:
      branches: [main]
      paths-ignore:
         - '**/*.md'
         - '**/*.txt'
```

### Adjust scanning schedule
If you use the default CodeQL analysis workflow, the workflow scans the code in your repository once a week at a randomly generated day and time, in addition to the scans triggered by events. To adjust this schedule, edit the cron value in the workflow.

The following example shows a CodeQL analysis workflow for a repository with a default branch called main and one protected branch called protected:

```yml
on:
   push:
      branches: [main, protected]
   pull_request:
      branches: [main]
   schedule:
      - cron: '20 14 * * 1'
```
This workflow scans:

Every push to the default branch and the protected branch
Every pull request to the default branch
The default branch every Monday at 14:20 UTC

Unit 5: Lab

Unit 6: Quiz

Unit 7: Summary
In this module, you learned how to enable and configure code scanning for your repository. Code scanning works with the integrated GitHub CodeQL action or with third party tools. You can schedule or trigger it based on specific events, saving time and ensuring your code stays free of errors and security vulnerabilities. Without code scanning, you'd need to manually verify the code base, which can take a lot of time and has a higher potential for mistakes. Code scanning alerts you of any problems and lets you review these issues in a single location.

