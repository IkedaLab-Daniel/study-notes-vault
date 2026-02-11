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

## Why AI Needs Tools: From Guessing to Real-World Action

* Large Language Models (LLMs) are powerful at generating human-like text but are limited to pattern recognition and guessing without tools.
* On their own, LLMs cannot access real-time data, perform reliable math, call APIs, or interact with the real world, which leads to errors and hallucinations.
* Tools enable LLMs to move beyond text generation into accurate problem-solving and real-world action.
* With tools, LLMs can:

  * Retrieve external information such as company documents, personal files, or specialized databases (Retrieval-Augmented Generation or RAG).
  * Process non-text data like images, audio, and multimodal inputs.
  * Maintain memory across sessions and handle data beyond context window limits.
  * Interact with APIs, software, and digital services to perform real actions.
* Tools significantly improve accuracy, such as using a calculator to perform correct mathematical computations instead of guessing.
* Examples of tools include calculators, web access, search engines, code execution environments, SQL databases, and visualization tools.
* When equipped with tools, LLMs become intelligent, agentic systems that can observe, reason, and act.
* The agentic workflow follows a clear loop: user request → tool selection → tool execution → meaningful response.
* Tools are essential for transforming LLMs from unreliable guessers into precise, real-world problem solvers.

## Build Effective AI Tools for Advanced LLMs

* LLMs understand and generate language, while agents extend LLMs by using tools to take real-world actions and make decisions.
* Tools are functions that allow LLMs to access live data, perform precise calculations, retrieve private or enterprise data, execute actions, and support multi-step reasoning.
* These capabilities transform LLMs from passive text generators into active, goal-driven agents.
* In frameworks like LangChain, tools are typically Python functions with a single, well-defined purpose.
* Effective tools require:

  * A clear and descriptive name that reflects the tool’s intent.
  * Well-defined, standardized inputs that are easy for LLMs to parse, often strings or structured JSON.
  * Comprehensive documentation or docstrings describing purpose, parameters, outputs, examples, and limitations.
  * A reliable function body that performs the intended logic.
  * Consistent and predictable outputs, usually returned in a dictionary format.
* Tool calling follows a structured flow: user query → parameter extraction → tool selection → tool execution → result returned to the LLM.
* Simple tools may accept unstructured string input, while structured tools support multiple typed inputs and named parameters.
* The `Tool` class and `@tool` decorator in LangChain allow wrapping Python functions into agent-compatible tools, with the decorator offering cleaner syntax and better support for structured inputs.
* Structured tools define input schemas using Python typing, enabling lists, booleans, and other JSON-serializable types.
* Optional parameters and default values allow flexible tool behavior, such as summing absolute values when requested.
* Tools can return variable outputs, including success results or error messages, using typing constructs like `Dict` and `Union`.
* Testing is essential, as different LLMs and agents may vary in how well they handle structured inputs and outputs.
* Careful tool design, clear interfaces, and version control are critical due to the fast-evolving nature of agent frameworks like LangChain.
* Well-designed tools enable context-aware workflows and allow agents to orchestrate multiple tools for smarter, more reliable responses.

## Build Intelligent Agents for Dynamic LLM Tool Use

* Intelligent agents combine an LLM with one or more tools to reason, act, and interact with real-world data, going beyond simple text generation.
* Agents make decisions, call tools, and manage multi-step logic, making them suitable for complex workflows where static prompts are insufficient.
* When building agents in LangChain, key considerations include:

  * **LLM choice**: Not all models support tool use or advanced reasoning; model capabilities directly affect agent behavior.
  * **Tool design**: Tools must use JSON-serializable inputs and outputs, with structured tools preferred for clarity and reliability.
  * **Agent strategy**: Different agents suit different tasks, such as simple agents versus ReAct agents for multi-step reasoning.
