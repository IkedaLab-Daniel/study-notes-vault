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

## Computing Log Likelihood and Performing Inference

To perform inference using Naive Bayes with log likelihoods, you simply **sum the Lambda values (log ratios)** for each word in the tweet.

Given a Lambda dictionary:

* Words like **I**, **am**, **because** → Lambda = 0 (neutral)
* **happy** → 2.2 (positive)
* **learning** → 1.1 (positive)

### Example Tweet

“I am happy because I am learning”

Compute log likelihood by summing Lambdas:

* I → 0
* am → 0
* happy → 2.2
* because → 0
* I → 0
* am → 0
* learning → 1.1

**Total log likelihood = 3.3**

Since:

* log(1) = 0,
* log likelihood **> 0 → positive**,
* log likelihood **< 0 → negative**,

the tweet is classified as **positive**.

Notice that the positive score comes entirely from **happy** and **learning**, while neutral words contribute nothing. This shows how strongly sentiment-bearing words influence classification.

### Recap

* Log likelihood = sum of Lambdas for all words in the tweet.
* Threshold for decision is **0**:

  * > 0 → positive
  * < 0 → negative
* Neutral words do not affect the score; sentiment-heavy words dominate.

## Training a Naive Bayes Classifier

Training a Naive Bayes classifier for sentiment analysis is different from logistic regression or deep learning—there is **no gradient descent**. Instead, the model is trained by *counting word frequencies* in labeled text.

### 1. Collect and Label Data

Gather a dataset of tweets and divide them into:

* **Positive tweets**
* **Negative tweets**

### 2. Preprocess the Tweets

Preprocessing is crucial and includes five steps:

1. Lowercase the text
2. Remove punctuation, URLs, and Twitter handles
3. Remove stop words
4. Apply stemming
5. Tokenize into individual words

Real-world text cleaning often takes substantial time.

### 3. Build Vocabulary and Count Frequencies

From the cleaned corpus:

* Count how many times each word appears in positive tweets and negative tweets.
* Also compute the total word count for each class.
  This forms a frequency table.

### 4. Compute Conditional Probabilities (With Laplacian Smoothing)

Use the formula:

$$
P(\text{word}\mid\text{class}) = \frac{\text{freq(word, class)} + 1}{N_{\text{class}} + V_{\text{class}}}
$$

Where:

- $N_{\text{class}}$ is total word count for that class
- $V_{\text{class}}$ is number of unique words in that class

This ensures **no probability is zero**.

### 5. Compute Lambda for Each Word

Lambda is the **log of the ratio** between positive and negative conditional probabilities:

$$
\lambda = \log \frac{P(\text{word}\mid\text{pos})}{P(\text{word}\mid\text{neg})}
$$

These values will be used later for inference.

### 6. Estimate the Log Prior

Count the number of positive vs. negative tweets:

