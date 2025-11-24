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