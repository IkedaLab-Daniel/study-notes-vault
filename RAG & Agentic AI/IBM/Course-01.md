# Develop Generative AI Applications: Get Started

## Overview

* The course introduces **Generative AI Applications**, highlighting the rising industry demand for developers skilled in AI-driven systems.
* It is ideal for **AI developers, ML engineers, data scientists, AI researchers**, and related roles.
* **Python programming** is required; basic **AI and web development** knowledge is recommended.
* **Module 1** covers generative AI fundamentals, prompt engineering, and **LangChain**, with a hands-on lab on building prompt templates.
* **Module 2** explores LangChain's core concepts and advanced features, including another hands-on lab to integrate AI capabilities into applications.
* **Module 3** guides learners in building a **GenAI-powered web app** using **LangChain and Flask** and evaluating different language models.
* Learners are encouraged to follow all course materials: videos, readings, quizzes, labs, and the final graded assessment.

> # Module 1

## Intro to Generative AI

* The video introduces **generative AI**, its evolution, and how it differs from **discriminative AI**.
* **Discriminative AI** classifies data by learning decision boundaries (e.g., spam vs. non-spam). It is suited for prediction and classification but cannot generate new content.
* **Generative AI** learns the underlying data distribution and can produce **new content** (text, images, audio, video, code, etc.) based on a **prompt**. It can perform text-to-text, text-to-image, image-to-video, and other transformations.
* Discriminative AI mimics analytical skills, while generative AI mimics **creative skills**.
* Generative AI is built using **deep learning** and relies on neural network models such as:

  * **GANs** (Generative Adversarial Networks)
  * **VAEs** (Variational Autoencoders)
  * **Transformers**
  * **Diffusion models**
* Generative AI has origins dating back to the **1950s**, with major advances in:

  * **1990s** – neural networks
  * **2010s** – deep learning and large datasets
  * **2014** – introduction of GANs (Ian Goodfellow)
* Growth of **foundation models** and **large language models (LLMs)** (e.g., GPT, PaLM, LLAMA) accelerated generative AI’s capabilities.
* Models for various domains include **Stable Diffusion**, **DALL-E**, **MidJourney**, **Copilot**, **AlphaCode**, **Synthesia**, etc.
* Generative AI has broad applications across industries and significant **economic potential**, including large projected productivity gains.
* Key takeaways:

  * Generative AI creates new content from learned data.
  * Creative capability comes from GANs, VAEs, transformers, and diffusion models.
  * Foundation models can be customized for specific use cases.
  * Generative AI tools are rapidly expanding across domains.

## What is Generative AI Models?

* Large language models (LLMs) like ChatGPT belong to a broader category called **foundation models**, a concept introduced by Stanford researchers.
* Traditional AI used many small, task-specific models, while foundation models act as **general-purpose models** that can transfer to many tasks.
* Foundation models are trained on massive amounts of **unstructured data** (terabytes) in an **unsupervised** way by predicting the next word in a sequence—making them a key part of **generative AI**.
* Although trained for text generation, foundation models can be **tuned** with small labeled datasets to perform specific NLP tasks (classification, NER, etc.).
* Even without labeled data, models can perform tasks via **prompting / prompt engineering**, where instructions guide the model to produce the desired output.
* **Advantages of foundation models:**

  * **High performance** due to exposure to huge datasets.
  * **Productivity gains** because they require far less labeled data for downstream tasks.
* **Disadvantages:**

  * **High compute cost**—expensive to train and expensive to run inference (often needing multiple GPUs).
  * **Trust issues** due to training on large, unvetted internet datasets that may introduce bias, toxic content, or unknown data sources.
* IBM is working on improving the **efficiency**, **trustworthiness**, and **reliability** of foundation models for enterprise use.
* Foundation models extend beyond language to **vision** (e.g., DALL·E 2), **code** (e.g., Copilot), **chemistry** (e.g., IBM’s Moleformer), and **climate science** (e.g., Earth science foundation models).
* IBM integrates foundation model innovations into products such as **Watson Assistant**, **Watson Discovery**, **Maximo Visual Inspection**, and Red Hat’s **Project Wisdom**.