* Agents follow a reasoning loop: receive user input, reason about the task, select and call tools, observe results, decide next steps, and generate a final response.
* The ReAct framework enables step-by-step reasoning, tool usage, observation, and planning until a solution is reached.
* Zero-shot ReAct agents can solve unseen tasks by reasoning through problems without prior examples, ideal for well-structured tasks.
* In LangChain, `initialize_agent` simplifies agent creation by combining an LLM, tools, and a chosen agent type in one step.
* The `verbose` option reveals the agent’s reasoning process, while error-handling options help recover from malformed tool outputs.
* The `run` method is used for simple agents, while `invoke` is preferred for debugging and complex workflows.
* Tool compatibility matters: some agents expect plain string inputs and outputs, while others support structured tools with typed parameters.
* Structured ReAct agents enable typed inputs, optional parameters, and structured outputs like JSON, improving flexibility and debugging.
* Different LLMs work better with different agent types; some models handle complex or structured outputs more reliably than others.
* Selecting the correct agent type ensures proper handling of multi-input tools and complex return values.
* Effective agent design relies on experimentation due to the rapid evolution of LangChain and LLM capabilities.
* Well-designed agents transform LLMs into dynamic, context-aware systems capable of precise, multi-step problem solving.
s

## Build a Custom Math Toolkit Agent with LangChain

* The video demonstrates how to build flexible, custom agents using **LangChain and LangGraph**, focusing on math-focused toolkits and multi-step reasoning.
* You learn to create a **custom math toolkit** with tools for addition, subtraction, multiplication, and division, instead of relying on a single tool.
* LangGraph is introduced as a more flexible and robust alternative to `initialize_agent`, especially for complex, multi-step workflows.
* Using **create_react_agent**, you can fully customize the agent’s prompt, giving more control over reasoning style and behavior compared to predefined agent strategies.
* Agents are created by passing an **LLM**, a **list of tools**, and optionally a **custom prompt** that defines the agent’s role, such as a helpful math assistant.
* Interaction with agents is done through the **invoke method**, passing structured chat-style messages.
* The agent reasons through the query, selects the appropriate tool, executes it, validates the output, and returns a final response.
* Full agent responses include **tool call traces and intermediate steps**, which are useful for debugging and understanding agent behavior.
* Real-world agents often require **multiple tools**, as a single tool cannot handle all user requests.
* A multi-tool math agent demonstrates how agents dynamically choose the correct tool based on the query.
* LangChain provides many **prebuilt tools**, such as Wikipedia search, web search, Python execution, weather queries, and video search.
* You learn to build a **custom Wikipedia search tool** using the Tool Decorator and LangChain’s community integrations, with clear input/output types and documentation.
* By combining math tools with the Wikipedia search tool, the agent can handle **hybrid queries** that require both information retrieval and calculation.
* Example workflow: retrieve Canada’s population from Wikipedia, then apply a math tool to compute a percentage of it.
* Key takeaways include building ReAct-style agents with full customization, orchestrating multiple tools in one agent, guiding behavior with prompts, and extending agents with external data sources for real-world, multi-step problem solving.

## Summary M1: Foundations of Tool Calling and Chaining
- Use simple LLM features for basic tasks, use workflows for predictable and efficient operations, and deploy agents only when complex reasoning or adaptability is needed.
- AI agents sit at the highest end of the AI complexity spectrum, excelling at tasks that require autonomous decision-making, adaptation, and strategy. 
- Use the four-step decision framework—task ambiguity, step flexibility, tool variety, and failure impact—to decide if an AI agent is the right fit for the task. 
- Avoid using AI agents for simple, repeatable, or high-risk tasks where errors are costly or predictable; tools can perform better. 
- Today's AI agents struggle with reliability, high compute costs, and often need human oversight to avoid hallucinations or missteps. 
- Manage risks associated with AI agents by setting boundaries, using logs, monitoring outcomes, and keeping a human in the loop for oversight. 
- Effective AI agent architecture includes modular components like memory, tool use, planning strategies, and clear reasoning paths.Tool calling enhances LLM capabilities by connecting them to real-time external data and functionality. 
- Embedded tool calling improves LLM accuracy and reduces hallucinations by centralizing tool handling within a dedicated library or framework, replacing error-prone client-side implementations.
- Tools help LLMs access external data and support RAG, enabling the use of the organization's or other specialized databases.
- Tools help process images, audio, and video to enable vision, voice, and multimodal reasoning, manage long conversations, and connect to APIs to perform real-world actions.
- The Zero-Shot ReAct Agent uses zero-shot reasoning to solve tasks it hasn't seen before and works best for simple or well-structured problems.

