# Develop your first agent with Microsoft Foundry

## Introduction
"Ready to dive in and start building AI agents? This fast-start, hands-on training is designed to get you up and running with Microsoft Foundry quickly. Whether you're new to AI development or looking to expand your skills, you'll be developing and deploying your first AI agent in an hour or less. We'll cover the key concepts you need to get started, and then jump straight into practical development, guiding you through the essential steps to create a working agent that can understand requests, use tools, and deliver intelligent responses."

## Generative AI and Agents

Generative AI is a branch of AI that enables software applications to generate new content; often natural language dialogs, but also images, video, code, and other formats.

For example, a computing history web site could provide a generative AI chat interface into which users can enter questions about key figures, technologies, and events in the history of computing.

The ability to chat with the site and have it generate original responses to questions creates a compelling interactive experience for users.

### How does generative AI work?
The ability to generate content is based on a language model, which has been trained with huge volumes of data - often documents from the Internet or other public sources of information.

Users interact with generative AI language models through prompts - natural language statements or questions. The language model in a generative AI solution uses the prompt to initiate the generation of a meaningful response.

Generative AI models encapsulate semantic relationships between language elements (that's a fancy way of saying that the models "know" how words relate to one another), and that's what enables them to generate a meaningful sequence of text.

There are large language models (LLMs) and small language models (SLMs) - the difference is based on the volume of data and the number of variables in the model. LLMs are powerful and generalize well, but can be more costly to train and use. SLMs tend to work well in scenarios that are more focused on specific topic areas or that require easily deployed small models for local applications and agents on devices.

### What are agents?
Agents are software applications built on generative AI that can reason over and generate natural language, automate tasks by using tools, and respond to contextual conditions to take appropriate action.

AI agents have three key elements:

- A large language model: This is the agent's brain; using generative AI for language understanding and reasoning.
- Instructions: A system prompt that defines the agent’s role and behavior. Think of it as the agent’s job description.
- Tools: These are what the agent uses to interact with the world. Tools can include:
    - Knowledge tools that provide access to information, like search engines or databases.
    - Action tools that enable the agent to perform tasks, such as sending emails, updating calendars, or controlling devices.

With these capabilities, AI agents can take on the role of digital assistants that intelligently automate tasks and collaborate with you to work smarter and more efficiently.

### Generative and agentic AI scenarios
Common uses of generative AI and agents include:

Creating chat bots that answer user questions or engage in conversation.
Implementing AI assistants that assist human users by automating tasks.
Creating new documents or other content (often as a starting point for further iterative development)
Automated translation of text between languages.
Summarizing or explaining complex documents.

## Prepare to Developer AI Solution on Azure
Microsoft Foundry is a platform for AI development on Microsoft Azure. While you can provision individual AI resources and build applications that consume them without it, the project organization, resource management, and AI development capabilities of Microsoft Foundry makes it the recommended way to build all but the most simple solutions.

Microsoft Foundry provides the Microsoft Foundry portal, a web-based visual interface for working with AI projects. It also provides the Microsoft Foundry SDK, which you can use to build AI solutions programmatically.

### Microsoft Foundry projects
In Microsoft Foundry, you manage the resource connections, data, code, and other elements of the AI solution in a project. Each project belongs to a single Microsoft Foundry resource in Azure, which provides compute, data storage, AI tools, and other services.

A Foundry resource can support one or more child projects, with one of them being designated the default project.

Developers use projects to manage the assets needed for an AI solution, including:
- Models: Large language model (LLM) deployments based on models available in Foundry Models - a comprehensive catalog of models from Microsoft OpenAI, and other providers. You can connect to and interact with these models through the project endpoint (using Foundry-specific APIs and SDKs) and the Azure OpenAI endpoint (using OpenAI APIs and SDKs).

- Agents: Named AI configurations that encapsulate an LLM, instructions, and tools to define an autonomous AI entity that can automate tasks and collaborate with users and other agents. Agents in Foundry are developed and consumed using the Microsoft Foundry Agent service through the project endpoint.

- Tools: The tools used by agents can be based on built-in functionality, such as web search or a code interpreter, or connections to custom and third-party tools through Model Context Protocol (MCP) connections. Additionally, Microsoft Foundry Tools includes a suite of AI services for common tasks such as text analysis, speech recognition and synthesis, translation, and content understanding that you can use in your Foundry-based AI solutions. Foundry Tools are hosted in the Foundry resource associated with your project(s).

- Knowledge: Agents can use tools to connect to knowledge stores, and use the data they contain to contextualize prompts. To simplify integration with multiple sources of knowledge, you can use Foundry IQ in a project to create a single, central MCP-based knowledge connection.

The separation of project-specific assets and cloud services in Microsoft Foundry resources supports the most common AI development tasks to develop generative AI chat apps and agents. Using a Foundry project provides the right level of resource centralization and capabilities with a minimal amount of administrative resource management.

### The Microsoft Foundry portal
You can use Microsoft Foundry portal to develop and manage projects that are based in Microsoft Foundry resources.

Most AI solution development projects begin in the Foundry project, where you can:

- Find, compare, deploy, and test models.
- Create and test agents.
- Create MCP connections to tools and Foundry IQ knowledge sources.
- Explore and test Microsoft Foundry tools.
- Manage resource configuration and user access.
- Find the endpoints and keys you need to access assets from client applications.

To automate Foundry project operations, you can also use the Microsoft Foundry SDK - enabling you to create and manage assets using scripts or automated CI/CD actions in DevOps pipelines.