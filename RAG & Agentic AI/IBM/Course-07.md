# Agentic AI with LangChain and LangGraph

> # Module 1: Introduction to LangGraph
## Course Overview: Agentic AI Development with LangChain & LangGraph

* The field is shifting from **passive AI** (responds to prompts) to **Agentic AI** — systems that can **reason, plan, and act autonomously**.
* Businesses are rapidly adopting Agentic AI to handle **complex, multi-step workflows**, driving strong demand for developers skilled in **LangChain** and **LangGraph**.

### What Agentic AI Enables

Agentic systems excel at:

* Autonomy and decision-making
* Tool integration
* Multi-step reasoning

Key application areas include:

* Autonomous customer support
* Financial and market analysis
* Healthcare and diagnostics
* Supply chain and logistics
* Legal and compliance
* E-commerce and retail
* Government and defense

### Who This Course Is For

Designed for:

* Software engineers
* Data scientists
* ML engineers
* AI architects
* Automation engineers

**Requirements:**

* Strong Python skills (you’ll build agents immediately)
* Familiarity with core AI concepts
* Prior exposure to LangChain is recommended

### What You’ll Learn

#### Foundations

* What Agentic AI is and how it differs from traditional generative AI
* Core components and architecture of **LangGraph**
* **LangGraph vs LangChain** — when and why to use each

#### LangGraph Basics

* LangGraph 101
* Build your first **stateful AI workflow**
* Learn graph-based agent design fundamentals through hands-on labs

#### Agent Architectures

You’ll explore three powerful agent patterns:

* **Reflection Agents**
* **Reflexion Agents**
* **ReAct Agents**

You’ll learn how to:

* Integrate external knowledge
* Reason before acting
* Build practical agents (including a **LinkedIn post optimization agent**)

#### From Single-Agent to Multi-Agent Systems

* Understand how agents **collaborate, communicate, and coordinate**
* Explore **Agentic RAG** as a foundation for multi-agent interactions

### How to Succeed in the Course

* Watch all videos
* Complete readings and labs
* Use cheat sheets
* Take practice quizzes
* Finish the graded assessment

This course prepares you to design **autonomous, self-improving, multi-agent systems** and build real-world Agentic AI applications using LangChain and LangGraph.

## Generative AI vs Agentic AI — Key Differences

* **Generative AI is reactive.**
  It waits for a user prompt, then generates content (text, images, code, audio) based on patterns learned during training. Once it produces the output, its job is done until the next prompt.

* **Generative AI = pattern generation.**
  It predicts what comes next using statistical relationships learned from massive datasets. Think chatbots, image generators, and code assistants. Humans stay in control: the AI suggests, the human reviews and refines.

* **Agentic AI is proactive.**
  It doesn’t just generate responses — it **pursues goals** through a continuous loop:

  1. Perceive the environment
  2. Decide on an action
  3. Execute the action
  4. Learn from the result
  5. Repeat — often with minimal human intervention

* **Generative AI stops at creation; Agentic AI continues into action.**

* **Both often rely on LLMs**, but they use them differently:

  * In generative AI, LLMs primarily generate content.
  * In agentic AI, LLMs act as a **reasoning engine**, powering planning and decision-making.

* Agentic systems use **chain-of-thought reasoning**, breaking complex problems into smaller steps (similar to how humans think through tasks).

### Practical contrast

* **Generative AI example:**
  A YouTuber uses AI to draft scripts, suggest thumbnails, or generate music — but a human guides every step.

* **Agentic AI example:**
  A personal shopping agent autonomously searches for products, tracks prices, completes checkout, and manages delivery — only asking the user when necessary.

### Core takeaway

* **Generative AI = create content on demand.**
* **Agentic AI = reason, plan, act, and adapt toward goals.**

The future lies in **hybrid systems** that combine both: generating ideas when needed and autonomously executing multi-step actions when appropriate — becoming intelligent collaborators rather than passive tools.

## Core Components of LangGraph

### What LangGraph Is

* LangGraph is an advanced framework in the LangChain ecosystem for building **stateful, multi-agent AI applications**.
* It is **low-level and flexible**, giving developers full control over workflows without heavy abstractions.

### Graph-Based Workflow Model

LangGraph represents agent workflows as graphs made of three core primitives:

* **Nodes** – Individual steps or functions that perform computation.
* **Edges** – Paths that define how execution flows between nodes.
* **State** – Shared memory that persists across nodes, maintaining context throughout the workflow.