> # Module 2: LCEL and Manual Tool Calling in Langchain

## LangChain LCEL (LangChain Expression Language) Chaining Method

### Overview

LCEL is LangChain’s modern, recommended way to build AI workflows. It uses the **pipe (`|`) operator** to connect components, creating clean, readable, and composable chains that move data from input to output.

Compared to older LLMChain approaches, LCEL offers:

* Clearer data flow
* Better composability
* Easier visualization of pipelines
* More flexibility for building complex systems

### Core LCEL Workflow

A typical LCEL chain follows these steps:

1. Define a prompt template using variables in `{curly_braces}`
2. Create a PromptTemplate instance
3. Connect components with the pipe (`|`) operator
4. Invoke the chain with input values

### Runnables: Building Blocks of LCEL

LCEL is built on **runnables**, which connect prompts, LLMs, retrievers, tools, and functions into pipelines.

There are two main composition types:

#### RunnableSequence

* Runs components sequentially
* Output of one becomes input to the next
* In LCEL, this is simply written with `|`

#### RunnableParallel

* Runs multiple components at the same time using the same input
* Created automatically when you use a dictionary

### Elegant Syntax with the Pipe Operator

Instead of explicitly creating RunnableSequence objects, LCEL lets you write:

```
component1 | component2 | component3
```

This produces a sequential chain with much cleaner syntax.

### Automatic Type Coercion

LCEL automatically converts common Python objects into runnable components:

* **Functions → RunnableLambda**
* **Dictionaries → RunnableParallel**

You don’t need to handle this manually.

Example behavior:

* A function becomes a transformation step
* A dictionary triggers parallel execution
* Each parallel task receives the same input

This allows patterns like:

* Summarization
* Translation
* Sentiment analysis

to run simultaneously from a single input.

### Example Flow (Conceptual)

1. RunnableLambda formats a prompt using input variables
2. Pipe sends formatted prompt to the LLM
3. Pipe sends LLM output to an output parser (for example, StrOutputParser)

Each step is connected with `|`, forming a readable pipeline.

### Parallel Execution Example

Using a dictionary automatically creates RunnableParallel:

* Same input goes to multiple tasks
* Outputs are returned as keyed results (for example: summary, translation, sentiment)

### When to Use LCEL vs LangGraph

* **Use LCEL** for simpler orchestration and linear or parallel pipelines
* **Use LangGraph** for complex, multi-step agent workflows
* LCEL can still be used *inside* LangGraph nodes

### Key Advantages of LCEL

* Pipe-based readable chaining
* Parallel execution support
* Async compatibility
* Simplified streaming
* Automatic tracing
* Reduced boilerplate
* Reusable chain patterns

## When to Call Tools Manually

### Overview

LLMs can recommend tools and parameters to solve tasks, and agents can automatically execute these tools. While automation is powerful, manual tool invocation gives developers greater control, safety, and accuracy—especially in sensitive or high-risk systems.

### How Tool Suggestion and Execution Works

* LLMs analyze user input and **suggest which tool to use**, along with required parameters (for example, location for a weather API).
* Agents can then **automatically execute** the suggested tool and return results to the user.
* This creates a fast, hands-free workflow—but removes human oversight.

### Why Manual Tool Invocation Matters

