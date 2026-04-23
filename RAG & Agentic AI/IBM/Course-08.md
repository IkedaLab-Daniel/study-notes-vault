> # Module 1: Agentic Frameworks and LangGraph Design Patterns for Effective AI Systems

## Course Overview

* Introduction to building agentic AI applications using LangGraph, CrewAI, Autogen (AG2), and BeeAI
* Focus on the next wave of AI: systems that can reason, plan, and act independently
* Emphasis on creating multi-step workflows and integrating tools for autonomous decision-making

### What is Agentic AI

* AI systems that break down high-level goals into coordinated tasks
* Capable of reasoning, planning, and executing actions with minimal human input
* Widely adopted by businesses to improve efficiency, innovation, and automation

### Learning Objectives

* Understand core concepts of agentic AI
* Design and orchestrate multi-agent systems
* Learn key design patterns:

  * Sequential workflows
  * Routing workflows
  * Parallelization workflows
* Build and optimize AI agents using multiple frameworks

### Target Audience & Prerequisites

* Intended for:

  * Software engineers
  * Data scientists
  * Machine learning engineers
  * AI architects
  * Automation engineers
* Requirements:

  * Strong Python programming skills
  * Familiarity with AI concepts
  * Basic knowledge of LangChain (recommended)

### Frameworks Covered

* LangGraph
* CrewAI
* BeeAI
* Autogen (AG2)

### LangGraph Section

* Learn orchestration and evaluation workflows
* Apply design patterns through guided labs
* Build structured agent workflows

### CrewAI Section

* Build agent workflows from scratch
* Generate structured outputs using Pydantic
* Use YAML and CrewBase for configuration
* Extend functionality with custom tools
* Understand:

  * Agents with tools vs tasks with tools
* Practical project: meal and grocery planner

### BeeAI Section

* Learn core concepts and architecture
* Build basic agents using Bee Agent framework

### Autogen (AG2) Section

* Explore architecture and conversation patterns
* Build multi-agent systems
* Practical project: healthcare chatbot

### Learning Approach

* Video lessons and readings
* Cheat sheets for reference
* Practice quizzes for understanding
* Hands-on labs for real-world application
* Graded assessments to test knowledge

### Key Takeaway

* The course prepares learners to design, build, and deploy powerful multi-agent AI systems using modern frameworks.

## Understanding Agentic AI and Open Source Frameworks

* Introduction to agentic AI and open-source frameworks
* Covers core traits of agentic AI, benefits and challenges of multi-agent systems
* Compares popular frameworks and explains when to use each

### What is Agentic AI

* Autonomous systems that make decisions and take actions to achieve goals
* Key characteristics:

  * Multi-step reasoning (breaking complex tasks into steps)
  * Decision-making capabilities
  * Tool and API integration
  * Context retention (memory of past interactions)
  * Goal-oriented behavior

### Agentic AI vs Reactive Systems

* Reactive systems (e.g., calculators) only respond to inputs
* Agentic AI acts proactively like a research assistant:

  * Understands goals
  * Plans steps
  * Uses tools
  * Continues until task completion

### Why Use Frameworks

* Building from scratch is complex due to:

  * Message handling between agents
  * State synchronization
  * Custom coordination logic
  * Debugging and error handling challenges
* Frameworks provide:

  * Built-in communication protocols
  * Automatic state management
  * Predefined coordination patterns
  * Standardized error handling
  * Monitoring and debugging tools

### Multi-Agent Systems

* Multiple agents collaborate like a team with specialized roles

#### Benefits

* Specialization (agents focus on specific tasks)
* Parallel processing (simultaneous work)
* Fault tolerance (system remains stable)
* Scalability (add more agents as needed)
* Modularity (easy to update components)

#### Challenges

* Complex coordination
* State management across agents
* Debugging distributed systems

### Overview of Frameworks

#### CrewAI

* Simulates team-based collaboration
* Agents have defined roles (e.g., researcher, writer, editor)
* Strong in:

  * Task delegation
  * Structured outputs
* Best for:

  * Content creation
  * Collaborative workflows

#### LangGraph

* Uses graph-based workflows (nodes and edges)
* Provides fine-grained control over execution flow
* Strong in:

  * Workflow design
  * State management
  * Visual debugging
* Best for:

  * Multi-step processes
  * Document workflows
  * Decision trees

#### AutoGen (AG2)

* Enables conversational collaboration between agents and humans
* Supports:

  * Real-time interaction
  * Human-in-the-loop workflows
  * Code execution in conversations
* Best for:

  * Education
  * Collaborative coding
  * Technical support systems

#### Pydantic AI

* Focuses on structured, type-safe outputs
* Combines LLMs with schema validation
* Strong in:

  * Data consistency
  * API reliability
* Best for:

  * Enterprise systems
  * APIs and structured data
* Note: Not covered in depth in the course

#### BeeAI

* Flexible and scalable multi-agent framework
* Features:

  * Tool integration (OpenAI, Ollama, WatsonX, etc.)
  * Memory and state persistence
  * Logging and telemetry
  * Error handling
* Best for:

  * Enterprise-grade systems
  * Scalable production environments

### Framework Comparison & Use Cases

* **CrewAI & AutoGen**

  * Easy to learn and use
  * Ideal for rapid prototyping and collaboration