### Key Capabilities

* **Looping and branching** – Agents can make dynamic decisions and change execution paths at runtime.
* **State persistence** – Context is preserved across long interactions.
* **Human-in-the-loop** – Allows manual intervention when needed.
* **Time travel** – Enables debugging by rewinding to earlier states.

### Why LangGraph Instead of Traditional Control Flow

Traditional constructs like `for`, `while`, and `if` are linear and limited for complex workflows.

LangGraph provides:

* **Explicit state management** – Context is continuously updated and shared.
* **Conditional transitions** – Runtime branching based on decisions.
* **Modularity** – Nodes can be developed and tested independently.
* **Enhanced observability** – Clear visibility into execution paths for debugging and monitoring.

### Ideal Use Cases

LangGraph excels in sophisticated agent systems that require:

* Dynamic decision-making
* Long-term memory
* Adaptive workflows
* Multi-step reasoning

Example: A customer support agent that can branch, loop, pause for human input, and resume — all while retaining full conversation history.

### Visualization

* LangGraph workflows can be visualized using **Mermaid diagrams**, making nodes, edges, and execution paths easy to understand and debug.

### Summary

* LangGraph models AI workflows as graphs with **nodes, edges, and shared state**.
* It supports **branching, looping, persistent memory, human-in-the-loop, and time-travel debugging**.
* It offers superior flexibility over traditional programming constructs for building complex, autonomous agents.
* Graph visualization helps maintain and reason about intricate workflows.

## LangChain vs LangGraph — Key Differences and When to Use Each

### LangChain: Chained LLM Workflows

* LangChain is a framework for building **LLM-powered applications using sequential chains of components**.
* It’s ideal when you know the order of steps in advance (for example: retrieve → summarize → answer).

**Core characteristics:**

* Uses **chains** (directed acyclic graphs) where execution moves forward step-by-step.
* Provides modular components such as:

  * Document loaders (fetch data)
  * Text splitters (chunk large documents)
  * Prompts (guide the LLM)
  * LLMs (generate outputs)
  * Memory (store limited conversational context)
* Different stages can use **different LLMs**.
* Best suited for:

  * Linear or mostly linear workflows
  * RAG pipelines
  * Summarization → Q&A pipelines
  * Applications where the flow is predictable

**State management:**

* Limited and mostly forward-passing.
* Memory components exist, but persistent, shared state is not central to the design.

---

### LangGraph: Stateful, Agentic Systems

* LangGraph is a specialized library within the LangChain ecosystem for building **stateful, multi-agent, non-linear workflows**.
* It models applications as **graphs**, not chains.

**Core primitives:**

* **Nodes** – individual actions (add task, complete task, summarize, etc.)
* **Edges** – transitions between nodes
* **State** – shared memory accessible and modifiable by all nodes

**Key capabilities:**

* Looping and revisiting steps
* Branching based on runtime conditions
* Persistent state across interactions
* Flexible control flow
* Supports interactive and adaptive behavior

Example: a task assistant where users can add tasks, complete tasks, or request summaries in any order, with all actions updating shared state.

**State management:**

* First-class feature.
* All nodes can read and write state, enabling long-lived, context-aware agents.

---

### Direct Comparison

**Primary focus**

* LangChain: chaining LLM operations into applications
* LangGraph: building stateful, multi-agent systems

**Structure**

* LangChain: chains (DAGs, mostly forward-only)
* LangGraph: graphs (supports loops and revisiting states)

**Components**

* LangChain: prompts, LLMs, memory, agents, chains
* LangGraph: nodes, edges, shared state

**State**

* LangChain: limited, mostly via memory components
* LangGraph: robust, central, persistent

**Best use cases**

* LangChain: sequential pipelines (retrieve → process → respond)
* LangGraph: complex, interactive agents requiring ongoing context and adaptive behavior

---

### Bottom Line

* Use **LangChain** when your workflow is mostly linear and well-defined.
* Use **LangGraph** when you need **agentic behavior**, shared state, looping, and dynamic decision-making.

Both are powerful, but they solve different problems:
LangChain excels at structured pipelines, while LangGraph shines in autonomous, stateful AI systems.


## Getting Started with LangGraph 101 — Building Your First Stateful Workflow

### What LangGraph Is

LangGraph is a framework for building **stateful, multi-agent workflows** using graphs instead of linear chains. It models applications as:

