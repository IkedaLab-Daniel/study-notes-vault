# Build AI Agents using MCP

> # Module 1: Introduction to MCP

## Model Context Protocol (MCP) for AI Agents

### Overview

* MCP (Model Context Protocol) is an **open-source standard** for connecting AI agents to external data sources
* Enables integration with:

  * Databases (relational or NoSQL)
  * APIs
  * Local files or code
* Designed to make agents more **capable, flexible, and data-aware**

### Core Components

* **MCP Host**

  * The main application (e.g., chat app, IDE assistant)
  * Contains one or more MCP clients
* **MCP Client**

  * Lives inside the host
  * Requests tools and communicates with MCP servers
* **MCP Server**

  * Provides tools and executes actions
  * Connects to external data sources (DBs, APIs, files)

### MCP Architecture

* MCP Host ↔ MCP Server communication happens through the **MCP Protocol**
* The protocol acts as a **transport layer**
* A single host can connect to **multiple MCP servers**
* Each server can expose different tools and capabilities

### How MCP Works (Workflow)

1. User sends a query (e.g., weather, customer data) to the MCP host
2. MCP client requests available tools from MCP server(s)
3. MCP server responds with available tools
4. MCP host sends:

   * User query
   * Available tools
     → to the LLM
5. LLM decides which tools to use
6. MCP client calls the appropriate MCP server(s)
7. MCP server executes actions:

   * Query database
   * Call API
   * Run local code
8. Results are returned to the MCP host
9. MCP host sends results back to the LLM
10. LLM generates the **final answer**

### Key Advantages

* Standardized way to connect **agents to real-world data**
* Supports **multiple tools and data sources**
* Decouples:

  * Agent logic (LLM)
  * Tool execution (MCP servers)
* Works across different applications and environments

### Use Cases

* Chat applications with real-time data access
* IDE code assistants accessing local files or codebases
* Business dashboards querying databases
* AI agents integrating multiple APIs

## Why MCP (Model Context Protocol) Matters

### Overview

* MCP is an **open protocol** that standardizes how AI agents connect to:

  * External data (databases, documents, APIs)
  * Tools and services (search, booking, calculations)