* **LangGraph & Pydantic AI**

  * More complex but offer greater control
  * Suitable for structured workflows and reliable outputs

* **BeeAI**

  * Built for production and enterprise scalability
  * Focus on robustness and control

### Real-World Applications

* CrewAI: content pipelines, automated reporting
* LangGraph: document workflows, customer service
* AutoGen: education, technical support
* Pydantic AI: API validation and data reliability
* BeeAI: enterprise automation systems

### Key Takeaways

* Agentic AI enables autonomous, goal-driven systems
* Multi-agent systems improve scalability, modularity, and efficiency
* Frameworks simplify development and reduce complexity
* Choosing the right framework depends on:

  * Use case
  * Level of control needed
  * System scale and complexity

## Building AI Agents with Open-Source Frameworks

### Overview

* Explains how agentic frameworks structure multi-agent workflows
* Covers agent creation, task assignment, and coordination
* Demonstrates workflow logic through code interpretation
* Compares use cases and limitations of different frameworks

### Agentic AI Fundamentals

* Autonomous systems that think, plan, and act
* Capable of:

  * Multi-step reasoning
  * Decision-making
  * Tool integration
* Frameworks provide infrastructure to simplify building these systems

### CrewAI Workflow

* Focus: role-based multi-agent collaboration
* Process:

  * Define agents with roles, goals, and backstories
  * Assign tasks with clear outputs
  * Combine into a “crew” for execution

#### Example Pattern: Evaluator-Optimizer

* Generator produces output
* Evaluator checks quality
* If rejected → feedback loop to generator
* If accepted → finalize output

#### Strengths

* Easy team simulation with clear roles
* Structured collaboration

#### Limitations

* Less flexible
* Debugging can be difficult

### LangGraph Workflow

* Uses Directed Acyclic Graphs (DAGs)
* Agents are nodes, workflows defined by edges

#### Key Concepts

* State management for passing data
* Nodes represent LLM operations
* Routers control flow based on conditions
* Graph defines full workflow execution

#### Strengths

* Fine-grained control
* Advanced memory and error handling
* Flexible workflow design

#### Limitations

* More complex and verbose code

#### Best Use Cases

* Complex workflows
* Multi-step automation (e.g., finance, healthcare systems)

### AutoGen Workflow

* Dialogue-driven multi-agent system
* Agents communicate through structured conversations

#### Example: Study Assistant

* Agents:

  * Student (input)
  * Concept analyzer
  * Study tips generator
* Group chat manager coordinates interaction
* Uses turn-based communication (round-robin)

#### Strengths

* Intuitive conversational design
* Supports human-in-the-loop workflows
* Built-in code execution

#### Best Use Cases

* Chatbots
* Virtual assistants
* Educational tools

### BeeAI Workflow

* Modular framework with strong tool integration

#### Example: Multi-Agent Report System

* Researcher → gathers history (Wikipedia)
* Weather agent → retrieves live data
* Synthesizer → combines outputs

#### Features

* Supports sequential and parallel execution
* Flexible agent design with tools
* Produces combined outputs from multiple agents

#### Strengths

* Scalable and modular
* Good for real-world integrations

#### Best Use Cases

* Travel assistants
* Data aggregation systems
* Educational bots

### Framework Comparison

* **CrewAI**: Role-based collaboration, simple but less flexible
* **LangGraph**: Highly customizable workflows, more complex
* **AutoGen**: Conversation-driven systems, easy prototyping
* **BeeAI**: Modular, tool-integrated, scalable workflows

### Key Takeaways

* Agentic frameworks simplify building intelligent systems
* Each framework supports different workflow patterns:

  * Reflection (CrewAI, LangGraph)
  * Delegation (CrewAI, BeeAI)
  * Conversation (AutoGen)
* Trade-offs exist in:

  * Flexibility
  * Code complexity
  * Debugging ease
* Choosing the right framework depends on system requirements and use case


## Essential Design Patterns for AI Systems

### Video Overview

* Introduces three core LLM workflow patterns:

  * Sequential (Prompt Chaining)
  * Routing
  * Parallelization
* Demonstrates each pattern using LangGraph
* Explains how state variables, nodes, and execution flow interact
* Shows example outputs from each workflow

### Sequential Pattern (Prompt Chaining)

* Simplest workflow pattern
* Output of one LLM becomes input to the next
* Breaks complex tasks into smaller, specialized steps

#### Example Use Case

* Writing a cover letter:

  * Agent 1: Generates resume summary
  * Agent 2: Creates cover letter using summary + job description

#### Implementation Flow

* Define state variables:

  * job_description
  * resume_summary
  * cover_letter
* Create nodes:

  * Resume summary generator
  * Cover letter generator
* Connect nodes sequentially in a graph
* Execute workflow to transform input into final output

#### Key Benefit

* Easy to implement and ideal for step-by-step task processing

### Routing Pattern

* Dynamically selects the appropriate agent based on input
* Uses a router agent to analyze the task

#### Example Use Case

* Decide whether to:

  * Summarize text
  * Translate text

#### Implementation Flow

* Define router state:

  * user_input
  * task_type
  * output
* Router node:

  * Analyzes input
  * Determines task (summarize or translate)
* Conditional routing:

  * Directs flow to the correct node
