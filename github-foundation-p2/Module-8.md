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