## What is Natural Language Processing (NLP)?

* **Natural Language Processing (NLP)** is the field of enabling computers to understand and generate human language.
* Humans naturally comprehend unstructured speech; NLP converts this **unstructured text** into **structured data** that computers can process.
* Converting unstructured → structured is **NLU (Natural Language Understanding)**, and structured → unstructured is **NLG (Natural Language Generation)**.
* Key NLP use cases:

  * **Machine translation** (requires understanding context, not just individual words)
  * **Virtual assistants** (e.g., Siri, Alexa) and **chatbots**
  * **Sentiment analysis** (positive/negative, serious/sarcastic)
  * **Spam detection** (identifying suspicious patterns like urgency or bad grammar)
* NLP works through a *collection of tools*, not one single algorithm.
* Core NLP pipeline steps:

  * **Tokenization** – breaking text into smaller units (words/tokens)
  * **Stemming** – reducing words to their base form (running → run)
  * **Lemmatization** – finding the dictionary-based root form (better → good)
  * **Part-of-speech tagging** – identifying the grammatical role of each token (e.g., “make” as noun vs verb)
  * **Named Entity Recognition (NER)** – identifying entities (Arizona → U.S. state, Ralph → person)
* These tools help convert human language into structured data for use in AI applications.

## Introduction to In-Context Learning

* **In-context learning (ICL)** is a prompt-engineering method where the model learns a new task from examples included directly in the prompt.
* ICL requires **no additional training or fine-tuning**—the model adapts using only the provided examples at inference time.
* **Advantages of ICL:**

  * No need for fine-tuning on task-specific datasets
  * Saves time and compute resources
  * Improves performance using small example sets
* **Limitations of ICL:**

  * Context window limits how many examples can be provided
  * Complex tasks may still need traditional training or gradient updates
* **Prompts** are instructions or inputs given to an LLM to guide it toward a desired output.
* A prompt contains two core components:

  * **Instructions** – direct, clear commands
  * **Context** – relevant information supporting the task
* **Prompt engineering** is the practice of designing and refining prompts to get accurate, relevant, high-quality outputs from LLMs.
* Benefits of prompt engineering:

  * Boosts accuracy and effectiveness
  * Ensures responses match context and expectations
  * Reduces misunderstandings
  * Removes the need for continuous model fine-tuning
* **Example:** A simple prompt like “The wind is” can lead GPT-3.5 to generate a creative poetic continuation.
* **A well-structured prompt includes:**

  1. **Instructions** – what the LLM must do
  2. **Context** – background details
  3. **Input data** – the text or content to analyze
  4. **Output indicator** – where the model should place its answer
* Recap: ICL uses examples inside prompts; prompt engineering improves LLM usefulness; prompts have four essential elements.

## Introduction to Langchain

* **LangChain** is an open-source Python framework that simplifies building applications powered by Large Language Models (LLMs).
* It helps retrieve, extract, process, and generate information from large text sources (e.g., research papers, legal documents) by chaining steps together.

### Key Benefits

* **Modularity:** Components work like building blocks that can be reused to reduce development time.
* **Extensibility:** Developers can add features, integrate external tools, and adapt components with minimal code changes.
* **Decomposition:** Breaks complex problems into smaller steps, improving reasoning and response accuracy.
* **Vector Database Integration:** Enables fast semantic search and efficient retrieval from large datasets.

### Practical Uses

* **Summarization:** Breaks down complex documents such as legal papers or reports.
* **Data Extraction:** Pulls key statistics or facts from text.
* **Question & Answer Systems:** Provides context-aware, multi-turn responses for support or knowledge bases.
* **Automated Content Generation:** Drafts emails, documentation, or brainstorms ideas.

### Working with Other Data Types

* Although text-focused, LangChain can handle **images, audio, and video** by using external tools (e.g., speech-to-text).
* Embeddings from these data types can be stored in vector databases for semantic search.

### Key Takeaways

* LangChain streamlines LLM workflows.
* Offers modular, extensible, and decomposable components.
* Useful for summarization, extraction, Q&A systems, and content generation.
* Supports other data types through external models and vector embeddings.