* Task nodes:

  * Summarization node
  * Translation node
* Final output stored in state

#### Key Benefit

* Enables intelligent decision-making within workflows

### Parallelization Pattern

* Runs multiple LLM tasks simultaneously
* Improves speed and efficiency

#### Example Use Case

* Translate text into multiple languages at once:

  * French
  * Spanish
  * Japanese

#### Implementation Flow

* Define state variables:

  * text (input)
  * language outputs (e.g., French, Spanish, Japanese)
  * combined_output
* Create parallel nodes:

  * One node per language
* Aggregator node:

  * Combines outputs into a final result
* Connect nodes:

  * All translation nodes run in parallel
  * Outputs flow into aggregator

#### Key Benefit

* Faster processing and higher throughput

### LangGraph Workflow Concepts

* **State Variables**: Store and pass data between nodes
* **Nodes**: Represent LLM operations or agents
* **Edges**: Define execution flow between nodes
* **Graphs**: Structure workflows for clear logic and control

### Key Takeaways

* **Sequential Pattern**: Best for step-by-step processing
* **Routing Pattern**: Best for dynamic decision-making
* **Parallelization Pattern**: Best for handling independent tasks simultaneously
* LangGraph enables structured implementation of these patterns using graphs, improving clarity, flexibility, and control over AI workflows

## Orchestrator Design Pattern

### Video Overview

* Introduces the **orchestrator pattern**, ideal for workflows where task complexity is unknown in advance.
* Focuses on **dynamic task assignment**, **parallel worker coordination**, and **merging outputs**.
* Shows how **state variables** and **worker states** manage shared context and task-specific details.

### Conceptual Analogy

* Imagine a **party planner on a cruise ship**:

  * Guests request multi-themed dinners daily.
  * Orchestrator (planner) analyzes requests and assigns tasks to specialized chefs.
  * Chefs work **in parallel**, and a synthesizer merges outputs into a **dinner guide**.
  * Example growth: Italian pasta + Mexican tacos → five international dishes → buffet plan.

* **AI Analogy**:

  * **Specialized agent workers** = chefs
  * **Central orchestrator** = head planner
  * **Synthesizer** = combines all outputs into a unified result

---

### Key Components

#### 1. State Variables

* **Shared state**: Contains global workflow data.

  * Example fields: `meals` (user input), `sections` (dish objects), `completed_menu` (merged outputs), `final_meal_guide`.
* **Worker state**: Each worker gets a copy of task-specific data.

  * Shares key-value pairs with global state for context.
  * Enables **parallel execution** without conflicts.

#### 2. Orchestrator Node

* Breaks down complex requests into structured tasks.
* Example workflow:

  1. Receives `meals` input: `"prepare Italian pasta, Mexican tacos, Indian curry…"`.
  2. Outputs **dish objects**: fields `name`, `ingredients`, `cuisine`.
  3. Populates the **sections list** in state.

#### 3. Assign Workers Node

* Determines how many workers are needed based on task complexity.
* Uses **LangGraph `send`** to distribute each dish object to worker state.
* Creates **parallel execution paths** dynamically.

#### 4. Worker Nodes

* Example: `chef_worker` node

  * Each worker receives a dish object (name, location, ingredients).
  * Generates detailed **cooking instructions** using a worker-specific LLM prompt.
  * Updates `completed_menu` (shared state) using `operator.add`.

#### 5. Synthesizer Node

* Combines outputs from all workers.
* Formats a **final meal guide** (`final_meal_guide`).
* Ensures parallel outputs merge into **a unified, coherent result**.

---

### Workflow Summary

1. **Planner Input** → Orchestrator breaks down meal requests.
2. **Orchestrator Output** → Sections list with structured dish objects.
3. **Assign Workers** → Sends tasks to multiple worker nodes in parallel.
4. **Workers** → Generate detailed outputs for their assigned dishes.
5. **Synthesizer** → Aggregates all completed menus into final guide.

---

### Benefits of Orchestrator Pattern

* **Dynamic task assignment**: adapts to unknown complexity.
* **Parallel execution**: multiple workers handle tasks simultaneously.
* **Separation of context and task-specific data**: state vs worker state.
* **Scalable and flexible workflows**: easily handle more tasks or agents.
* **Unified output**: synthesizer merges worker results for final execution.

---

### Key Takeaways

* The orchestrator pattern extends **static workflow patterns** (sequential, routing, parallelization) to **dynamic scenarios**.
* **Workers** focus on specialized tasks; orchestrator handles **coordination**.
* **State variables** provide context, **worker state** ensures task-specific details remain isolated but accessible.
* **Synthesizer** ensures all outputs combine into a **single coherent result**, making workflows scalable and robust.

## Evaluator-Optimizer Pattern for AI Systems

### Overview

* This pattern is used to **iteratively refine outputs** from an LLM until they meet predefined criteria.
* It combines **generator nodes** (create proposals/strategies) with **evaluator nodes** (assess quality/risk) in a **feedback loop**.
* State variables track all key data, enabling controlled iteration and context management.

### Conceptual Example: Multi-Agent Investment Advisor

1. **Investor Profile Input**

   * Example fields: risk tolerance, investment goals, capital, preferences.

