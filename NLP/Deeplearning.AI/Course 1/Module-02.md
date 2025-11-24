# Week 2: Probability and Bayes' Rule

## Probability & Bayes Rule — Overview

This lesson reviews basic probability and conditional probability and shows how **Bayes’ rule** follows from those definitions — all framed for NLP tasks like sentiment analysis.

* **Probabilities by counting:** estimate (P(A)) as (count of events (A)) / (total items).

  * Example: if 13 out of 20 tweets are positive, (P(\text{positive}) = 13/20 = 0.65).
  * Complement: (P(\text{negative}) = 1 - P(\text{positive})) (assuming mutually exclusive labels).

* **Events & intersections:** define events (e.g., (A=) “tweet is positive”, (B=) “tweet contains ‘happy’”).

  * Probability of intersection (P(A \cap B)) = (count tweets that are both positive and contain “happy”) / total.
  * Example: if 3 tweets are both positive and contain “happy” out of 20, (P(\text{positive} \cap \text{happy}) = 3/20 = 0.15).

* **Conditional probability:** (P(A \mid B)) describes the probability of (A) given (B); conditional definitions lead directly to Bayes’ rule.

* **Bayes’ rule:** derived from conditional probability identities; useful in NLP for tasks like sentiment classification and (later) autocorrect.

* **Why this matters for NLP:** counting-based probabilities and Bayes’ rule let you reason about how words (like “happy”) relate to labels (positive/negative) across a corpus — foundational for Naive Bayes and other probabilistic models.

Next video: **Naive Bayes** and its application to sentiment analysis.