* Can be implemented in multiple languages (JavaScript, Python, Java, C#, etc.)
* Acts as a **universal integration layer** between LLMs and external systems

### Core Needs of AI Agents

* **Contextual Data**: Documents, database records, articles
* **Tool Capabilities**: Actions like API calls, searches, computations
* MCP enables agents to **discover and use these capabilities in a standardized way**

### Importance of Standardization

* **Extensibility**: Easily add new tools without breaking existing systems
* **Interoperability**: Works across platforms, vendors, and frameworks
* **Consistency**: Tools behave uniformly regardless of the model used
* **Reusability**: Build once, reuse across multiple projects
* **Rapid Development**: Avoid rebuilding integrations from scratch

### Key Benefits of MCP

#### Standardized Integration

* Eliminates need for custom integrations
* Simplifies connecting LLMs with tools and services

#### Simple Architecture

* Client-server, plug-and-play model
* Easy to deploy and scale

#### Interoperability

* Works across ecosystems (e.g., OpenAI, Azure, LangChain, LlamaIndex)

#### Enhanced Security

* Uses OAuth 2.0 and token-based authentication
* Supports TLS/SSL encryption for secure communication

#### Reduced AI Hallucinations

* Fetches **real-time, external data**
* Improves accuracy and reduces outdated or incorrect responses

#### Agentic Workflow Support

* Enables **multi-agent collaboration**
* Supports complex, multi-step automation tasks

#### Improved Data Relevance

* Retrieves up-to-date information from external sources
* Overcomes limitations of static LLM training data

### Real-World Use Cases

#### Enterprise Applications

* Connect to:

  * Databases
  * CRM systems
  * Ticketing platforms
* Automate workflows and generate reports
* Access live data (stocks, weather, news)

#### Agentic AI Systems

* Autonomous tool selection based on user goals
* Combines multiple data sources for better decision-making

#### DevOps, NetOps, SecOps

* **DevOps**:

  * CI/CD automation
  * Repository management (e.g., GitHub)
  * Infrastructure automation
* **NetOps**:

  * Network monitoring and configuration
  * Anomaly detection and issue resolution
* **SecOps**:

  * Threat detection and response
  * Incident orchestration
  * Vulnerability management

### Example: MCP in RAG Systems

* Instead of managing complex vector databases:

  * MCP server handles retrieval
  * Returns only relevant document chunks to the LLM
* Simplifies architecture and improves scalability

## MCP vs API (Model Context Protocol Explained)

### Overview

* LLMs need external data and tools to be useful in real-world applications
* Traditionally, this was done using **APIs**
* In 2024, Anthropic introduced **MCP (Model Context Protocol)** as a new open standard for AI systems
* MCP standardizes how AI applications connect to tools, data, and services

---

### MCP Explained

* MCP (Model Context Protocol) is like a **USB-C port for AI systems**
* It standardizes connections between:

  * AI applications (hosts)
  * LLMs (clients)
  * External systems (servers)

### MCP Architecture

* **MCP Host**

  * The main application (chat app, IDE, etc.)
* **MCP Client**

  * Runs inside the host
  * Opens a JSON-RPC 2.0 session using MCP protocol
* **MCP Server**

  * Exposes capabilities like tools, data, and prompts
  * Connects to:

    * Databases
    * APIs
    * File systems
    * Code repositories

---

### MCP Analogy (USB-C Model)

* Host = Laptop
* MCP Protocol = USB-C standard
* MCP Servers = Peripherals (monitor, storage, power, etc.)
* Key idea: **any compatible server works with any host using the same standard**

---

### MCP Capabilities (Primitives)

MCP servers expose three main types of capabilities:

#### 1. Tools

* Actions/functions the AI can execute
* Examples:

  * `get_weather`
  * `create_event`
* LLM calls tool → server executes function

#### 2. Resources

* Read-only data sources
* Examples:

  * Files
  * Database records
  * Knowledge base entries

#### 3. Prompts

* Predefined prompt templates for structured usage

> Not all MCP servers use all primitives, but tools are the most common.

---

### Key MCP Feature: Dynamic Discovery

* MCP servers expose a **machine-readable catalog**

  * `tools/list`
  * `resources/list`
  * `prompts/list`
* Agents can:

  * Discover capabilities at runtime
  * Use new tools without code redeployment
* This makes MCP highly **flexible and extensible**

---

### What APIs Are

* APIs (Application Programming Interfaces) allow systems to communicate
* Define rules for requesting and receiving data/services
* Commonly used to integrate external functionality without building from scratch

---

### REST APIs (Most Common Type)

* Communicate over HTTP
* Standard methods:

  * GET → retrieve data
  * POST → create data
  * PUT → update data
  * DELETE → remove data

#### Example

* `GET /books/123` → fetch book details
* `POST /loans` → borrow a book
* Responses typically in **JSON format**

---

### MCP vs API (Key Differences)

#### APIs

* Generic system-to-system communication
* Developer must manually:

  * Define endpoints
  * Handle integration logic
* Fixed structure per service

#### MCP

* Designed specifically for **AI agents and LLMs**
* Standardized discovery of tools and data
* Dynamic usage at runtime
* Works like a universal plug-and-play layer

---

### Key Insight

* APIs = manual integration layer for software systems
* MCP = standardized, AI-native layer for connecting LLMs to tools and data dynamically


## MCP App Demo

Think of Context7 as a **documentation brain plugged into your IDE**.

### 1. You (in Cursor / Windsurf)

You type:

> “How do I create a LangGraph React agent?”

---

### 2. MCP Client (inside IDE)

The IDE doesn’t answer directly.

It says:

> “Wait, I should check MCP servers first.”

---

### 3. MCP Server (Context7)

It exposes tools like:

* `ResolveLibraryID` → finds what library you mean
* `GetLibraryDocs` → fetches real documentation

So it does:

* detects “LangGraph”
* retrieves correct docs/snippets

---

### 4. LLM (inside IDE)

Now the model gets:

* your question
* * real docs from MCP

Then it responds with:

> a grounded, accurate code answer

---

## 🧩 Why this is powerful (this is the key idea)

Without MCP:

> LLM = “I think LangGraph works like this…” ❌ (hallucination risk)

With MCP:

> LLM = “Here’s what the official docs say…” ✅ (grounded output)

So MCP basically turns an LLM into a:

> **“tool-using system with live data access”**

---

## ⚔️ MCP vs APIs (this is the mental model upgrade)

You already saw APIs vs MCP — here’s the real difference:

### 🔧 API style (old way)

* You manually integrate each service
* Every tool has different format
* No standard discovery

> “I must code integration for each service”

---

### 🧠 MCP style (new way)

* Standard protocol
* AI can *discover tools automatically*
* Same interface for docs, DBs, APIs, files

> “AI figures out what tools exist and uses them”

---

## 🧑‍💻 Why Cursor/Windsurf matter here

These IDEs are basically becoming:

> **“AI operating systems for developers”**

With MCP they can:

* fetch docs (Context7)
* run tools
* query APIs
* even connect to your local files

So instead of:

> Googling → StackOverflow → copy-paste

You get:

> Ask → MCP fetches truth → AI writes working code

---

## 🧠 Big picture (connect everything you learned)

You just saw 4 layers of modern AI systems:

### 1. Single agent systems

(CrewAI / AG2 / BeeAI basics)
→ agents + tools + roles

### 2. Multi-agent systems

→ planner, writer, reviewer, coordinator

### 3. Tool frameworks

→ custom functions, APIs, ReAct, structured outputs

### 4. MCP layer (this video)

→ universal tool/data access layer for all agents