# IBM: Generative AI: Prompt Engineering Basics

## What Is a Prompt?

A **prompt** is any input or series of instructions given to a generative AI model to produce a desired output. It guides the model’s behavior, helping it generate responses that are relevant, logical, creative, and human-like.

---

### 🔑 Key Concepts:

#### ✅ What Is a Prompt?

* An **instruction** you give to a generative model.
* Examples:

  * *“Write a small paragraph describing your favorite holiday destination.”*
  * *“Write HTML code to generate a dropdown selection of cities.”*

---

### 🧱 Elements of an Effective Prompt:

1. **Instruction**

   * Clearly defines what you want the model to do.
   * *Example*: “Write an essay in 600 words analyzing the effects of global warming on marine life.”

2. **Context**

   * Sets the background or scenario for the prompt.
   * *Example with context*:
     “In recent decades, global warming has undergone significant shifts… Write an essay analyzing the effects on marine life.”

3. **Input Data**

   * Provides supporting information for the model to refer to.
   * *Example*:
     “You have been provided with a dataset containing temperature records… Write an essay analyzing the effects on marine life in the Pacific Ocean.”

4. **Output Indicators**

   * Specifies the format, tone, style, length, etc.
   * *Example*:
     “Write an essay in 600 words…” → sets length and style expectations.

---

### 🧠 Why Prompt Design Matters:

* **Naive prompting** (e.g., “rich man’s story from small town”) → results in generic outputs.
* **Refined prompting** (e.g., “Write a story about a farmer who became a successful businessman in 10 years”) → leads to more specific and accurate results.

---

### 📸 Visual Example (Prompt for Image Generation):

* ❌ *“Sunset image between mountains”* → too vague.
* ✅ *“Generate an image depicting a calm sunset over a river valley that rests amidst mountains”* → clearer, more vivid.

## What Is Prompt Engineering?

**Prompt Engineering** is the structured process of crafting precise and effective prompts to guide generative AI models to produce accurate, relevant, and useful outputs.

---

### 🔑 What Is Prompt Engineering?

> Prompt engineering is the **design** of input instructions (prompts) to achieve **better and desired responses** from generative AI.

* It involves **critical thinking**, **creativity**, and **technical skill**.
* A poorly written prompt can lead to **incomplete**, **inaccurate**, or even **misleading** outputs.
* A well-engineered prompt guides the AI to perform tasks effectively and ethically.

---

### ⚓ Example Scenario: The Ship Captain

* ❌ Poor Prompt:
  `"Weather forecast of the Atlantic Ocean."`
  (Too broad → produces vague results.)

* ✅ Engineered Prompt:
  `"Provide weather forecasts for 28th Aug to 1st Sep 2023 for coordinates 20°N–30°N, 40°W–20°W in the Atlantic Ocean, including wind patterns, wave height, storm probability, etc."`
  (Specific location, time, and data needs.)

---

### 🧱 Prompt Engineering Process:

1. **Define the Goal**

   * Clearly outline what you want the model to generate.
   * *E.g.* “Summarize benefits and risks of AI in automobiles.”

2. **Craft Initial Prompt**

   * Translate the goal into a clear instruction.
   * *E.g.* “Write an article about pros and cons of AI in the automobile industry.”

3. **Test the Prompt**

   * Run the prompt and evaluate the model’s response.
   * Check for missing depth, context, or scope.

4. **Analyze the Response**

   * Identify gaps: Did it meet the objective? Was the tone right? What was missing?

5. **Refine the Prompt**

   * Add context, rephrase, or include specific domains.
   * *E.g.* Add instructions to cover ethics, cybersecurity, autonomous driving, etc.

6. **Iterate**

   * Repeat testing and refining until the response meets expectations.

---

### ✅ Final Refined Prompt Example:

> *“Write an article highlighting how artificial intelligence is reshaping the automobile industry. Focus on positive advancements such as autonomous driving and real-time traffic analysis. Also discuss technical challenges like decision-making algorithms and cybersecurity threats. Emphasize how these concerns impact vehicle safety. Include examples and promote critical thinking.”*

---

### 🌟 Importance of Prompt Engineering

* **Optimizes Model Efficiency**
  Get the best results *without retraining* the model.

* **Boosts Task-Specific Performance**
  Fine-tuned prompts produce *context-aware* and *nuanced* results.

* **Reveals Model Strengths & Limitations**
  Helps improve future designs and updates.

* **Improves AI Safety**
  Reduces the chance of *harmful or biased outputs* by controlling inputs precisely.

## Best Practices for Prompt Creation

### Clarity

* Use **simple and straightforward language** to convey instructions.
* Avoid **ambiguous or complex terminology** that may confuse the model or the user.
* Provide a **clear description of the task**.

**Example**
❌ *Discuss culinary processes that take place on foliaceous stipules...*
✅ *Explain the process of photosynthesis in plants, detailing the role of chlorophyll and how sunlight, carbon dioxide, and water contribute to this biological function.*

---

### Context

* Supply **background information** or situational details to guide the model’s response.
* Include **relevant names, events, dates, or explanations** to set the stage.

**Example**
❌ *Write what happened during the outbreak of the Revolutionary War in 1775.*
✅ *Describe the historical events leading to the American Revolutionary War, focusing on key incidents like the Boston Tea Party and Battle of Saratoga. Highlight tensions between the colonies and British government that led to war in 1775.*

---

### Precision

* Clearly **outline the structure or format** of the desired response.
* Use **examples** to guide the model toward your expectations.

**Example**
❌ *Talk about supply and demand and how it is affected in economics.*
✅ *Explain the concept of supply and demand in economics. Describe how increased demand can affect pricing using the smartphone market as an example. Also explain the effects of reduced supply using disruptions in oil production.*

---

### Role Play (Persona Pattern)

* Ask the model to **assume a specific role or identity**.
* Provide **contextual details** to enhance alignment with the assumed persona.

**Example**
❌ *Write a log entry describing strange flora and fauna on an alien planet.*
✅ *Pretend you are an astronaut who just landed on an uncharted alien planet. Write a log entry describing the flora, fauna, sky color, and sounds. Express your feelings of excitement, curiosity, and apprehension.*