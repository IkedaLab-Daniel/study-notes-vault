## Introduction

* **Growing Demand:** The rise of generative AI requires developers to build comprehensive solutions combining machine learning models, AI services, prompt engineering, and custom code.
* **Azure Platform:** Microsoft Azure offers multiple services, tools, and frameworks to build AI applications.
* **Key Concept:** Successful projects require evaluating available services and understanding foundational principles before development begins.

---

## What is AI?

* **Definition:** Software capabilities enabling applications to exhibit human-like behavior.
* **Modern Foundation:** Built on machine learning models that capture semantic relationships in vast amounts of data.
* **Core Functions:** Interpret various input formats, reason over data, and generate appropriate responses and predictions.

---

## Common AI Capabilities for Applications

| Capability | Description |
| --- | --- |
| **Generative AI and Agents** | • Based on Large Language Models (LLMs) to generate original responses to natural language.<br> <br>• Power interactive chat and content creation.<br> <br>• Foundation for **agentic AI**, combining LLMs with specific task instructions and automated tools. |
| **Natural Language Processing (NLP)** | • Statistical and semantic models to interpret text in documents, emails, and social media.<br><br>• Used for text analysis, term-frequency algorithms, text classification, sentiment analysis, and summarization. |
| **Computer Speech** | • Recognizes and synthesizes speech for natural voice interactions.<br><br>• Handles complex conversations, background noise, interruptions, and multiple accents/languages.<br><br>• Used for live transcription, translation, and text-to-speech. |
| **Computer Vision** | • Interprets and processes visual input from images, videos, and live camera streams.<br><br>• Enabled by multimodal generative models that can both process and generate visual content. |
| **Information Extraction** | • Combines generative AI, NLP, computer vision, and speech to extract key information from unstructured media.<br><br>• Example: Extracting dates, items, and totals from scanned receipts. |

## Microsoft Foundry on Azure

### Platform Overview

* **Microsoft Foundry:** The recommended platform for building AI solutions on Microsoft Azure, providing comprehensive project organization, resource management, and development capabilities.
* **Developer Interfaces:**
* **Microsoft Foundry Portal:** A web-based visual interface for developing and managing AI projects.
* **Microsoft Foundry SDK:** Enables programmatic development, resource management, and automation for CI/CD pipelines.

---

### Microsoft Foundry Projects

* **Structure:** Projects manage the data, code, and connections for an AI solution. They are hosted within a **Foundry resource**, which supplies the necessary compute, storage, and AI services. A single resource can support multiple projects (with one designated as the default).
* **Core Assets:**

| Asset | Description |
| --- | --- |
| **Models** | Deployments of Large Language Models (LLMs) from the Foundry Models catalog. Accessed via project-specific or Azure OpenAI endpoints. |
| **Agents** | Autonomous AI entities configured with an LLM, instructions, and tools to automate tasks. Developed and consumed through the Foundry Agent service. |
| **Tools** | Capabilities utilized by agents. Includes built-in functions (e.g., code interpreters), custom integrations via the **Model Context Protocol (MCP)**, and Microsoft Foundry Tools (speech, text analysis). |
| **Knowledge** | Data stores used by agents to ground and contextualize prompts. **Foundry IQ** can be used to create a centralized, MCP-based knowledge connection. |

---

### The Microsoft Foundry Portal Capabilities

Most AI solution development begins in the portal, where developers can:

* Find, compare, test, and deploy models.
* Create, configure, and test AI agents.
* Set up MCP connections to external tools and Foundry IQ knowledge sources.
* Manage user access and resource configurations.
* Retrieve endpoints and keys necessary for client applications.

> **Note on Architecture:** The platform is currently transitioning to a new project architecture. Older "classic" Foundry projects may still utilize a legacy hub-based system.

## Microsoft Foundry Tools

### Overview

While generative AI models and agents are the focus of modern AI development, **Foundry Tools** offer prebuilt, "off-the-shelf" APIs and models for common AI tasks. Integrating these out-of-the-box tools can help developers create more cost-effective and predictable solutions than relying solely on generative AI agents.

### Available Tools

| Tool | Description |
| --- | --- |
| **Azure Language** | Analyzes natural language text to perform tasks like entity extraction, sentiment analysis, and summarization. Also aids in building conversational language models and question-answering solutions. |
| **Azure Speech** | Provides APIs for text-to-speech and speech-to-text transformation, as well as real-time live speech capabilities for conversational apps. |
| **Azure Translator** | Utilizes advanced language models to seamlessly translate text across a large number of languages. |
| **Azure Document Intelligence** | Employs pre-built or custom models to extract data fields from complex, structured documents such as invoices, receipts, and forms. |
| **Azure Content Understanding** | Provides multi-modal analysis capabilities to extract structured data from forms, documents, images, videos, and audio streams. |

### Implementation and Usage

* **Connection:** Developers create client applications that connect to a tool-specific endpoint hosted in their Microsoft Foundry resource.
* **Authentication:** Access is secured by specifying the project authentication key or by utilizing token-based authentication.
* **Development:** Functionality is implemented using the specific APIs and SDKs provided for each tool.
* **Portal Access:** Select tools provide a visual user interface within the Foundry portal for straightforward configuration and testing.

> **Note on Naming:** Foundry Tools were previously known as *Azure AI Services* (and before that, *Azure Cognitive Services*). These legacy names may still appear in some APIs and SDKs. While some tools can still be provisioned outside of Foundry, new projects should utilize the tools provided directly within a Microsoft Foundry resource.