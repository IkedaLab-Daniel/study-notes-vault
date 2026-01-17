# Fundamentals of Building AI Agents

> # Module 1: Foundation of Tool Calling and Chaining

## Introduction to AI Agents Course

This course introduces AI agents and their growing importance in modern applications as businesses increasingly rely on intelligent systems that can reason, act, and solve problems in real time. AI agents are used across domains such as customer support, research, law, healthcare, data analysis, and report generation, creating strong demand for developers who can build task-driven, tool-integrated solutions.

The course is designed for aspiring software engineers, data scientists, machine learning engineers, AI architects, and related roles. Strong **Python programming skills** are required, along with recommended familiarity in core AI concepts and the **LangChain** framework.

The curriculum begins by explaining what AI agents are, how they differ from traditional workflows, and when to use them effectively. Learners gain a foundation in **tool calling and chaining** with LangChain, understanding why language models need tools and how function calling improves accuracy. Early activities include building a math assistant by converting functions into tools and orchestrating them with LangChain, as well as exploring LangChain’s built-in agents.

**Module 2** focuses on **LangChain Expression Language (LCEL)**, a concise, chain-first syntax for creating modular AI workflows. Learners practice manually invoking tools based on LLM outputs, parsing and validating tool calls, and building a tool-calling agent through a hands-on lab.

**Module 3** emphasizes building solutions using LangChain’s built-in agents. Learners create natural language data visualizations and conversational agents that query SQL databases using plain English, implementing two complete agents through guided walkthroughs.

To succeed, learners are encouraged to engage fully with videos, readings, practice quizzes, hands-on labs, and the graded assessment to solidify their understanding of AI agent development.

## What Are AI Agents and Why They Matter

AI agents emerge from a major shift in generative AI, moving away from **monolithic models** toward **compound AI systems**. Standalone models are limited by their training data, lack access to private or real-time information, and are costly to adapt through fine-tuning. While useful for tasks like summarization or drafting, their true power is unlocked when they are embedded within systems that integrate models with external data sources, tools, and logic.

## From Models to Compound AI Systems

Compound AI systems solve problems through **system design**, combining multiple modular components such as language models, databases, tools, and verification logic. A common example is **Retrieval Augmented Generation (RAG)**, where a model retrieves relevant information from a database before generating a response. These systems are faster to adapt and more flexible than retraining models, but they often rely on **fixed, human-defined control logic**, meaning every query follows the same predefined path.

## Control Logic and Its Limitations

In traditional compound systems, the control logic determines how queries are handled. This works well for narrow, well-defined problems but fails when queries fall outside the expected scope. The rigidity of predefined paths limits flexibility and scalability for complex or unpredictable tasks.

## Enter AI Agents: LLMs in Control

AI agents represent an **agentic approach**, where a large language model is placed in charge of the system’s control logic. This is enabled by advances in LLM reasoning capabilities. Instead of following fixed instructions, the model can:

* Think slowly and plan
* Break down complex problems
* Decide when and how to use external tools
* Iterate based on observations until a solution is reached

This shift moves systems along a spectrum from **low autonomy (programmatic, fast, rigid)** to **high autonomy (agentic, slow, flexible)**.

## Core Capabilities of AI Agents

### Reasoning

The model plans and reasons through problems step by step, rather than producing immediate answers.

### Acting (Tool Use)

Agents can call external tools such as web search, databases, calculators, APIs, code execution, or even other models, deciding dynamically which tools to use and when.

### Memory

Agents can store and retrieve information, including:

* Intermediate reasoning steps
* Past interactions and conversation history
  This enables continuity, learning, and personalization.

## The ReAct Pattern

A popular way to implement agents is the **ReAct (Reason + Act)** framework:

1. User query is sent to the LLM
2. The LLM plans and reasons about the problem
3. The LLM decides to call a tool
4. The system observes the tool’s output
5. The LLM adjusts its plan if needed
6. The loop continues until a final answer is produced

## Why Agentic Systems Are Powerful

Agentic systems excel at **complex, multi-step problems** with many possible solution paths. For example, solving a vacation planning question may involve:

* Retrieving personal vacation data
* Checking weather forecasts
* Consulting public health guidelines
* Performing calculations
  An agent can dynamically orchestrate all these steps without hardcoding every path.

## Choosing Between Programmatic and Agentic Approaches

* **Programmatic systems** are best for narrow, predictable tasks where efficiency and consistency matter.
* **Agentic systems** are better for broad, complex, and unpredictable tasks where flexibility and reasoning are required.

## The Road Ahead

Compound AI systems are here to stay, and they are becoming increasingly **agentic**. Developers will choose the level of autonomy based on trade-offs between efficiency, complexity, and control. While agentic systems are still evolving, combining system design with agent behavior is driving rapid progress, with humans remaining in the loop as accuracy continues to improve.

## Tool Calling in AI Systems

Tool calling is a technique that allows large language models (LLMs) to access **real-time or external data** such as APIs, databases, or executable code, making them context-aware beyond their training data. It is commonly implemented through a chat-based interaction between a client application and an LLM.

## Traditional Tool Calling

In traditional tool calling:

* The client application sends **messages plus tool definitions** to the LLM.
* Tool definitions include the tool name, description, and required input parameters.
* The LLM analyzes the user query and available tools, then **recommends which tool to call and how to call it**.
* The client executes the tool (for example, calling a weather API) and sends the result back to the LLM.
* The LLM uses the tool response to either request another tool call or generate the final answer.

### Example

A user asks for the temperature in Miami.

* The LLM selects the weather API tool.
* The client calls the API and gets the result (for example, 71°F).
* The LLM generates a final response using that data.

### Limitations

* The LLM may hallucinate.
* The LLM may generate incorrect or invalid tool calls.
* The client is responsible for managing tool execution and error handling.

## Embedded Tool Calling

Embedded tool calling improves reliability by introducing a **library or framework** between the application and the LLM.

* The library holds both the **tool definitions and tool execution logic**.
* The application sends only the user query to the library.
* The library appends tool definitions and communicates with the LLM.
* When the LLM requests a tool call, the **library executes it automatically**, handles retries, and manages errors.
* The library returns the final answer to the application.

## Benefits of Embedded Tool Calling

* Reduces hallucinations related to tool usage
* Prevents incorrect or malformed tool calls
* Automates tool execution and retries
* Simplifies application logic
* Improves robustness and reliability of agentic systems

## Key Takeaway

Tool calling enables LLMs to interact with real-world systems. While traditional tool calling gives flexibility, embedded tool calling offers a safer and more reliable approach by delegating tool execution and validation to a dedicated library or framework.