* **State** – a shared, evolving memory that holds inputs, intermediate values, and outputs
* **Nodes** – functions that read and/or modify state
* **Edges** – transitions that control how state flows between nodes

This structure enables **looping, conditional branching, and dynamic execution**, which are essential for agentic systems.

---

### Defining State

* State is commonly defined using `TypedDict`, but it can also be lists, nested objects, or message sequences.
* Example state might include:

  * `n` (an integer counter)
  * `letter` (a random character)

This typed state acts like a row in a table and travels through the graph, accumulating updates.

---

### Creating Nodes

* Nodes are Python functions that accept the current state and return an updated state.

Example patterns:

* **Update node**

  * Takes state
  * Modifies values (e.g., increments `n`, generates a random letter)
  * Returns the new state

* **Side-effect node**

  * Reads state (e.g., prints values)
  * Returns state unchanged

Some nodes transform data; others exist purely for logging or output.

---

### Building the Graph

1. **Create a StateGraph**

   * Initialize it with your state class.

2. **Add nodes**

   * Use `add_node(name, function)` to register logic.

3. **Connect nodes with edges**

   * Use `add_edge(source, destination)` to define execution flow.

4. **Add conditional edges**

   * Use `add_conditional_edges` to route execution dynamically based on state.
   * A condition function evaluates the state and determines the next node (for example, loop back or end).

Example logic:

* If `n >= 13` → end workflow
* Otherwise → loop back to the increment node

5. **Set the entry point**

   * Define which node runs first using `set_entry_point`.

6. **Compile the graph**

   * Call `compile()` to create a runnable application.

---

### Running the Workflow

* Invoke the compiled graph with an initial state, such as:

```text
n = 1
letter = ""
```

Execution flow:

1. State enters the first node.
2. Counter increments and a random letter is generated.
3. Values are printed.
4. A condition checks whether `n` has reached 13.
5. If not, the workflow loops.
6. When the condition is met, the graph transitions to the end node.

The final state is returned after completion.

---

### Key Concepts Recap

* **State**: Central memory holding all inputs, intermediate values, and outputs.
* **Nodes**: Functions that process or observe state.
* **Edges**: Define execution paths between nodes.
* **Conditional edges**: Enable dynamic routing and looping.
* **Entry point**: Starting node of the workflow.
* **Compile + invoke**: Turns the graph into a runnable app and executes it.

---

### Why This Matters

LangGraph lets you:

* Build workflows with **loops and branching**
* Maintain **persistent context**
* Model complex agent behavior
* Visualize execution paths
* Create dynamic, state-aware AI systems far beyond simple linear pipelines

This example counter demonstrates the core mechanics that power more advanced agentic applications.

## Module 1 Summary
- Generative AI is a reactive system that creates content like text or images based on prompts. Agentic AI, on the other hand, is proactive and uses prompts to pursue goals. LangGraph is an advanced framework designed for building stateful, multiagent applications. 
- Nodes are functions that do the actual computation. Edges define how the execution flows from one step to the next. State is a shared memory that remembers everything across nodes. 
- LangGraph's unique capabilities include looping and branching for making dynamic decisions, state persistence to maintain context over long interactions, human-in-the-loop functionality for timely human interventions, and time travel   to facilitate convenient debugging. 
- LangGraph offers state management, allowing the workflow to maintain and modify context across different nodes. It also offers conditional transitions, enabling the workflow to make decisions at runtime and branch accordingly.
- A LangGraph workflow can branch, loop, pause for human input, and resume execution, all while preserving full conversational memory.
- LangGraph graphs can be visualized using Mermaid diagrams with core primitives such as nodes and edges clearly represented.
- LangChain helps developers build LLM-powered applications using modular components like prompts, memory, and tools. LangGraph, on the other hand, extends LangChain's capabilities by enabling stateful, multiagent workflows
- State in LangGraph is a complex, evolving memory that contains all inputs, intermediate values, and outputs.
- Nodes are functions that process the current state. Some nodes modify the state, whereas others are used for side effects.
- Edges define how the execution flows between nodes, passing the updated state from one step to the next.
- Conditional edges allow the workflow to make dynamic decisions, routing the state to different nodes.
- Building a LangGraph application involves creating a StateGraph object, incorporating nodes, connecting them, setting an entry point, and then compiling the graph into a runnable application.
- Running a LangGraph workflow is done by invoking the compiled application with an initial state.
- Workflow visualization helps to understand the execution flow and how the state progresses through different nodes.