2. **Target Risk Grading**

   * **LLM** computes a target risk grade (`ultra-conservative` → `high-risk`) from the investor profile.
   * Node: `risk_grading_node`
   * Output: `target_grade` in state variable.

3. **Generator Node (Initial Strategy)**

   * **Kathy Wood persona**: high-risk, innovation-driven strategies.
   * Produces an initial investment plan based on the investor profile.
   * Node: `generator_node_initial`

4. **Evaluator Node**

   * **Warren Buffett persona**: conservative, value-investing evaluator.
   * Assesses plan against investor profile and target risk grade.
   * Returns:

     * `grade` – assessed risk level
     * `feedback` – reasoning and improvement suggestions
     * Updates iteration counter.
   * Node: `evaluator_node`

5. **Generator Node (Refined Strategy)**

   * **Ray Dalio persona**: adjusts strategy using feedback from evaluator.
   * Refines the plan to address evaluator concerns while targeting desired returns.
   * Node: `generator_node_refined`

6. **Iteration / Reflection Loop**

   * Evaluate → Compare current grade vs. target grade:

     * **If match** → Accept plan, exit loop.
     * **If mismatch & iteration limit not reached** → Send plan + feedback back to generator for refinement.
     * **Iteration counter** ensures process does not loop indefinitely.

---

### State Variable Structure

* **Investor profile**: input details for the strategy.
* **Investment plan**: current proposal from generator nodes.
* **Target grade**: risk level target computed from profile.
* **Feedback**: evaluator comments for refinement.
* **Iteration counter**: tracks cycles through the reflection loop.

---

### Workflow Graph Nodes

1. **Grading Node**

   * Computes target risk score using `grade_prompt` and `grade_pipe`.
2. **Generator Node**

   * Combines Kathy Wood and Ray Dalio personas:

     * Kathy Wood for initial strategy.
     * Ray Dalio for refined strategy using feedback.
3. **Evaluator Node**

   * Warren Buffett-style assessment (`Buffett_evaluator_pipe`).
4. **Routing / Reflection Logic**

   * Conditional edges:

     * `accepted` → finish workflow.
     * `rejected` → loop back to generator with evaluator feedback.

---

### Key Principles

* **Iterative refinement**: LLM outputs are improved until target criteria are met.
* **State management**: Tracks investor profiles, plans, feedback, and iteration counts.
* **Multi-agent personas**: Different LLM personas simulate diverse investment styles and evaluation methods.
* **Reflection loop**: Enables structured feedback-based learning, akin to real-world advisor consultation.

---

### Benefits

* Produces **high-quality outputs** by continuous evaluation.
* Separates **generation** and **evaluation**, allowing modular persona designs.
* **Controlled iteration** prevents runaway loops while ensuring convergence.
* Scalable to **multi-agent, multi-step decision-making workflows**.

# > Module 2: CrewAI Fundamentals and Advanced Applications

## Design AI Agent Workflows with CrewAI

### Video Overview

* Explains how to design multi-agent workflows using CrewAI
* Covers core components: agents, tasks, tools, and flows
* Demonstrates sequential task execution
* Shows how to access results and evaluate performance using the Crew output object

### Core Components of CrewAI

#### Task

* Defines what needs to be accomplished
* Key elements:

  * **Description**: what the agent should do
  * **Expected output**: desired result format
* Acts like a “director” guiding the agent

#### Agent

* LLM-powered entity with structured prompts
* Defined by:

  * **Role**: expertise or identity
  * **Goal**: objective to achieve
  * **Backstory**: context shaping behavior
* Acts like an “actor” executing tasks

#### Tool

* External resources used by agents or tasks
* Examples:

  * APIs
  * Search engines
* Enhances capabilities and real-time data access

#### Flow

* Defines how tasks are executed and agents interact
* Types:

  * **Sequential**: tasks run one after another
  * **Hierarchical**: manager agent dynamically assigns tasks

---

### Sequential Workflow in CrewAI

* Tasks execute in a linear order
* Output of one task becomes input for the next
* Similar to a reflection workflow with feedback between steps

---

### Example: Content Creation Pipeline

#### Agents

* **Research Analyst**

  * Role: Senior Research Analyst
  * Goal: uncover insights
  * Uses tools (e.g., web search)

* **Content Strategist**

  * Role: Tech Content Strategist
  * Goal: create engaging content
  * Transforms research into readable output

#### Tasks

* **Research Task**

  * Input: topic (e.g., generative AI breakthroughs)
  * Output: detailed summary

* **Writing Task**

  * Input: research findings
  * Output: structured blog post

---

### Crew Object

* Central orchestrator combining:

  * Agents
  * Tasks
  * Tools
  * LLM
  * Flow type

#### Configuration

* Agents and tasks passed as lists
* Flow defined using `process.sequential`
* Execution starts with `.kickoff()` method

---

### Workflow Execution

1. Crew initializes
2. Research agent gathers and analyzes information
3. Output passed to writer agent
4. Writer creates final content
5. Workflow completes and returns results

---

### Crew Output Object

* Stores results and performance data

#### Fields

* **raw**: final combined output
* **tasks_output**: results from each task
* **token_usage**:

  * prompt tokens
  * completion tokens
  * total tokens (cost tracking)

#### Accessing Results

