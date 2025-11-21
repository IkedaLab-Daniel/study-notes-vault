# Natural Langugage Processing With Classification  and Vector Spaces
- DeepLearning.AI

## Intro to the NLP Specialization & Course 1 Overview

The instructors—Andrew, Younes, and Lukasz—introduce the NLP Specialization and outline its evolution from rule-based systems to modern deep learning methods. Advances in computing and attention mechanisms now allow efficient training of complex NLP models used in applications like chatbots, question answering, and machine translation.

The specialization contains four courses:

* **Course 1:** Classification and vector spaces. You’ll build sentiment classifiers using logistic regression and Naive Bayes, and learn vector representations for text. You’ll also build a simple machine translation system and use locality-sensitive hashing for efficient search.
* **Course 2:** Probabilistic models for predicting the likelihood of the next word.
* **Course 3:** Sequence models.
* **Course 4:** Attention models powering state-of-the-art NLP systems like chatbots and summarizers.

Within **Course 1**, the weekly breakdown is:

* **Week 1:** Text representation as vectors and logistic regression for sentiment.
* **Week 2:** Naive Bayes for sentiment classification.
* **Week 3:** Vector space models for tasks like retrieval and ranking.
* **Week 4:** Simple machine translation + locality-sensitive hashing for faster nearest-neighbor search.

The course prepares you to build foundational NLP systems and understand the core concepts behind modern applications.

## Week 1 Overview: Logistic Regression for Sentiment Analysis

This week introduces **logistic regression**, a foundational supervised learning method widely used in NLP due to its simplicity, fast training, and strong baseline performance.

The main task you'll work on is **sentiment analysis of tweets**:

* Positive tweets are labeled **1**
* Negative tweets are labeled **0**

### Key Steps in Supervised Learning

1. **Inputs (X)** and **labels (Y)** form your training data.
2. A **prediction function** uses parameters to map features to predicted labels **Ŷ**.
3. A **cost function** measures the difference between predictions and true labels.
4. Parameters are updated repeatedly to minimize this cost.

### Workflow for Logistic Regression in Sentiment Analysis

1. **Process raw tweets** to extract meaningful features.
2. **Train the logistic regression classifier**, minimizing the cost function.
3. **Use the trained model** to classify new tweets as positive or negative.

You now understand the overall process: extract features → train model → make predictions.
The next video will dive into how to extract features from text.

## Representing Text as Vectors Using a Vocabulary

To convert text into numerical form for machine learning, you first create a **vocabulary (V)**—a list of all unique words appearing across your dataset of tweets.

### Building the Vocabulary

* Collect all tweets.
* Scan every tweet and add each new word to the vocabulary.
* Each word appears **only once**, even if it occurs multiple times in the dataset.

### Encoding a Tweet as a Vector

For each word in the vocabulary:

* If the word appears in the tweet → assign **1**
* If it does not appear → assign **0**

This creates a vector with:

* Length = size of the vocabulary
* Mostly 0s and few 1s → a **sparse representation**

### Issues With Sparse Representations

* Each tweet’s vector must include every word in the vocabulary.
* Logistic regression must learn **V + 1 parameters**, where **V = vocabulary size**.
* As V grows large, training becomes slow and prediction becomes inefficient.

The next video addresses the problems caused by this approach and how to handle them.

## Generating Word Counts for Logistic Regression Features

To improve feature extraction for logistic regression, you can track how often each word appears in **positive** and **negative** tweets. These word–class counts will later help build stronger features for sentiment classification.

### Setup

* You have a corpus of tweets.
* A vocabulary of **unique words** is created from the entire corpus.
* Tweets are divided into two classes:

  * **Positive**
  * **Negative**

### Counting Word Frequencies by Class

For each word in the vocabulary:

* **Positive frequency** = number of times the word appears across all positive tweets.
* **Negative frequency** = number of times the word appears across all negative tweets.

Example:

* Word **"happy"** appears once in each of two positive tweets → positive frequency = **2**
* Word **"am"** appears three times across negative tweets → negative frequency = **3**

These counts form a table (or matrix) mapping every **word–class pair** to its frequency.