> # Module 2: Build Self-Improving Agents with LangGraph

## Types of AI Agents: From Simple Reflex to Learning Systems

AI agents are categorized by how intelligently they perceive, decide, and act within their environment. Here are the **five main types of AI agents**, ordered from simplest to most advanced:

---

### 1. Simple Reflex Agents — *React*

* Operate using **if–then condition–action rules**
* Respond only to **current perceptions**
* Have **no memory** or understanding of past states
* Example: a thermostat turning heat on/off based on temperature

**Pros:** fast, simple
**Cons:** fail in dynamic environments; repeat mistakes

---

### 2. Model-Based Reflex Agents — *Remember*

* Extend reflex agents with an **internal state (model of the world)**
* Track how the environment changes and how their actions affect it
* Can reason about parts of the world they can’t currently observe

Example: robotic vacuum remembering cleaned areas and obstacles

**Key upgrade:** memory + world model

---

### 3. Goal-Based Agents — *Aim*

* Make decisions based on **explicit goals**
* Use their internal model to **simulate future outcomes**
* Choose actions that help achieve the goal

Example: self-driving car choosing turns to reach a destination

**Key upgrade:** planning toward objectives (not just reacting)

---

### 4. Utility-Based Agents — *Evaluate*

* Go beyond goals by assigning **utility scores** (preference or “happiness”)
* Compare multiple outcomes and select the **best** one
* Optimize for factors like speed, safety, or energy efficiency

Example: delivery drone choosing the fastest and most energy-efficient route

**Key upgrade:** optimization via utility functions

---

### 5. Learning Agents — *Improve*

* Adapt behavior over time using **experience and feedback**
* Core components:

  * **Performance element:** chooses actions
  * **Critic:** evaluates outcomes (reward signal)
  * **Learning element:** updates strategy
  * **Problem generator:** explores new actions

Example: chess AI improving by analyzing thousands of games

**Key upgrade:** continuous learning from experience (often via reinforcement learning)

---

### Quick Comparison

* **Simple reflex:** reacts (no memory)
* **Model-based reflex:** remembers
* **Goal-based:** plans toward goals
* **Utility-based:** optimizes outcomes
* **Learning agent:** improves over time

---

### Beyond Single Agents

* Real systems often use **multi-agent architectures**, where multiple agents collaborate in a shared environment.
* Despite advances, **human-in-the-loop** remains essential for oversight, especially in complex or high-stakes applications.

---

### Bottom line:
Agentic AI progresses from reactive rule-following systems to adaptive learning systems capable of planning, optimization, and self-improvement—forming the foundation of modern autonomous AI workflows.

## The Art of AI Self-Improvement: Building Reflection Agents

### What Is a Reflection Agent?

A **reflection agent** improves its own outputs through an iterative feedback loop. It typically includes two LLM roles:

* **Generator** – Produces initial content.
* **Reflector** – Critiques and suggests improvements.

The process repeats for a fixed number of iterations or until a stopping condition is met.

---

### Types of Reflection-Based Agents

Reflection agents fall into three categories:

1. **Basic Reflection Agent** (focus of this lesson)
2. **Reflexion Agent**
3. **Language Agent Tree Search (LATS)**

Basic reflection agents rely on simple generate → critique → refine cycles.

---

### How the Reflection Loop Works

1. User provides a prompt.
2. The **generator** produces an initial response.
3. The **reflector** evaluates and critiques the response.
4. The generator revises the content using the critique.
5. Steps repeat until termination.

Example evolution:

* Initial suggestion: “Wear a fedora.”
* Reflection: Critiques outdated advice.
* Revised output: Focus on authenticity and personal style.

Each iteration improves quality through structured self-evaluation.

---

### Use Case: LinkedIn Post Optimization Agent

The system is designed with two phases:

* **Post-generation phase**
* **Reflection (AI review) phase**

The generator produces a draft post.
The reflector critiques tone, clarity, and strategy.
The generator refines the post.
The cycle continues until a final optimized version is produced.

---

### Implementing with LangChain

* Initialize an LLM (for example, IBM Granite).
* Create a **ChatPromptTemplate**:

  * `SystemMessage` defines the LLM’s role.
  * `MessagesPlaceholder` maintains conversational memory.
* Connect prompt → LLM using the pipe operator (`|`) to build:

  * `generate_chain`
  * `reflect_chain`

Prompt engineering ensures:

* Structured generation
* Structured critique
* Iterative improvement

