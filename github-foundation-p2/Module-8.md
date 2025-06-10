# Module 8: Using GitHub Copilot with Python

## Unit 1: Introduction
GitHub Copilot is an AI coding partner that provides autocomplete suggestions while you code. You get suggestions from Copilot by typing code or describing it in natural language.

Copilot analyses your file and related files, offering suggestions in your text editor. It uses OpenAI Codex, a new AI system developed by OpenAI, to help derive context from written code and comments, and then suggests new lines or entire functions.

GitHub Codespaces is a hosted developer environment operating in the cloud that can be run with Visual Studio Code. You can customize the development experience for any development project on GitHub, preinstalling dependencies, libraries, and even Visual Studio Code extensions and settings.

As a developer, you want to be more productive when you're typing code for new projects and existing ones. For this task, you want to find out if an AI assistant is what you need to improve your developer workflows in code writing, documentation, testing, and more.

## Unit 2: What is GitHub Copilot?
Often, when you write code, you need to consult official documentation or other web pages to remember syntax or how to solve a problem. You can also spend hours trying to resolve a problem when the code isn't working. Additionally, you also spend time writing tests and documentation. All these tasks are time consuming. To be more efficient, you could use code snippets or rely on tooling in your integrated development environment (IDE). But is there a better way?

### How does it work?
GitHub Copilot is an AI assistant that you use from within your IDE that’s capable of generating code and much more. GitHub Copilot uses prompts. A prompt is natural language text that you type. Copilot uses the text to provide suggestions based on what you type.

###  How it recognizes prompts
Copilot can tell that something is a prompt or an instruction if you:

- Type it as a comment in a code file with a file ending like .py or .js.
- Type text in a markdown file and wait a few seconds for Copilot to return a response.

### Accepting suggestions
What you get back from Copilot is a suggestion, or text that shows itself as gray code, if you use black as your text color. To accept the suggestion, you need to press the Tab key.

Copilot might suggest more than one thing. In this case, you can cycle between suggestions by using Ctrl + Enter, and select the most appropriate one.

## Unit 3: Lab

## Unit 4: Use GitHub Copilot with Python

### Developing with GitHub Copilot
Often when we build out projects, we need to continuously ensure our code is fresh and updated. Additionally, we might need to fix any bugs that come up or add new features to improve functionality and usability. Let's explore some ways to make updates with GitHub Copilot and GitHub Copilot Chat, an interactive chat interface that lets you ask and receive answers to code-related questions.

#### Prompt engineering
GitHub Copilot can suggest code as you enter it, but you can also create useful suggestions by building prompts. A prompt, which is our input, is a collection of instructions or guidelines that help generate code. A prompt is useful to generate specific responses from Copilot. The prompt might be a comment or input when using GitHub Copilot Chat that steers Copilot to generate code on your behalf or writing code that Copilot autocompletes.

The quality of output from Copilot depends on how well you craft your prompt. Designing an effective prompt is crucial to ensuring you achieve your desired outcome.

### Best practices using GitHub Copilot
Copilot supercharges your productivity but requires some good practices to ensure quality. Some best practices when using Copilot are:

Keep your prompts simple then add more elaborate components as you keep going. For example:
```bash
create an HTML form with a text field and button
```
Next, elaborate more on the prompt to get more specific suggestions:
```bash
Add an event listen to the button to send a POST request to /generate endpoint and display response in a div with id "result"
```
Cycle between suggestions. You can do this using Ctrl+Enter (or Cmd+Enter on a Mac). You get various suggestions from Copilot, and you can pick the best output. Optionally, when using GitHub Copilot Chat, you can use the chat input to add your prompt and interact with the output.

If you're not getting the results you want, then you can reword the prompt or start writing code for Copilot to autocomplete.

GitHub Copilot uses open files in your text editor as additional context. This is helpful because it provides useful information in addition to the prompt or code you may be writing. If you need GitHub Copilot to provide suggestions based on other files you can open those or use @workspace with your prompt when using GitHub Copilot Chat.

## Unit 5: Lab

## Unit 6: Quiz

## Unit 7: Summary
In this module, we looked at how GitHub Codespaces can significantly improve the software development lifecycle. We learned about the features of GitHub Codespaces that range from creating a repository from a GitHub template to adding animations with live suggestions. GitHub Codespaces allows you to customize your coding experience and GitHub Copilot guides you in each step of the way.

After finishing this module, you should be able to:

- Configure a GitHub repository in Codespaces and install the GitHub Copilot extension.
- Engineer prompts for your project that follow best practices to generate suggestions from GitHub Copilot.
- Use GitHub Copilot Chat to ask coding-related questions and receive answers.

### Delete your Codespaces resources
To avoid consuming all of your monthly GitHub Codespaces time, it's important to delete your resources after you upload your changes to your repository.

Use the following steps to delete your Codespace instance:
- Go to GitHub Codespaces.
- Find your Codespace instance in the list, and select the ... menu to display your options.
- Select Delete to remove your Codespace instance.