## Advanced Methods of Prompt Engineering

### Advanced Prompting Techniques

* **Zero-shot prompting:**
  The LLM performs a task without prior examples.
  *Example:* Classifying a fact (“The Eiffel Tower is in Berlin”) as true or false.

* **One-shot prompting:**
  The LLM is given **one example** as a template before completing a similar task.
  *Example:* Showing one English→French translation, then asking for another.

* **Few-shot prompting:**
  The model receives **multiple examples** to generalize from.
  *Example:* Classifying emotions using three labeled statements, then inferring the emotion of a new one.

* **Chain-of-Thought (CoT) prompting:**
  Guides the model through **step-by-step reasoning**, helpful for multi-step problems.
  *Example:* Apple arithmetic problem broken into sequential steps to reach the correct answer.

* **Self-consistency:**
  The model generates **multiple independent answers**, then the consistent result is selected.
  *Example:* Age calculation problem solved in three different ways to confirm accuracy.

### Tools for Prompt Engineering

* Tools such as **OpenAI Playground**, **LangChain**, **Hugging Face Model Hub**, and **IBM AI Classroom** help:

  * Build, experiment, and deploy prompts
  * Test and adjust prompts in real-time
  * Access pre-trained models
  * Share and collaborate on prompts
  * Analyze results and optimize prompt performance

### LangChain for Prompt Engineering

* LangChain provides **prompt templates**, reusable structures for creating consistent prompts.
* Templates may include:

  * Instructions for the LLM
  * One-shot or few-shot examples
  * The final question or request
* Example: Filling placeholders in a joke template → “Tell me a *funny* joke about *chickens*.”

### Agents in Prompt Applications

* **Agents**, powered by LLMs and tools like LangChain, can perform complex tasks via prompts.
* Types of agents include:

  * Q&A agents (with citations)
  * Content creation & summarization agents
  * Analytic & business intelligence agents
  * Multilingual translation agents

### Key Takeaways

* Advanced prompting methods: **zero-shot, one-shot, few-shot, chain-of-thought, self-consistency**
* Tools enable easier development, testing, and optimization of prompts
* LangChain uses prompt templates for structured, scalable prompting
* Agents use prompts to perform sophisticated, real-world tasks

## LangChain LCEL Chaining Method

### What LCEL Is

* **LangChain Expression Language (LCEL)** is a modern method for building LangChain applications.
* Uses the **pipe (|) operator** to connect components, creating clean and readable chains.
* Replaces the older “LLM chain” approach with a more flexible, composable system.

---

### How LCEL Works

To build an LCEL chain, you:

1. **Define a prompt template** with variables in `{}`
2. **Create a PromptTemplate instance**
3. **Connect components** using the pipe operator
4. **Invoke the chain** with input values

LCEL chains are built from **runnables**, which act as modular building blocks such as:

* LLMs
* Retrievers
* Tools
* Custom functions

---

### Runnable Composition Primitives

* **RunnableSequence**

  * Executes components in order; each output becomes the next input
  * LCEL replaces this with the **pipe operator** for cleaner syntax

* **RunnableParallel**

  * Runs multiple components at the same time with the same input
  * Often created automatically when using a **dictionary** in LCEL

---

### Automatic Type Coercion

LCEL converts regular Python structures into runnable components automatically:

* **Functions → RunnableLambda**

  * Used to transform inputs
* **Dictionaries → RunnableParallel**

  * Each key becomes a parallel task
* Happens behind the scenes, reducing boilerplate

Example:
A dictionary with tasks `{summary, translation, sentiment}` becomes a parallel chain producing outputs for all three at once.

---

### Example Workflow

A simple LCEL chain might look like:

* A **RunnableLambda** formats the prompt
* The pipe operator sends the formatted prompt to the **LLM**
* Another pipe sends the result to **StrOutputParser**

This creates a clean, readable sequence:

```
input → formatting → LLM → output parsing
```

---

### When to Use LCEL

* Best for **simple to moderately complex orchestration**
* Supports:

  * Parallel execution
  * Async operations
  * Streaming
  * Automatic tracing

For more complex workflows or branching logic, **LangGraph** is recommended, with LCEL usable inside individual nodes.

