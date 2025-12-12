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
