# IBM Introduction to AI

> Module 3: Business and Career Transformation Through AI

## AI Agents

### What Are AI Agents?

AI agents are software programs that:

* Interact with their environment
* Collect and process data
* Perform tasks autonomously to meet human-defined goals

They are capable of decision-making, problem-solving, adapting to new information, and learning from past experiences.

---

### How AI Agents Work (Phases)

1. **Perception** – Use sensors to gather environmental data
2. **Understanding** – Process and interpret data
3. **Decision-Making** – Determine the best actions using logic
4. **Action** – Use actuators to carry out decisions
5. **Learning** – Improve over time through machine learning

---

### Key Characteristics of AI Agents

* **Social Ability**: Communicate and collaborate with others
  *Example*: Healthcare chatbots for advice and scheduling
* **Autonomy**: Operate and make decisions independently
  *Example*: Self-driving cars
* **Reactiveness**: Respond quickly to environmental changes
  *Example*: Thermostats, predictive maintenance
* **Proactiveness**: Take initiative to achieve goals
  *Example*: Smart assistants taking actions based on patterns

---

### Multi-Agent Systems

* **Definition**: Systems where multiple AI agents work together
* **Capabilities**:

  * Distributed problem-solving
  * Cooperative decision-making
  * Emergent behavior through agent interaction

**Applications**:

* Online marketplaces – Negotiating agents for buyers/sellers
* Robotic coordination – Teamwork in logistics or rescue
* Traffic management – Communicating vehicles to reduce congestion

---

### Real-World Applications by Tech Giants

* **Google**:

  * YouTube: Content recommendation, moderation
  * Gmail: Smart replies, spam filtering
  * Maps: Real-time navigation and traffic updates
* **Amazon**:

  * Alexa: Voice recognition and smart home control
  * E-commerce: Product recommendation, inventory management
  * AWS: AI services like NLP and computer vision

---

### Conclusion

AI agents are transforming industries through automation, strategic decision-making, and enhanced customer interaction. Their characteristics—social ability, autonomy, reactiveness, and proactiveness—enable them to work independently or in multi-agent systems across a wide range of applications.

## AI Agents and the Shift to Compound AI Systems

### From Monolithic Models to Compound AI Systems

* Traditional models are limited to their training data and lack adaptability.
* Compound AI systems integrate models with tools, databases, and logic to solve real-world problems.
* Example: Planning a vacation involves accessing personal vacation data and generating personalized responses via database queries and LLMs.

### Compound AI System Characteristics

* **Modular Design**: Includes models, tools (e.g., verifiers, calculators), and databases.
* **Control Logic**: Defines the path from query to answer (e.g., always querying the vacation policy database).
* **RAG (Retrieval-Augmented Generation)**: A common compound AI pattern using external sources to enhance responses.

### Introduction to AI Agents

* AI agents are LLMs embedded within compound systems, controlling the system’s logic using reasoning.
* Agents use **slow thinking**: plan, break down tasks, observe results, and iterate.

### Core Capabilities of AI Agents

1. **Reasoning**: LLMs plan the solution step-by-step.
2. **Acting**: Use of external tools/APIs (e.g., search, calculators, code execution).
3. **Memory**: Stores internal reasoning logs and conversation history for personalization.

### ReAct Agent Pattern

* Combines **Reasoning** + **Acting**.
* Process:

  1. Receive a user query.
  2. Prompted to think before answering.
  3. Decide to call external tools if needed.
  4. Observe tool outputs and adjust plan accordingly.

### Concrete Example – Sunscreen Planning

* Query involves multiple steps:

  1. Retrieve vacation days from memory.
  2. Get forecasted sun hours for Florida.
  3. Retrieve sunscreen dosage guidelines.
  4. Calculate required sunscreen bottle count.
* Demonstrates multi-tool reasoning, memory use, and step-by-step planning.

### Choosing Between Programmatic vs Agentic Approaches

* **Programmatic systems** are more efficient for narrow, well-defined problems.
* **Agentic systems** are better for complex, varied tasks where manual path configuration is infeasible.
* Trade-off between efficiency (programmatic) and flexibility (agentic).

### Conclusion

* Compound AI systems are evolving toward agentic architectures.
* LLMs now control logic, enabling dynamic reasoning and tool use.
* Human-in-the-loop is still necessary, but autonomy in AI systems is increasing rapidly.

Here's a concise summary of the video **"The Rise of Generative AI for Business"**:

## Summary: The Rise of Generative AI for Business

This video explores how **Generative AI** is transforming businesses by enabling **efficiency, creativity, and innovation** across various domains.

### Key Takeaways:

* **Generative AI is revolutionary**, capable of producing original content—text, images, code, and more—evoking a sense of “magic.”
* It's not limited to digital content creation; it also accelerates discovery in **science, medicine, climate**, and other critical fields.

### Business Applications:

1. **Content Generation**:

   * Automates creation of marketing materials, product descriptions, and social media posts.
   * Example: *Persado* helped *Vanguard* improve sales conversions by 15%.

2. **Data Analysis**:

   * Processes large datasets to uncover patterns and generate insights.
   * Example: *Salesforce* integrates GenAI to enhance CRM strategies, lead identification, and customer behavior prediction.

3. **Customer Service**:

   * AI-powered chatbots handle repetitive tasks and provide real-time personalized assistance.
   * Example: *Sephora* uses GenAI to deliver tailored product recommendations.

4. **Product Development**:

   * Generates multiple design variations quickly for rapid prototyping.
   * Example: *Nike* uses GenAI for product innovation by analyzing trends and materials.

5. **Support for Startups**:

   * Helps reduce costs, automate routine tasks, and focus on strategic growth.
   * Example: *Stitch Fix* uses GenAI to interpret customer feedback and aid in personalized styling.

### Industry Adoption Stats (JP Morgan Survey):

* Highest adoption in **Marketing (28%)**, followed by **Legal (21%)**, **Media (20%)**, **Data Analytics (18%)**, and **Consumer Tech (13%)**.

### Conclusion:

Generative AI is reshaping how businesses operate by driving **personalization, automation, and efficiency**. As it continues to evolve, its practical and responsible application will be key to unlocking even greater value across industries.

## Summary: Retrieval-Augmented Generation (RAG) for Improving LLMs

Large Language Models (LLMs) can produce both impressively accurate and surprisingly incorrect answers. Two key challenges with LLMs are:

1. **Outdated knowledge**
2. **Lack of source attribution**

**Retrieval-Augmented Generation (RAG)** is a framework that addresses both issues by enhancing LLMs with an external content retrieval step.

### How RAG Works:

* Instead of generating a response based only on pre-trained data, the LLM first **retrieves relevant information** from a **content store** (e.g., the internet, private documents).
* The prompt now includes:

  1. An instruction to consider retrieved content
  2. The user's question
  3. The generation task
* This enables the model to generate **accurate, up-to-date, and source-grounded responses**.

### Benefits of RAG:

* **Current information** without retraining the model — just update the data store.
* **Factual grounding** using verifiable sources.
* **Reduces hallucination** and potential data leakage.
* Allows the model to respond with **“I don’t know”** when no reliable source is found.

### Limitation:

* The effectiveness of RAG depends on the **quality of the retriever**. Poor retrieval can result in missed or incorrect answers.