---

### Key Takeaways

* LCEL chains use the **pipe operator** for clear, linear data flow.
* Prompt templates use **variables with curly braces**.
* **RunnableSequence** and **RunnableParallel** form the foundation, but LCEL provides simpler syntax.
* **Type coercion** automatically turns functions and dictionaries into runnable components.
* LCEL improves readability, composability, and maintainability of GenAI applications.

## Summary and Highlights: Foundations of Generative AI and Prompt Engineering
- In-context learning is a prompt engineering method where demonstrations of the task are provided to the model as part of the prompt.
- Prompts are inputs given to an LLM to guide it toward performing a specific task.
- Prompt engineering is a process where you design and refine the prompt questions, commands, or statements to get relevant and accurate responses.
- Advantages of prompt engineering include that it boosts the effectiveness and accuracy of LLMs, ensures relevant responses, facilitates user expectations, and eliminates the need for continual fine-tuning.
- A prompt consists of four key elements: the instructions, the context, the input data, and the output indicator.
- Advanced methods for prompt engineering include zero-shot prompts, few-shot prompts, chain-of-thought prompting, and self-consistency.
- Prompt engineering tools can facilitate interactions with LLMs.
- LangChain uses 'prompt templates,' which are predefined recipes for generating effective prompts for LLMs.
- An agent is a key component in prompt applications that can perform complex tasks across various domains using different prompts.
- LCEL pattern structures workflows use the pipe operator (|) for clear data flow.
- Prompts are defined using templates with variables in curly braces {}.
- Components can be linked using RunnableSequence for sequential execution.
- RunnableParallel allows multiple components to run concurrently with the same input.
- LCEL provides a more concise syntax by replacing RunnableSequence with the pipe operator.-  - Type coercion in LCEL automatically converts functions and dictionaries into compatible components.

> # Module 2
## LangChain: Core Concepts

### What is LangChain?

* **LangChain** is an open-source framework that simplifies building applications using **Large Language Models (LLMs)**.
* Provides a **structured interface** to integrate LLMs into use cases like **NLP**, **data retrieval**, and more.

---

### Core Components of LangChain

1. **Language Models (LLMs)**

   * Generate text output from text input.
   * Can complete tasks, summarize documents, or generate responses.
   * Examples: IBM WatsonX.AI, OpenAI, Google, Meta models.
   * Can be customized with parameters like **tokens** and **temperature**.

2. **Chat Models**

   * Specialized LLMs for **conversational tasks**.

   * Convert LLMs into a chat interface for dynamic dialogue.

   * Handle multiple **chat message types**:

     * **HumanMessage** – input from user
     * **AIMessage** – response from model
     * **SystemMessage** – instructions for model behavior
     * **FunctionMessage** – calls functions with parameters
     * **ToolMessage** – interacts with external tools

   * Each chat message has:

     * **Role** – who is speaking
     * **Content** – what is being said

3. **Prompt Templates**

   * Translate user input into **clear instructions** for the model.
   * Types of prompt templates:

     * **StringPromptTemplate** – single-string formatting
     * **ChatPromptTemplate** – handles lists of messages

       * Supports role-specific templates: AI, Human, System, and Tool messages
     * **ViewShotPromptTemplate** – provides examples (“shots”) for few-shot learning
   * **Example Selectors** help choose the most relevant examples:

     * Semantic Similarity
     * Max Marginal Relevance for diversity
     * N-Gram Overlap for textual similarity

4. **Output Parsers**

   * Convert LLM output into **structured data** for easier handling.
   * Supported formats: JSON, XML, CSV, Pandas DataFrames.
   * Example: **Comma Separated List Output Parser** converts model output into CSV format.

---

### Workflow Example

1. User input → Chat Prompt Template → LLM or Chat Model → Output Parser → Structured Output
2. Example selector optimizes which examples to include in few-shot prompts, improving model accuracy.

---

### Key Takeaways

* **LangChain** is a framework for integrating LLMs into applications efficiently.
* **Language Models** generate outputs, **Chat Models** handle dialogue.
* **Prompt Templates** guide model instructions and few-shot examples.
* **Example Selectors** optimize context for LLMs.
* **Output Parsers** convert unstructured outputs into usable formats.

