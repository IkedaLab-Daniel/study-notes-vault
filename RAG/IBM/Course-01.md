# Develop Generative AI Applications: Get Started

## Overview

* The course introduces **Generative AI Applications**, highlighting the rising industry demand for developers skilled in AI-driven systems.
* It is ideal for **AI developers, ML engineers, data scientists, AI researchers**, and related roles.
* **Python programming** is required; basic **AI and web development** knowledge is recommended.
* **Module 1** covers generative AI fundamentals, prompt engineering, and **LangChain**, with a hands-on lab on building prompt templates.
* **Module 2** explores LangChain's core concepts and advanced features, including another hands-on lab to integrate AI capabilities into applications.
* **Module 3** guides learners in building a **GenAI-powered web app** using **LangChain and Flask** and evaluating different language models.
* Learners are encouraged to follow all course materials: videos, readings, quizzes, labs, and the final graded assessment.

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
