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