This structured approach makes building advanced AI applications more **modular, flexible, and maintainable**.

## LangChain Chains and Agents for Building Applications

### 1. **LangChain Overview**

* **LangChain** is a platform with APIs that help developers build applications with **language processing capabilities**.
* It uses **documents, chains, and agents** to structure workflows and integrate LLMs into applications.

---

### 2. **Chains in LangChain**

* A **chain** is a **sequence of calls** where the output of one step becomes the input of the next.
* **Sequential chains** allow multiple steps to create a smooth information flow.

**Example: Three-Step Sequential Chain**

1. **Chain 1 – Select Dish**

   * Input: User-specified location (e.g., China)
   * Output: Famous dish (e.g., Peking Duck)
   * Implemented via a **prompt template** and **LLM chain**

2. **Chain 2 – Provide Recipe**

   * Input: Dish name from Chain 1
   * Output: Recipe for that dish

3. **Chain 3 – Estimate Cooking Time**

   * Input: Recipe from Chain 2
   * Output: Estimated cooking time

* All three chains are combined into a **single sequential chain**, enabling a unified process.
* **Verbose mode** allows tracking how each input transforms through the chain.

---

### 3. **Memory in LangChain**

* **Memory storage** preserves historical context across interactions.
* Chains can **read from memory** to enhance input and **write back outputs** for future use.
* Example: **ChatMessageHistory**

  * Stores **human messages** and **AI messages**
  * Adds AI message: `"hi"` and user message: `"What is the capital of France?"`
  * Maintains conversation continuity

---

### 4. **Agents in LangChain**

* **Agents** are dynamic systems where an LLM **decides and sequences actions**.
* LLMs generate instructions but **do not execute actions directly**; agents integrate with external **tools**.
* Tools can include: search engines, databases, websites, or custom APIs.

**Example: Pandas DataFrame Agent**

* Allows users to query and visualize data using natural language.
* Steps:

  1. Instantiate `create_pandas_dataframe_agent` with LLM and DataFrame
  2. Set `verbose=True` to view reasoning
  3. Invoke queries like `"How many rows in the DataFrame?"`
* The agent translates the query into Python code, executes it, and returns the answer (e.g., 139 rows).

---

### 5. **Key Takeaways**

* **Chains**: Sequence of LLM calls; output of one step feeds the next.
* **Memory**: Preserves historical data for context-aware interactions.
* **Agents**: Use LLM reasoning + external tools to autonomously perform tasks.
* LangChain allows **dynamic, context-aware applications** that combine LLMs, chains, memory, and agents for complex workflows.

This structure enables developers to **build robust AI applications** with modular and maintainable components.

## LangChain LCEL (LangChain Expression Language) Chaining Method

### 1. **Overview of LCEL**

* **LCEL** is a modern pattern in LangChain for building **flexible, composable chains**.
* It uses the **pipe (`|`) operator** to connect components, creating **readable and maintainable workflows**.
* LCEL improves over traditional sequential LLM chains by offering:

  * Better composability
  * Clearer visualization of data flow
  * Greater flexibility for complex chains

---

### 2. **Steps to Build an LCEL Chain**

1. **Define a template**

   * Use **variables and curly braces** for dynamic input.
2. **Create a prompt template instance**

   * Converts your template into a reusable component.
3. **Build a chain** using the **pipe operator**

   * Connects components sequentially or in parallel.
4. **Invoke the chain** with input values

---

### 3. **Runnable Components**

* **Runnables** are building blocks that connect LLMs, retrievers, tools, or functions.
* **Two main composition types**:

  1. **RunnableSequence** – runs components **sequentially**

     * Output of one component → input of next
  2. **RunnableParallel** – runs multiple components **concurrently** with the same input

---

### 4. **LCEL Syntax Shortcuts**

* **Pipe operator (`|`)** replaces RunnableSequence for a **cleaner sequential chain**.
* **Type coercion** automatically converts:

  * **Functions** → `RunnableLambda`
  * **Dictionaries** → `RunnableParallel`

