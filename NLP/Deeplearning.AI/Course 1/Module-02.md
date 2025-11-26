# Week 2: Probability and Bayes' Rule

## Probability & Bayes Rule — Overview

This lesson reviews basic probability and conditional probability and shows how **Bayes’ rule** follows from those definitions — all framed for NLP tasks like sentiment analysis.

* **Probabilities by counting:** estimate $P(A)$ as $\#(A)/N$ (count of events $A$ divided by total items $N$).

  * Example: if 13 out of 20 tweets are positive, $P(\text{positive}) = 13/20 = 0.65$.
  * Complement: $P(\text{negative}) = 1 - P(\text{positive})$ (assuming mutually exclusive labels).

* **Events & intersections:** define events (e.g., $A$ = “tweet is positive”, $B$ = “tweet contains ‘happy’”).

  * Probability of intersection: $P(A\cap B)=\dfrac{\#(A\cap B)}{N}$, where $N$ is the total number of tweets.
  * Example: if 3 tweets are both positive and contain “happy” out of 20, $P(\text{positive}\cap\text{happy}) = 3/20 = 0.15$.

* **Conditional probability:** $P(A\mid B)$ describes the probability of $A$ given $B$; conditional definitions lead directly to Bayes' rule.

* **Bayes’ rule:** derived from conditional probability identities; useful in NLP for tasks like sentiment classification and (later) autocorrect.

* **Why this matters for NLP:** counting-based probabilities and Bayes’ rule let you reason about how words (like “happy”) relate to labels (positive/negative) across a corpus — foundational for Naive Bayes and other probabilistic models.

## Conditional Probability & Deriving Bayes Rule

* **Conditional probabilities** narrow the sample space.
  If you only look at tweets that contain **“happy”**, you're evaluating probabilities *within* that subset, not the entire corpus.

* **Example (given “happy”):**

  $$
  P(\text{positive}\mid\text{happy}) = \frac{\#(\text{positive}\cap\text{happy})}{\#(\text{happy})}
  $$

  In the example, this evaluates to $3/4 = 0.75$.

* **Reverse conditional:**

  You can also compute

  $$
  P(\text{happy}\mid\text{positive}) = \frac{3}{13} \approx 0.231
  $$

  Same intersection, different denominator.

* **Conditional probability interpretation:**

  $P(B\mid A)$ means: “given we are inside set $A$, what fraction also belong to $B$?”

* **Venn diagram view:**
  Both conditional probabilities use the *same* intersection area.
  Only the denominators differ: size of set **A** vs size of set **B**.

* **Deriving Bayes' Rule:**

  From

  $$
  P(A\mid B) = \frac{P(A\cap B)}{P(B)}
  $$

  and

  $$
  P(B\mid A) = \frac{P(A\cap B)}{P(A)}
  $$

  set the numerators equal and rearrange to get the familiar form:

  $$
  P(A\mid B) = P(B\mid A)\cdot\frac{P(A)}{P(B)}
  $$

* **Interpretation:**

  Bayes' rule lets you compute $P(x\mid y)$ if you know:

  * $P(y\mid x)$
  * $P(x)$
  * $P(y)$

* **Why this matters for NLP:**
  You’ll use Bayes rule in **Naive Bayes**, a probabilistic classifier for tasks like sentiment analysis and later autocorrect.

  ## Naive Bayes for Sentiment Classification

* Naive Bayes is a **supervised machine learning method** similar to logistic regression but assumes all features (words) are **independent** — an unrealistic but useful assumption.

### Building the Model

* Start with two corpora: **positive tweets** and **negative tweets**.
* Build a **vocabulary** and count how many times each word appears in each corpus.
* Compute total word counts per class

  * Example: 13 words in positive corpus, 12 in negative corpus.

### Conditional Probabilities

* For each word, compute the class-conditional probabilities:

$$
P(\text{word}\mid\text{positive}) = \frac{\text{count in positive}}{\text{total positive words}}
$$

and

$$
P(\text{word}\mid\text{negative}) = \frac{\text{count in negative}}{\text{total negative words}}
$$
* Store these in a new table where each class’s probabilities sum to **1**.

### Understanding the Probabilities

* Words with **similar conditional probabilities** (e.g., “I”, “I'm”, “learning”) are *neutral* and do not affect sentiment.
* Words with **large differences** (e.g., “happy”, “sad”, “not”) are *powerful sentiment indicators*.
* If a word appears in one class only (e.g., “because”), the probability for the other class becomes **0**, causing problems.
  → This is solved later using **smoothing**.

### Classifying a New Tweet

Tweet: *“I’m happy today, I’m learning”*

Use the Naive Bayes inference rule (product of likelihood ratios):

$$
\prod_{\text{word in tweet}} \frac{P(\text{word}\mid\text{positive})}{P(\text{word}\mid\text{negative})}
$$

* Neutral words (I, am, I'm, learning) → ratios = 1
* Sentiment word (happy) → 0.14 / 0.10 = 1.4
* Word not in vocabulary (“today”) → ignored

Resulting product = **1.4**

* Because the score > 1, the tweet is more likely **positive**.

### What You’ve Accomplished

* Built conditional probability tables for each class.
* Used the Naive Bayes inference rule to compute sentiment.
* Saw how neutral and sentiment-heavy words contribute differently.

## Laplacian Smoothing in Naive Bayes

* When calculating conditional probabilities of words, some word–class combinations may never appear in the training corpus.
* This leads to **zero probabilities**, which can cause the entire sequence or classification probability to become zero.
* Laplacian smoothing solves this.

### Why Smoothing Is Needed

* Conditional probability formula (before smoothing):

$$
P(\text{word}\mid\text{class}) = \frac{\text{freq(word, class)}}{N_{\text{class}}}
$$

* If `freq = 0`, then the whole product for the sentence may become **0**, breaking Naive Bayes.

### Laplacian (Add-1) Smoothing

Modify the formula to avoid zeros:

$$
P(\text{word}\mid\text{class}) = \frac{\text{freq(word, class)} + 1}{N_{\text{class}} + V}
$$

Where:

- $+1$ ensures no probability becomes zero.
- $V$ is the number of **unique words in the vocabulary** (added to normalize correctly).

### Example

* Suppose there are **8 unique words** in the vocabulary.
* Positive class total words: 13
* Negative class total words: 12

For word **"I"**:

- Positive: $\dfrac{3 + 1}{13 + 8} = 0.19$

- Negative: $\dfrac{3 + 1}{12 + 8} = 0.20$

- All probabilities now sum to 1 per class.

- Previously unseen words (e.g., “because”) no longer have probability 0.

### Key Takeaways

* Laplacian smoothing prevents zero probabilities and keeps Naive Bayes functional.
* It ensures fair comparison between classes even when a word is missing in one class.

## Log Likelihoods in Naive Bayes

Log likelihoods are logarithms of the probabilities used in Naive Bayes, making calculations easier and avoiding numerical issues. Starting with the conditional probability table for each word (positive vs. negative), words can be categorized as **neutral**, **positive**, or **negative** by comparing their conditional probability ratios.

* **Ratio = P(word|positive) / P(word|negative)**

  * Ratio ≈ 1 → neutral
  * Ratio > 1 → positive
  * Ratio < 1 → negative

Examples:

* “happy”: 1.4 → positive
* “sad”, “not”: 0.6 → negative
* Words like “I”, “because”, “learning”: 1 → neutral

In Naive Bayes binary classification, you multiply all ratios of words appearing in a tweet:

* Product > 1 → positive
* Product < 1 → negative

This multiplication is called the **likelihood**. Combined with the **prior ratio** (positive tweets / negative tweets), you get the full Naive Bayes formula. In balanced datasets, this prior is 1, but in real projects with unbalanced data, it becomes important.

### Why Use Log Likelihoods

Multiplying many small probabilities (values < 1) can lead to **numerical underflow**—numbers too small for computers to store.
The solution: take the **logarithm** of the score.

Using logarithm properties:

* log(a × b × c) = log(a) + log(b) + log(c)

Thus, the Naive Bayes score becomes:

* **log score = log prior + sum of log ratios**

The log of a ratio is called **Lambda**:

* Λ(word) = log( P(word|positive) / P(word|negative) )

Examples:

* “I”: log(1) = 0 → neutral
* “am”: log(1) = 0 → neutral
* “happy”: log(2.2) → positive

To classify a tweet, sum all Lambdas:

* Sum > 0 → positive
* Sum < 0 → negative

### Key Points

* Ratios measure positivity/negativity of words.
* Lambda (log ratio) avoids numerical underflow.
* Log likelihoods convert products into sums, simplifying computation.
* Higher ratio (or Lambda) → more positive meaning.
* Lower ratio (or Lambda) → more negative meaning.