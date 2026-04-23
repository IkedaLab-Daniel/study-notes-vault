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