**Example:**

```python
{
  "summary": llm_call,
  "translation": llm_call,
  "sentiment": llm_call
}
```

* This dictionary becomes a **RunnableParallel**, processing all three tasks simultaneously.
* Output: `{"summary": ..., "translation": ..., "sentiment": ...}`

---

### 5. **Building a Simple Chain**

* Use **RunnableLambda** to wrap a function like `format_prompt`.
* Pipe the formatted prompt to:

  1. LLM for processing
  2. Output parser (e.g., `StrOutputParser`)

**Flow Example:**

```
RunnableLambda(format_prompt) | LLM | StrOutputParser
```

---

### 6. **Best Practices & Strengths**

* **LCEL is ideal for:** simpler orchestration tasks
* For **complex workflows**, use **LangGraph** while leveraging LCEL within nodes
* **Key strengths**:

  * Parallel execution
  * Async support
  * Simplified streaming
  * Automatic tracing
* Promotes **readable, reusable, and maintainable pipelines**

---

### 7. **Key Takeaways**

* **LCEL pattern** structures workflows using the **pipe operator**.
* **Prompts** are defined using **templates with variables and curly braces**.
* Components can run **sequentially** (RunnableSequence) or **in parallel** (RunnableParallel).
* **Type coercion** automatically converts functions and dictionaries into runnable components, simplifying development.

This method enables developers to **create clear, composable chains for various AI applications** efficiently.

## Summary and Highlights: Introduction to LangChain in GenAI Applications
- LangChain is an open-source interface that simplifies the application development process using LLMs.
- The core components of LangChain are:
  - The language models that use text input to generate text output.
  - The chat models that understand questions or prompts and respond like a human.
  - The chat models that handle chat messages such as HumanMessage, AIMessage, SystemMessage, FunctionMessage, and Tool Message.
  - The prompt templates that translate a user’s question or messages into clear instructions.
  - The example selector that informs the model about the input context and guides the LLM to generate the desired output.
  - The output parsers that transform the output from an LLM into a suitable format.
- LangChain is a platform that embeds APIs for the development of applications.
- Chains are the sequence of calls in LangChain, and the output for one step becomes the input for the next step.
- Chains first define the template string for the prompt, then create a prompt template using the defined template, and then create an LLMChain object name.
- Memory storage is important for reading and writing historical data.
- Agents are dynamic systems where the language model determines the sequence of actions.
- Agents integrate with tools such as search engines, databases, and websites to fulfill user requests.

> # Module 3

## Summary: Choosing and Managing AI Models with a Multi-Model Approach

### 1. **AI Models as a Garden Analogy**

* AI models are compared to **vegetables in a garden**.
* Before using a model, you must understand its **requirements** (data, environment, risks), or it may fail.
* Ongoing **evaluation and optimization** are needed for models to thrive.
* Relying on only one model is risky—**diversity is essential**, just like you can’t survive on carrots alone.

---

### 2. **Multi-Model Approach**

* A **multi-model strategy** uses different models for different use cases.
* This allows you to:

  * Choose the **right model for the right problem**
  * Compare how models are designed and behave
* Key questions to ask about each model:

  * Who built it?
  * What data was it trained on?
  * What guardrails exist?
  * What risks and regulations apply?

---

### 3. **Starting with the Right Use Case and Prompt**

* Everything begins with a **prompt**.
* A good prompt clearly defines:

  * The use case
  * The user problem
  * What the AI is expected to do
  * Guardrails for acceptable outputs
* Writing a precise prompt is the **first step** in model selection.

---

### 4. **Model Research and Evaluation**

* After defining the prompt, research models based on:

  * Size
  * Performance
  * Cost
  * Risk
  * Deployment method
* Evaluate models **against the prompt**, not in isolation.

---

### 5. **Testing and Optimization Process**

* Start testing with a **large model** to meet the prompt requirements.
* Then try to **replicate results with smaller models**.
* Pass the same prompt through different models to compare outcomes.
* Select the model that best balances **performance and cost**.

---

### 6. **Ongoing Governance and Maintenance**

