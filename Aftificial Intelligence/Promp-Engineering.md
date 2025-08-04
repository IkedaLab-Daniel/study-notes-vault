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