### Frequency Dictionary

In code, this becomes a dictionary:

```
(word, class) → frequency
```

This allows quick lookup of how often any word appeared in each sentiment class.

You’ve now built the frequency dictionary—next, you'll learn how to use it to represent a tweet for classification.

## Encoding a Tweet as a 3-Dimensional Feature Vector

Previously, tweets were encoded as high-dimensional vectors (dimension = vocabulary size **V**). Now you learn a more efficient representation using **only 3 features**, allowing logistic regression to train and predict much faster.

### Using the Frequency Dictionary

You created a dictionary mapping:

```
(word, class) → frequency
```

This tells how many times each word appears in **positive** and **negative** tweets.

### The 3 Features

For any tweet *m*, you compute:

1. **Bias term** — always **1**
2. **Sum of positive frequencies** — add the positive-class frequency for every unique word in the tweet
3. **Sum of negative frequencies** — add the negative-class frequency for every unique word in the tweet

### Example

Given a sample tweet:

* Identify all words appearing in it.
* Add up their **positive frequencies** → result = **8**
* Add up their **negative frequencies** → result = **11**

So the tweet’s final vector is:

```
[1, 8, 11]
```

This 3-value representation is far more efficient than a full vocabulary-sized vector and retains useful sentiment information.

Next, you’ll learn how to **pre-process tweets** so that the vocabulary is built from clean, normalized text.

## Preprocessing Text: Stop Words, Punctuation, Stemming, and More

This lesson introduces two key preprocessing concepts used before feeding text into a logistic regression classifier: **stop words** and **stemming**. The goal is to clean and normalize tweets so features become more meaningful and the vocabulary becomes smaller.

### 1. Removing Stop Words and Punctuation

* **Stop words** are common words that add little meaning (e.g., *and, are, a, at*).
* Compare each tweet against:

  * A stop-words list
  * A punctuation list
* Remove any word or character found in these lists.
* Removing them preserves the sentiment and simplifies the text.

Example result: after removing stop words and punctuation, the tweet keeps only the meaningful words.

### 2. Removing Handles and URLs

Tweets often contain:

* Mentions (@user)
* URLs

These do not contribute to sentiment analysis, so they are removed to avoid noise.

### 3. Stemming

**Stemming** reduces words to a shared base form (stem), making variants count as the same feature.

Example:

* *tune, tuned, tuning* → **tun**

This reduces vocabulary size and helps the model generalize.

### 4. Lowercasing

Convert all words to lowercase:

* *GREAT*, *Great*, and *great* → **great**

This further reduces duplicate entries in the vocabulary.

### Final Output

After stop-word removal, punctuation removal, handle/URL cleanup, stemming, and lowercasing, you obtain a clean list of words containing only meaningful, normalized tokens.

## Building the Feature Matrix X

This lesson explains how to convert an entire dataset of tweets into a feature matrix **X**, using all the preprocessing and feature extraction techniques learned so far.

### 1. From Raw Tweets to Processed Word Lists

For each of the **m** raw tweets:

* Apply preprocessing:

  * remove stop words
  * remove punctuation
  * remove URLs and user handles
  * lowercase
  * apply stemming
* The result is a clean list of meaningful tokens for each tweet.

### 2. Using the Frequency Dictionary

* With the processed tokens, use the **frequency dictionary** (mapping `(word, class)` → count) to compute:

  * Bias term = 1
  * Sum of positive class frequencies for all words in the tweet
  * Sum of negative class frequencies for all words in the tweet
* This creates a **3-dimensional feature vector** per tweet.

### 3. Building Matrix X

* Initialize an **m × 3** matrix.
* For each tweet:

  1. Preprocess the tweet using `process_tweet`
  2. Extract the three features using the frequency dictionary
  3. Store them as a row in X

### 4. Implementation Notes

* You are given helper functions:

  * `build_freqs` – creates the frequency dictionary
  * `process_tweet` – performs preprocessing
* You must implement the function that extracts the three features from a single processed tweet.

### Result

Once all tweets are processed, you have the matrix **X**, ready to be fed into the logistic regression classifier in the next step.