* Use `result.raw` for final output only
* Includes combined results from all agents

---

### Key Takeaways

* CrewAI enables structured multi-agent collaboration
* Agents simulate human roles using structured prompts
* Tasks define clear goals and outputs
* Tools extend agent capabilities
* Crew object orchestrates the full workflow
* Output object provides results, breakdowns, and usage metrics

## CrewAI with Structured Outputs, YAML, and CrewBase Classes

### Video Overview

* Builds a **multi-agent meal planning system** using CrewAI
* Uses **Pydantic** for structured outputs
* Introduces **YAML-based configuration** for agents and tasks
* Demonstrates **@CrewBase class** for loading and running workflows

---

### System Overview

* Multi-agent workflow with specialized roles:

  * Meal planning
  * Shopping organization
  * Budget analysis
  * Leftover management
  * Final summary generation
* Tasks run **sequentially**, passing outputs between agents
* Shared LLM powers all agents for consistent reasoning

---

### Structured Outputs with Pydantic

#### Purpose

* Ensures **clean, validated, reusable data**
* Enables reliable data exchange between agents

#### Key Models

* **GroceryItem**

  * Fields: name, quantity, estimated price, store category
  * Represents individual shopping items

* **MealPlan**

  * Fields: meal name, difficulty, servings, ingredients
  * Represents complete meal details

* **ShoppingCategory**

  * Fields: section name, items list, total cost
  * Groups grocery items by store section

* **GroceryShoppingPlan**

  * Combines:

    * Meal plans
    * Shopping categories
    * Total budget
    * Shopping tips
  * Provides full structured output for the workflow

---

### Agents and Tasks

#### MealPlanner Agent

* Role: recipe planner
* Uses web search tool for real-time recipes
* Outputs structured `MealPlan` data

#### ShoppingOrganizer Agent

* Converts meal plans into shopping lists
* Groups items by category
* Outputs `GroceryShoppingPlan`

#### BudgetAdvisor Agent

* Ensures plan stays within budget
* Suggests cost optimizations
* Outputs markdown guide

---

### YAML Configuration

#### Purpose

* Separates configuration from code
* Simplifies updates without modifying Python

#### Example Usage

* Define **leftover agent** and **task** in YAML
* Includes:

  * Role
  * Goal
  * Backstory
  * Task description

---

### CrewBase Class

#### Features

* Uses `@CrewBase` decorator to define crew container
* Automatically loads YAML-defined agents and tasks
* Provides decorators:

  * `@Agent`
  * `@Task`
  * `@Crew`

#### Usage

* Instantiate CrewBase class with shared LLM
* Access agents/tasks as methods
* Integrate YAML and Python components seamlessly

---

### Final Workflow

#### Summary Agent

* Combines outputs from all agents:

  * Meal planner
  * Shopping organizer
  * Budget advisor
  * Leftover manager
* Produces final **meal planning guide**

#### Execution

* Create crew object with:

  * All agents
  * All tasks
  * Sequential flow
* Run with `.kickoff()` and user input
* Generates:

  * Recipes
  * Shopping lists
  * Budget insights
  * Leftover strategies

---

### Output Formats

* `.json`: structured data (e.g., shopping lists)
* `.md`: readable guides (e.g., shopping guide)

---

### Key Takeaways

* CrewAI supports structured multi-agent workflows with clear roles and tasks
* Pydantic ensures consistent, validated data across agents
* YAML enables flexible configuration without code changes
* `@CrewBase` simplifies integration of YAML and Python components
* Sequential workflows allow smooth data flow between agents
* Final output is a comprehensive, automated meal planning guide

## Extending CrewAI with Custom Functions

### Video Overview

* Explains how to create and use **custom tools (functions)** in CrewAI
* Demonstrates assigning tools to **agents vs tasks**
* Highlights how custom tools improve flexibility, efficiency, and control

---

### Custom Tools in CrewAI

#### Purpose

* Extend agent capabilities beyond built-in tools
* Enable **domain-specific functionality**

#### Creating Custom Tools

* Use `@tool` decorator from `crewai.tools`
* Define function logic in Python
* Include a docstring to describe functionality

#### Examples

* **add_numbers tool**

  * Extracts numbers and returns their sum
* **multiply_numbers tool**

  * Extracts numbers and returns their product

---

### Assigning Tools to Agents

#### Agent Setup

* Role: Calculator
* Goal: perform arithmetic operations
* Backstory: interprets numeric instructions

#### Tool Assignment

* Tools passed via `tools` parameter in agent definition
* Agent decides which tool to use based on input

#### Example Flow

1. Input: “Add 7, 8, 9, and 10”
2. Agent extracts numbers
3. Chooses **add_numbers tool**
4. Tool computes result → `34`

---

### Agent-Centric Approach

#### Key Idea

* Tools are attached to the **agent**
* Agent selects the appropriate tool dynamically

#### Example: Q&A Bot (Daily Dish)

* Tools used:

  * **PDF Search Tool** (for FAQ document)
  * **SerperDevTool** (for real-time web search)

#### Workflow

* Agent analyzes query
* Chooses:

  * FAQ tool → for known questions
  * Web search → for unknown queries
* Generates final response

#### Benefits

* Flexible decision-making
* More autonomous agents

---

### Task-Centric Approach