$$
    ext{log prior} = \log \frac{\#\text{pos tweets}}{\#\text{neg tweets}}
$$

- In the assignment dataset (balanced), log prior = **0**.
- In real-world datasets, this term becomes important.

---

### Summary of the Full Training Pipeline

1. Collect and label tweets
2. Preprocess to clean and tokenize text
3. Count word frequencies for each class
4. Compute smoothed conditional probabilities
5. Calculate lambda (log probability ratios)
6. Compute log prior

## Applying and Evaluating the Naive Bayes Classifier

Once your Naive Bayes model is trained, the next step is to test it on **unseen tweets** and evaluate its performance.

### Predicting Sentiment on New Tweets

1. Take the new tweet (e.g., *“I passed the NLP interview”*).
2. **Preprocess** it: lowercase, remove punctuation, stem, and tokenize.
3. For each token:

   * If it exists in the **lambda table**, add its lambda value to the score.
   * If it's unseen (e.g., *interview*), treat it as **neutral** (lambda = 0).
4. Add the **log prior**.
5. Final decision:

   * Score **> 0** → positive
   * Score **< 0** → negative

In the example, the score is **0.48**, so the tweet is **positive**.

### Evaluating Performance Using the Validation Set

You will evaluate the model using:

* **X_val**: raw validation tweets
* **Y_val**: their true sentiment labels

#### Steps:

1. Compute the **score** for each tweet in X_val using the lambda table + log prior.
2. Convert each score into a prediction:

   * score > 0 → 1 (positive)
   * score ≤ 0 → 0 (negative)
3. Compare predictions with **Y_val**:

   * Match → 1
   * Mismatch → 0
4. Compute accuracy:

$$
    ext{accuracy} = \frac{\text{number of correct predictions}}{\text{total validation examples}}
$$

### Key Points

* Words not seen during training contribute **0** to the score.
* Accuracy is calculated exactly like in last week’s logistic regression exercises.
* Validation helps determine how well your Naive Bayes model generalizes.

## Other Applications of Naive Bayes

Naive Bayes is not limited to sentiment analysis — the same probability-based framework can be used for many classification tasks by comparing likelihood ratios between classes.

### How It Works

Naive Bayes estimates:

* The **prior** probability of each class
* The **likelihood** of seeing specific words given each class
  Then it uses the **ratio of these probabilities** to choose the most likely class.
  This approach generalizes to many scenarios.

### Applications

#### **1. Author Identification**

* Train on writings from two or more authors.
* Compute lambda values for each word.
* For a new text, calculate which author’s word distribution it aligns with.
* Example: distinguishing Shakespeare vs. Hemingway.

#### **2. Spam Filtering**

* Use sender information, subject line, and email content.
* Train on spam vs. non-spam examples.
* Classify new email based on likelihood ratios.

#### **3. Information Retrieval**

* Given a user query, compute the likelihood of each document given the query words.
* Rank documents by likelihood.
* Keep the top *m* results or only those above a threshold.

#### **4. Word Sense Disambiguation**

* When a word has multiple possible meanings (e.g., *bank* = riverbank vs. financial institution):

  * Compute likelihood of each meaning given the surrounding text.
  * Choose the meaning with the higher score.

### Key Insight

Bayes rule and its naïve approximation provide a simple yet powerful method for:

* Classification
* Ranking
* Disambiguation

Because Naive Bayes is easy to train, fast to compute, and interpretable, it remains widely used across NLP tasks.

## Assumptions Behind Naive Bayes

Naive Bayes is powerful but relies on strong assumptions that are often unrealistic in real-world language tasks. Understanding these helps explain why the model sometimes fails.

### 1. **Independence of Words**

* Naive Bayes assumes each word in a sentence is **independent** of the others.
* In reality, words often appear together and influence each other.

  * Example: “sunny” and “hot” frequently co-occur and relate to “beach” or “desert.”
* Because this independence assumption is false, the model may:

  * Underestimate or overestimate word probabilities
  * Produce incorrect predictions in context-heavy phrases
* Example:

  * Completing “It’s always cold and snowy in ____”
  * Naive Bayes may give equal probability to “spring, summer, fall, winter,” even though “winter” is clearly the best choice based on context.

### 2. **Balanced Validation and Training Sets**

* Naive Bayes relies heavily on the probability distribution of the training data.
* Most annotated datasets (including the course datasets) are **artificially balanced** (equal positive and negative tweets).
* Real-world tweet streams are **not** balanced:

  * Positive tweets are more common.
  * Negative tweets may be filtered, muted, or banned.
* If the model assumes a balanced distribution when reality is not balanced, it may become:

  * Overly optimistic
  * Overly pessimistic
  * Misaligned with real-world data patterns

### Key Takeaways

* Independence assumption is almost always violated, but Naive Bayes still performs reasonably well for many tasks.
* For accurate results in this module’s assignments, the training data must be roughly balanced.
* Later videos will explain how to analyze and handle sentences where Naive Bayes fails.