---

### Implementing with LangGraph

LangGraph manages stateful iteration using **MessageGraph**, where state is a list of messages:

* `HumanMessage`
* `AIMessage`
* `SystemMessage`

Each iteration appends new messages to state.

#### Core Nodes

* **generate_node**

  * Takes current message state
  * Produces an `AIMessage`
  * Appends to state automatically

* **reflection_node**

  * Critiques the latest output
  * Returns critique wrapped as a `HumanMessage`
  * Feeds feedback back into generator

Using `HumanMessage` for critique ensures the generator interprets reflection as user feedback.

---

### Graph Construction

1. Add nodes: `generate`, `reflect`
2. Connect edges:

   * reflect → generate (loop)
3. Set entry point: `generate`
4. Add conditional routing:

   * If iteration count exceeds threshold → `END`
   * Otherwise → `reflect`
5. Compile workflow

---

### Execution Flow

1. Initial `HumanMessage` enters graph.
2. Generator produces draft (`AIMessage`).
3. Reflector critiques (`HumanMessage`).
4. Generator refines.
5. Loop continues until stop condition.
6. Final `AIMessage` returned.

State continuously accumulates messages, enabling memory across iterations.

---

### Key Takeaways

* Reflection agents improve outputs via **iterative self-critique**.
* Generator creates; reflector critiques.
* LangChain handles structured prompting.
* LangGraph manages stateful looping with `MessageGraph`.
* Nodes process state; edges control flow; conditional routing enables iteration.
* The result is higher-quality, self-refined AI output.

Reflection agents represent a foundational step toward more advanced self-improving agent architectures.

## Understanding Reflexion Agents

### What Makes Reflexion Different from Reflection?

**Reflexion agents** extend basic reflection agents.
While reflection agents iteratively *generate → critique → refine*, Reflexion agents go further by:

* Integrating **external tools** (like web search or APIs)
* Incorporating **real-time information**
* Producing **verifiable responses with citations and references**
* Continuously learning from past attempts, even after model training

They don’t just improve wording — they improve **factual accuracy, relevance, and justification**.

---

### Core Capabilities of Reflexion Agents

Reflexion agents are designed for **self-improvement over time**:

* **Iterative self-critique** – analyze what went wrong and adjust strategy
* **Tool integration** – pull in up-to-date information via search or APIs
* **Evidence-backed outputs** – include citations and references
* **Weakness detection** – identify gaps in prior responses and correct them
* **Structured reasoning** – separate response, critique, and tool queries clearly

This makes them ideal for tasks that require **current knowledge and transparency**.

---

### High-Level Reflexion Workflow

1. **User Query**

   * Example: *“I need more minerals in my diet.”*

2. **Responder (Generator LLM)**

   * Produces an initial answer.
   * Outputs a **structured object**, not plain text:

     * `response`
     * `critique`
     * `search_query`

3. **Tool Call (e.g., Web Search)**

   * Extracts `search_query`
   * Returns results (title, content, URL)
   * Appends tool output to a shared `response_list`

4. **Revisor (Reflection LLM)**

   * Consumes:

     * Original response
     * Self-critique
     * Tool results
   * Revises the answer
   * Adds **citations and references**
   * Outputs a new structured object:

     * `revised_response`
     * `references`
     * `critique`
     * `next_search_query`

5. **Repeat Loop**

   * Revisor output → tool → updated response list → revisor again
   * Continues for a fixed number of iterations or until stopping criteria

6. **Final Output**

   * A refined, evidence-backed response with references.

---

### Why Structured Outputs Matter

Instead of free-form text, Reflexion uses **schema-based outputs** (tables / data models) to clearly separate:

* Response
* Self-critique
* Tool queries
* References

This prevents confusion between:

* Model reasoning
* Tool results
* Final answers

It also makes downstream processing reliable and deterministic.

---

### Key Roles in Reflexion

* **Responder**

  * Generates the initial answer
  * Provides self-critique
  * Suggests tool queries

* **Tool**

  * Fetches external, real-time information

* **Revisor**

  * Refines the responder’s output
  * Integrates tool data
  * Adds citations
  * Produces improved responses

All messages (human input, AI outputs, tool results) are stored in a running **response list**, enabling learning across iterations.

---

### Key Takeaways