#### Key Idea

* Tools are attached to **specific tasks**, not agents
* Agent follows predefined workflow

#### Setup

* Agent: Customer Service Specialist (no tools assigned)
* Tasks:

  1. **FAQ Search Task**

     * Uses PDF search tool
  2. **Response Drafting Task**

     * Formats answer

#### Workflow

1. Task 1 retrieves data from FAQ
2. Task 2 generates response
3. Final answer returned

#### Benefits

* Clear, step-by-step execution
* Better traceability and control

---

### Comparison: Agent-Centric vs Task-Centric

* **Agent-Centric**

  * Tools assigned to agent
  * Agent chooses tools dynamically
  * More flexible and autonomous

* **Task-Centric**

  * Tools assigned to tasks
  * Fixed workflow execution
  * More controlled and predictable

---

### Crew Execution

* Combine agent(s), task(s), and tools into a crew
* Run using `.kickoff()` with user input
* Agents process input, use tools, and return results

---

### Key Takeaways

* Custom tools enable **specialized functionality** in CrewAI
* `@tool` decorator simplifies tool creation and registration
* Tools can be assigned:

  * To **agents** (flexible, autonomous workflows)
  * To **tasks** (structured, controlled workflows)
* Choosing between approaches depends on:

  * Need for flexibility vs control
  * Complexity of the workflow

## Module 2: Summary

- CrewAI is designed for multi-agent collaboration, with agents assigned clear roles and tasks to simulate human-like teamwork
- Tools are standard components in AI workflows (for example, APIs and search engines) that can be used by either the Agent or the Task.
- The Crew object combines agents, tasks, the LLM, and tools into a coordinated workflow.
- CrewOutput captures the final result, task outputs, and token usage, giving a full snapshot of what was generated and its cost
- CrewAI lets you build multi-agent workflows by defining agents with specific roles, goals, and tasks, then grouping them in a Crew for sequential execution
- YAML allows you to define agents and tasks outside of Python, simplifying updates without touching code
- The @CrewBase decorator loads YAML-defined components as methods, making them easy to call and integrate into a Python script or notebook
- Custom functions enhance CrewAI by enabling domain-specific tools that improve flexibility and control
- An agent-centric workflow assigns tools directly to the agent, letting them choose the best tool based on the query
- A task-centric workflow attaches tools to individual tasks, guiding the agent step by step through a fixed process

# > Module 3: Alternative Agentic Frameworks: BeeAI and AG2 (AutoGen)

## BeeAI: Introduction and Code Components

### Overview

* Explains how to create and use **custom tools (functions)** in CrewAI
* Demonstrates assigning tools to **agents vs tasks**
* Highlights how custom tools improve flexibility, efficiency, and control

---

### Custom Tools in CrewAI

#### Purpose

* Extend agent capabilities beyond built-in tools
* Enable **domain-specific functionality**

#### Creating Custom Tools

* Use `@tool` decorator from `crewai.tools`
* Define function logic in Python
* Include a docstring to describe functionality

#### Examples

* **add_numbers tool**

  * Extracts numbers and returns their sum
* **multiply_numbers tool**

  * Extracts numbers and returns their product

---

### Assigning Tools to Agents

#### Agent Setup

* Role: Calculator
* Goal: perform arithmetic operations
* Backstory: interprets numeric instructions

#### Tool Assignment

* Tools passed via `tools` parameter in agent definition
* Agent decides which tool to use based on input

#### Example Flow

1. Input: “Add 7, 8, 9, and 10”
2. Agent extracts numbers
3. Chooses **add_numbers tool**
4. Tool computes result → `34`

---

### Agent-Centric Approach

#### Key Idea

* Tools are attached to the **agent**
* Agent selects the appropriate tool dynamically

#### Example: Q&A Bot (Daily Dish)

* Tools used:

  * **PDF Search Tool** (for FAQ document)
  * **SerperDevTool** (for real-time web search)

#### Workflow

* Agent analyzes query
* Chooses:

  * FAQ tool → for known questions
  * Web search → for unknown queries
* Generates final response

#### Benefits

* Flexible decision-making
* More autonomous agents

---

### Task-Centric Approach

#### Key Idea

* Tools are attached to **specific tasks**, not agents
* Agent follows predefined workflow

#### Setup

* Agent: Customer Service Specialist (no tools assigned)
* Tasks:

  1. **FAQ Search Task**

     * Uses PDF search tool
  2. **Response Drafting Task**

     * Formats answer

#### Workflow

1. Task 1 retrieves data from FAQ
2. Task 2 generates response
3. Final answer returned

#### Benefits

* Clear, step-by-step execution
* Better traceability and control

---

### Comparison: Agent-Centric vs Task-Centric

* **Agent-Centric**

  * Tools assigned to agent
  * Agent chooses tools dynamically
  * More flexible and autonomous

* **Task-Centric**

  * Tools assigned to tasks
  * Fixed workflow execution
  * More controlled and predictable

---

### Crew Execution

* Combine agent(s), task(s), and tools into a crew
* Run using `.kickoff()` with user input
* Agents process input, use tools, and return results

## Developing Agents and Multi-Agent Systems with BeeAI Framework

### Video Overview