* Model selection is **not a one-time task**.
* Continuous responsibilities include:

  * Performance evaluation
  * Cost monitoring
  * Governance and compliance
  * Updating data and prompts
  * Testing new models as they become available
* Avoid long-term **model lock-in** as business and external conditions change.

---

### 7. **Key Factors in Model Selection**

* Beyond accuracy and performance, consider:

  * Reliability and speed
  * Model size
  * Deployment method
  * Transparency
  * Potential risks
* These factors guide both selection and implementation.

---

### 8. **Collaboration and Measurement**

* AI implementation should be **cross-functional**, not owned by a single department.
* Teams must be able to:

  * Measure performance benchmarks
  * Produce datasets explaining how results are calculated
* This enables informed decisions for future models and use cases.

---

### 9. **Final Takeaway**

* AI models require **continuous care**, not just initial setup.
* Through ongoing testing, governance, and optimization, models stay relevant and effective.
* As models evolve, your **AI strategy must evolve too**—keep growing instead of stagnating.

## Summary: Getting Started with Building Generative AI Applications

### 1. **Why Generative AI Matters for Developers**

* Gartner predicts **80% of enterprises will use GenAI by 2026**, creating pressure and opportunity for developers.
* Many developers have *used* AI tools but haven’t *built* AI-powered applications.
* Recent advancements and tooling have made GenAI **much more accessible** for developers.

---

### 2. **The Three Main Stages of the AI Developer Journey**

Developers typically move through three key phases:

1. **Ideation & Experimentation**
2. **Building the Application**
3. **Development, Deployment, and Operations (MLOps)**

---

### 3. **Ideation and Experimentation (Proof of Concept)**

* Start with a **clear, specialized use case**.
* Research and evaluate models from sources like **Hugging Face** and the open-source community.
* Compare models based on:

  * Model size
  * Performance
  * Cost
  * Latency
  * Benchmarks
* Key insights:

  * Self-hosted models are often cheaper than cloud APIs.
  * **Small Language Models (SLMs)** can be faster and more task-specific than large models.

---

### 4. **Prompting Techniques to Understand Model Behavior**

* **Zero-shot prompting**: Ask a question without examples.
* **Few-shot prompting**: Provide examples to guide behavior.
* **Chain-of-thought prompting**: Ask the model to explain its reasoning step by step.
* Early experimentation helps reveal **capabilities and limitations** of models.

---

### 5. **Building AI-Powered Applications**

* Models can be run **locally**, similar to databases or services.
* Local hosting improves **data privacy and security**.
* Two common ways to integrate your own data:

  * **RAG (Retrieval-Augmented Generation)**: Combine a pre-trained model with external data at query time.
  * **Fine-tuning**: Embed domain-specific data and behavior directly into the model.
* Each approach has trade-offs; many others also exist.

---

### 6. **Using Frameworks and Tools**

* Frameworks like **LangChain** simplify development.
* They help manage:

  * Prompt sequences
  * Multiple model calls
  * Complex workflows
* Enables popular GenAI use cases such as:

  * Chatbots
  * IT automation
  * Data management
* Encourages breaking problems into **smaller, manageable steps**.

---

### 7. **Operationalizing AI Applications (MLOps)**

* Deployment requires scalable infrastructure.
* Common technologies:

  * Containers
  * Kubernetes for orchestration and autoscaling
  * Runtime engines like **vLLM** for model serving
* Many organizations adopt a **hybrid approach**:

  * Multiple models for different tasks
  * Mix of on-premise and cloud infrastructure

---

### 8. **Monitoring and Continuous Improvement**

* Production AI systems require:

  * Benchmarking
  * Monitoring
  * Exception handling
* **MLOps** ensures smooth deployment, scaling, and maintenance—similar to DevOps but for models.

---

### 9. **Key Takeaway**

* Generative AI is not magic—it’s **another tool in a developer’s toolkit**.
* With the right process, tools, and mindset, developers can move from:

  * Ideation → Building → Deployment
* GenAI enables developers to create real-world impact through AI-powered applications.