Automatic execution isn’t always ideal. Manual invocation is preferred when:

#### Safety

* Prevents unintended or risky actions (for example, modifying financial or production databases).
* Allows validation before executing sensitive operations.

#### Cost Control

* Avoids unnecessary API calls or expensive operations.
* Lets developers decide when a tool is truly needed.

#### Accuracy

* Ensures tools are called with correct parameters.
* Allows verification of inputs and outputs before accepting results.

### Agents vs Manual Control

* **Agents**: Fully automate tool execution based on LLM recommendations.
* **Manual invocation**: Developers review tool choices, validate parameters, and explicitly trigger execution.

Manual control keeps humans “in the loop,” making it easier to:

* Inspect LLM recommendations
* Approve or reject actions
* Adjust parameters
* Confirm results

### Key Takeaways

* LLMs can suggest tools and required inputs, but humans should evaluate those suggestions.
* Agents automate execution, improving speed—but reducing oversight.
* Manual invocation provides:

  * Greater safety
  * Better cost management
  * Higher accuracy
* Choosing between automation and manual control depends on your use case, especially for high-stakes or regulated environments.

Manual tool invocation puts you back in the driver’s seat—offering precision, reliability, and peace of mind when building real-world AI systems.

## Build LLM Agents with Tools (Manual Tool Calling)

### Overview

This video introduces the first steps in **manual tool calling**, showing how to turn a basic LLM into an interactive agent by connecting it to custom tools like arithmetic functions.

The goal is to let the LLM **identify when a tool is needed, extract parameters, call the tool, and use the result to generate a final response**.

---

### Core Workflow

1. User asks a question (for example: *What is 3 plus 2?*)
2. The LLM:

   * Understands the intent
   * Extracts parameters (3 and 2)
   * Selects the correct tool (add)
3. The tool executes the operation.
4. The result is returned to the LLM.
5. The LLM produces a natural-language answer (5).

This is the foundation of an agent that can interact with the real world.

---

### Initializing the Chat Model

* Use `initChatModel` to create a chat-capable LLM.
* Load a model (for example, GPT-4.0 mini via OpenAI).
* Store it as `LLM`.
* From this point on, `LLM.invoke()` is how you communicate with the model.

The LLM becomes the central hub for user queries and tool calls.

---

### Creating Custom Tools

* Use the `@tool` decorator to mark Python functions as callable tools.
* Example: an `add(a, b)` function that returns `a + b`.
* The tool’s docstring tells the LLM **when and how** to use it.

At this stage, tools exist—but are not yet connected to the model.

---

### Binding Tools to the LLM

* Place tools in a list (for example: `[add]`).
* Bind them to the model to create `LLMWithTools`.

Now the LLM is “tool-aware” and can call `add` automatically when needed.

---

### Expanding Tool Capabilities

* Add more tools such as:

  * `subtract`
  * `multiply`

Bind all tools together so the LLM can choose between them dynamically.

---

### Dynamic Function Execution with Mapping Dictionaries

To support flexible tool calls:

* Create a mapping dictionary:

  * Tool name (string) → function
* Build an input dictionary matching parameter names:

  * `{ "a": 1, "b": 2 }`
* Call the tool dynamically using:

  * `tool_map["add"].invoke(input_dict)`

This enables name-based function execution and scalable tool orchestration.

---

### Key Takeaways

* Manual tool calling is a core building block for AI agents.
* You learned how to:

  * Initialize a chat model for tool use
  * Define tools with decorators
  * Bind tools to an LLM
  * Add multiple tools (add, subtract, multiply)
  * Use mapping dictionaries for dynamic function calls
* LLMs can:

  * Identify the correct tool
  * Extract parameters
  * Execute functions
  * Return precise, context-aware results
* Chat history can be preserved to enable personalized, multi-turn interactions.

This approach transforms an LLM from a text generator into a practical, tool-powered agent.