* Demonstrates how to build agents using BeeAI
* Covers tools, reasoning, requirements, and security features
* Explains ReAct pattern and multi-agent collaboration

---

### RequirementAgent Fundamentals

* Core class for building intelligent agents in BeeAI
* Key features:

  * Persistent state
  * Tool usage
  * Behavior control via requirements

#### Setup

* Use `RequirementAgent` with:

  * LLM
  * `UnconstrainedMemory` for context
  * System instructions for role definition
* Run using async execution

---

### Adding Tools to Agents

* Tools extend agent capabilities
* Example: **WikipediaTool**

  * Enables access to external knowledge

#### Controlled Usage

* Use `ConditionalRequirement` to:

  * Limit tool usage (e.g., `max_invocations=1`)
  * Control execution behavior

---

### ThinkTool for Systematic Reasoning

* Enables agents to “think” before responding
* Supports internal reflection

#### Configuration

* Add `ThinkTool` to tools list
* Use `ConditionalRequirement` to:

  * Limit number of reasoning steps
  * Control execution flow

---

### Requirements System

* Provides fine-grained control over agent behavior

#### Key Features

* **ConditionalRequirement**

  * Controls tool usage frequency and order
* **AskPermissionRequirement**

  * Requires human approval before tool execution
* **ControlTrajectoryMiddleware**

  * Tracks execution flow for debugging
* **force_at_step**

  * Forces tool usage at a specific step
* **only_after**

  * Creates dependency between tools
* **consecutive_allowed**

  * Controls repeated tool usage

---

### ReAct Pattern in BeeAI

* Combines reasoning and action in cycles:

  * Think → Act → Think → Act → Final Answer

#### Implementation

* Use:

  * `ThinkTool`
  * `WikipediaTool`
  * Middleware for tracking
* Configure requirements:

  * `force_at_step=1` → start with thinking
  * `force_after=Tool` → think after each action
  * `maxInvocations` → limit cycles
  * `consecutive_allowed=false` → avoid repetition

#### Benefits

* Transparent reasoning
* Self-correction
* Improved decision-making

---

### Human-in-the-Loop Security

* Ensures safe and controlled agent behavior

#### AskPermissionRequirement

* Prompts user approval before executing actions
* Useful for:

  * Sensitive operations
  * Compliance and risk management

---

### Creating Custom Tools

* Enables domain-specific functionality

#### Steps

1. Define input schema using Pydantic (`BaseModel`)
2. Create tool class extending `Tool`
3. Implement `_run()` method with custom logic

#### Example

* **AddTool**

  * Inputs: numbers
  * Output: computed sum

---

### Multi-Agent Systems in BeeAI

#### Concept

* Multiple specialized agents collaborate on tasks

#### Key Component

* **HandoffTool**

  * Delegates tasks between agents

#### Workflow

1. Create multiple specialized agents
2. Wrap each with `HandoffTool`
3. Create a **Coordinator agent**:

   * Uses ThinkTool + Handoff tools
4. Route user query to coordinator
5. Coordinator delegates tasks to appropriate agents

---

### Key Takeaways

* BeeAI agents are **stateful, tool-driven, and highly controllable**
* RequirementAgent enables structured and flexible agent design
* Tools extend capabilities; requirements control behavior
* ThinkTool enables reasoning, forming the basis of ReAct pattern
* AskPermissionRequirement adds security via human approval
* Custom tools allow domain-specific functionality
* Multi-agent systems enable scalable, specialized collaboration

## Introduction to AG2 (Autogen) and Its Key Elements

### Overview of AG2

* AG2 (formerly Autogen) is an open-source framework for building **collaborative multi-agent systems**
* Uses multiple specialized agents (e.g., researcher, writer, reviewer) instead of a single LLM
* Provider-agnostic: supports models like OpenAI and Anthropic
* Designed for **real-world applications** with scalability, error handling, and flexibility

### Core Concepts

* **Conversable Agents**: Agents that send, receive, and respond to messages
* **Human-in-the-Loop**: Allows human oversight and intervention when needed
* **Multi-Agent Orchestration**: Coordinates multiple agents to solve complex tasks
* **Tools Integration**: Agents can use APIs, code execution, and external systems
* **Structured Outputs**: Ensures consistent and reusable responses

### Setting Up AG2

* Install framework and import core components
* Configure LLM using `LLMConfig`
* Apply shared or per-agent configurations for flexibility

### Agent Roles and Interaction

* Agents are defined using **system messages** that specify roles and behavior
* Example: Student (asks questions) and Tutor (provides explanations)
* Use `initiate_chat` to start interactions
* `max_turns` limits conversation length
* `summary_method` generates a final summarized output

### Benefits of Multi-Agent Systems

* Produces **higher-quality outputs** than single prompts
* Enables **role-based reasoning and collaboration**
* Provides **context-rich and structured responses**
* Scales well for complex problem-solving

### Specialized Agent Types

* **Assistant Agent**: Handles reasoning and code generation
* **UserProxy Agent**: Executes code and provides feedback
* Separation ensures **safe and efficient workflows**

### Code Execution Workflow

* Assistant generates code (e.g., plotting a sine wave)
* UserProxy executes it in a safe environment
* Output (e.g., image file) is generated and saved
* Includes safeguards like execution limits

### Human-in-the-Loop Modes