## Summary and Highlights: Build a Generative AI Application with LangChain
- AI model selection requires a structured approach that includes careful initial evaluation, choosing the right model for each specific use case, and providing ongoing monitoring and refinement to ensure optimal performance.
- The process of selecting an AI model follows specific steps: Writing clear prompts that articulate your use case and requirements, researching available models based on size and performance metrics, evaluating models against your prompt, testing with larger models first before scaling down, and implementing continuous evaluation and governance.
- When choosing a model, you must consider key factors such as who built it, what data it was trained on, what guardrails exist, and what risks and regulations apply to ensure responsible AI implementation.
- Building AI applications begins with ideation and experimentation, progresses through implementation, and culminates in operationalization (MLOps), with each phase requiring unique approaches and tools.
- The multimodel approach enables you to select the most appropriate AI model for each task based on performance, accuracy, reliability, speed, size, deployment method, transparency, and potential risks.
- Python with Flask creates lightweight and flexible web applications that can scale from small projects to complex enterprise applications while maintaining simplicity and minimal design principles.
- Flask applications utilize URL routing with @app.route decorators, handle HTTP status codes systematically (including 200 OK, 400, 404, and 500 error codes), and support extensibility through a robust ecosystem of tools and libraries.
- Large-scale Flask applications benefit from features like extensibility and integration with other Python libraries, transparent documentation, custom implementations, strategic scaling considerations, and modular development approaches.
- Multiple AI models offer different advantages: Llama models provide enhanced context understanding, Granite models excel in business environments, and Mixtral utilizes a mixture of experts approach for efficient, specialized task handling.
- Modern Flask web applications can integrate with AI models through libraries like ibm-watsonx-ai and LangChain to implement structured JSON outputs, prompt templating, and format-specific tokens for different model types.
- Developers implement AI in Flask applications by creating properly configured virtual environments, installing necessary libraries, designing template-based prompts, utilizing model-specific formatting tokens, and adding comprehensive error handling.
- LangChain simplifies AI model management by providing consistent APIs across different models, structured output parsing, and support for multistep AI workflows in production applications.

## Recap

### 1. **Generative AI and Foundational Models**

* **Generative AI models**: Predict and generate new content (text, images, code, audio) from input data.
* **Foundational models**: A subset of generative AI, e.g., **Large Language Models (LLMs)**, which serve as the backbone for many AI applications.

---

### 2. **Prompts**

* **Definition**: Instructions or inputs that guide an LLM to perform a task.
* **Components**:

  * **Instructions**: Clear, specific commands for the AI.
  * **Context**: Background information to help the LLM understand the task.
* **In-Context Learning**: Providing examples in the prompt itself to teach the model a new task without training.

#### **Prompting Techniques**

1. **Zero-shot**: Task performed with no examples.
2. **One-shot**: Task performed with a single example.
3. **Few-shot**: Task performed using a small set of examples.
4. **Chain-of-Thought (CoT)**: Guides LLM reasoning step by step.
5. **Self-Consistency**: Generates multiple reasoning paths and selects the most consistent output.

---

### 3. **LangChain Framework**

* **Purpose**: Simplifies building applications using LLMs.
* **Key Components**:

  * Language model
  * Chat model
  * Chat messages
  * Prompt templates
  * Output parsers

#### **Chains**

* **Sequential chains**: Steps where the output of one becomes the input of the next.

#### **Agents**

* Dynamic systems where LLMs guide actions using chains.
* Can integrate tools like **databases or search engines** to fulfill user requests.

#### **LCEL (LangChain Expression Language)**

* Uses the **pipe (`|`) operator** to connect components.
* Provides **concise, readable, and flexible syntax** for building chains.
* Simplifies sequential and parallel execution of components.

---

### 4. **Notable AI Models Covered**

* **Llama3**: Strong reasoning, context understanding, handles nuanced problems.
* **Granite (IBM watsonx.ai)**: Optimized for enterprise, strong in business and technical domains.
* **Mixtro**: Mixture of experts; activates only the most relevant submodels for efficiency and adaptability.

---

### 5. **Next Steps**

* Apply the concepts to **real-world GenAI projects**.
* Explore additional courses in the professional certificate program (2–6 months to complete).
* Continue **testing, fine-tuning, and experimenting** with models to refine your AI engineering skills.