* Reflexion agents evolve beyond reflection by adding **tools, citations, and continuous learning**.
* They operate in an **iterative loop**: generate → critique → search → revise.
* They can **self-correct weaknesses**, integrate **real-time data**, and justify claims with **references**.
* Structured schema-based outputs enable clean coordination between generator, tools, and revisor.
* The system improves over multiple cycles, producing increasingly accurate and transparent answers.

In short: **Reflexion agents turn LLMs into self-improving, evidence-aware systems.**


## ReAct: Building Agents that Reason Before Acting

**ReAct = Reason + Act.**
It’s an agent pattern where an LLM doesn’t just “answer”—it **thinks step-by-step**, **calls tools**, reads the **tool outputs**, then **updates its plan** until it can give a final response.

The classic loop looks like:

* **Thought**: what I should do next (reasoning)
* **Action**: which tool to use
* **Action Input**: what to pass into the tool
* **Observation**: what the tool returned
* Repeat… until
* **Final Answer**

---

### Why ReAct is useful

ReAct is best when the question needs **multiple steps** or **external info**:

* Current weather → needs a weather/search tool
* “What should I wear?” → needs a recommendation tool + the weather result
* “Find X, summarize it, then compute Y” → needs tools + chaining

Without tools, the model is guessing. With ReAct, it **grounds** its answer in observations.

---

### What’s happening in the Tokyo example

User: *“What’s the weather in Tokyo and what should I wear?”*

1. LLM realizes it needs live weather → calls **search tool**
2. Tool returns: *22°C, sunny*
3. LLM uses that observation → calls **recommend_clothing**
4. Tool returns: *t-shirt, shorts, sunglasses*
5. LLM responds with a clean final answer

That’s the ReAct cycle in action.

---

###ReAct in LangGraph: the mental model

LangGraph makes this clean by splitting the workflow into **two main nodes**:

### 1) `agent` node (the “brain”)

* Sends current message history to the LLM
* LLM returns either:

  * a normal assistant answer (**no tool calls**) → finish
  * a tool call request (structured) → go to tools node

### 2) `tools` node (the “hands”)

* Reads the tool call name + args
* Executes the tool
* Wraps the result as a `ToolMessage`
* Appends it back into state
* Routes back to `agent`

### Conditional routing: `should_continue`

* If last AI message has tool calls → **continue → tools**
* Else → **end**

So the graph is basically:

`START → agent → (tools → agent)* → END`

---

### What state looks like

A common LangGraph ReAct state is just:

* `messages`: a growing list of:

  * `HumanMessage`
  * `AIMessage` (may contain tool_calls)
  * `ToolMessage` (tool results)

LangGraph’s `add_messages` (or equivalent) makes sure each node **appends** rather than overwrites.

## Summary Module 2
- Reflection agents iteratively improve AI outputs by critically analyzing their performance through a feedback loop 
- The generator produces content while the reflector provides critical feedback 
- Prompt Engineering with LangChain guides LLMs in content generation and structured reflection using dynamic ChatPromptTemplates and message placeholders 
- Agent state in LangGraph is defined using MessageGraph. It tracks conversation, accumulating messages and context across iterations 
- Graph Construction involves defining nodes, connecting them with edges, setting an entry point, and using router nodes for dynamic decision-making and iterative loops
- Reflexion agents build on reflection agents by iteratively improving responses using self-critiques, external tools, and citations 
- The reflection process involves a loop of generation, critique, and revision to enhance clarity, accuracy, and usefulness 
- Reflexion agents can identify and fix their own weaknesses, improving with each cycle by analyzing prior outputs 
- They can incorporate real-time data by calling external tools such as web search APIs, enhancing the relevance of responses 
- Structured schema-based output helps agents distinguish between different components such as response, critique, and tool query 
- The responder produces an object with fields such as query and response, which downstream components such as the revisor can build on 
- The revisor refines the response by revising it, integrating tool outputs, and adding references to support the claims 
- This entire process operates in an iterative cycle, with outputs and feedback passed through tools and stored in a response list across runs 
- A search tool such as Tavily can be configured and invoked to enhance AI responses with external data
- Prompt engineering and schema design guide the LLM to produce structured reflections and focused answers  
- The AnswerQuestion and Reflection schemas capture answers, flag missing or irrelevant details, and generate queries
- Tool outputs such as tool_calls and schema fields help extract structured insights from AI messages
- LangGraph chains responder and revisor nodes into an iterative feedback loop using prompt updates and evidence-based revisions
- A MessageGraph orchestrates the Reflexion agent, managing node routing, iteration limits, and control flow