* **Always**: Requires input at every step
* **Never**: Fully autonomous execution
* **Terminate**: Requires input only at the end
* Useful for sensitive domains (finance, healthcare, law)

### Multi-Agent Orchestration Patterns

* **Two-Agent Chat**: Simple interaction between two agents
* **Group Chat**: Multiple agents collaborate in one conversation
* **Sequential Chat**: Step-by-step workflow
* **Nested Chat**: Reusable sub-conversations

### Group Chat System

* **Group Chat**: Defines participants and interaction rules
* **Group Chat Manager**: Controls conversation flow
* Speaker selection methods:

  * Auto (LLM decides)
  * Round Robin (fixed order)
  * Manual (human selects)
  * Random (random order)

### Example Use Case: Lesson Planning

* Agents:

  * Lesson Planner (creates content)
  * Reviewer (provides feedback)
  * Teacher (oversees and finalizes)
* Conversation ends when termination condition is met (e.g., “done”)

### Key Takeaways

* AG2 enables **structured, role-based AI collaboration**
* Supports **flexible orchestration patterns and human oversight**
* Improves **output quality through multi-agent interaction**
* Suitable for **complex, real-world AI systems**

## Extending AG2 with Tools and Structured Outputs

### Overview

* Focuses on enhancing AG2 agents with **tools** and **structured outputs**
* Enables agents to perform real-world tasks and produce **consistent, reliable responses**
* Emphasizes **production-ready practices** for secure and scalable systems

### Extending Agents with Tools

* Tools allow agents to go beyond text generation:

  * Code execution
  * API calls
  * Database access
  * File system interaction
* Supports automation, analysis, and visualization
* Example:

  * `math_asker` agent interprets request
  * `math_checker` agent executes `is_prime` function
* Separation of reasoning and execution improves **security and clarity**

### Structured Outputs with Pydantic

* Ensures consistent and predictable responses
* Solves issues with unstructured outputs (e.g., inconsistent formats)
* Benefits:

  * Data validation
  * Type safety
  * Reliable API integration
* Example:

  * Ticket summary model with fields:

    * Customer name
    * Issue type
    * Urgency
    * Recommended action
* Set as `response_format` in `llm_config` to enforce schema

### Importance of Structured Data

* Prevents malformed responses
* Creates **clear data contracts**
* Enables seamless integration with APIs, databases, and pipelines
* Improves system robustness and maintainability

### Production Best Practices

#### Security

* Avoid hardcoding API keys
* Use environment variables or secure credential storage

#### Reliability

* Use fallback models to maintain uptime
* Implement error handling and rate limiting

#### Model Configuration

* Adjust temperature:

  * `0.0` → deterministic, structured outputs
  * `0.7–1.0` → creative responses

### Agent Design Best Practices

* Define clear roles using strong system messages
* Keep agents **specialized and focused**
* Prevent infinite loops with `max_consecutive_auto_reply`
* Choose appropriate `human_input_mode` (automation vs oversight)

### Human-in-the-Loop Strategy

* Apply in high-risk or high-impact scenarios
* Define escalation criteria (e.g., financial thresholds)
* Provide context for human reviewers
* Log interventions for accountability

### Multi-Agent Orchestration Best Practices

* Define clear roles and task handoffs
* Use:

  * Group chat for collaboration
  * Structured workflows for control
* Set termination conditions to avoid infinite loops
* Monitor interactions for quality and intervention needs

### Tool Design Guidelines

* Each tool should have a **single, clear purpose**
* Implement strong error handling
* Validate inputs and outputs
* Clearly document tool usage and capabilities

### Structured Output Best Practices

* Use Pydantic models for validation and consistency
* Align schemas with downstream system requirements
* Include meaningful error messages
* Version schemas to maintain compatibility over time

### Key Takeaways

* Tools enable AG2 agents to perform **real-world actions and automation**
* Structured outputs ensure **consistency, reliability, and integration readiness**
* Production systems require **security, error handling, and fallback strategies**
* Clear agent roles, orchestration design, and human oversight improve system quality and maintainability


## Module 3 Summary
- BeeAI is a cutting-edge, open-source platform for building production-ready AI agents
- You can create an AI conversation in BeeAI by importing the necessary modules, initializing the chat model, defining the conversation messages, and running the model asynchronously with Python's async and await syntax
- Dynamic prompt templates enable the creation of reusable prompts with variable data
- BeeAI can generate structured outputs using Pydantic schemas
- Conversational memory is managed with the UnconstrainedMemory class
- The key benefits of using the BeeAI framework include modularity, structured outputs, async execution, multi-agent support, standards compliance, and observability
- Agents maintain a persistent state, use external tools, and follow behavioral requirements
- The RequirementAgent class is used to build intelligent, controllable agents
- The UnconstrainedMemory class provides a persistent context for an agent
- Additional capabilities can be added to agents by integrating tools
- ThinkTool enables agents to engage in explicit thinking processes before providing answers
- BeeAI's requirements system provides fine-grained control of agent behavior.
- The ReAct pattern supports reasoning and acting in cycles
- The AskPermissionRequirement class enables human-in-the-loop workflows for improved security
- Custom tools can be built for applications that require domain-specific capabilities
- Multi-agent systems can be created with BeeAI for specialized agent collaboration