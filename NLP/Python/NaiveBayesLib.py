import nltk
# nltk.download('twitter_samples') ? Already installed
nltk.download('punkt')

from nltk.corpus import twitter_samples
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import TweetTokenizer

tokenizer = TweetTokenizer()

# > Load dataset
positive = twitter_samples.strings('positive_tweets.json')
negative = twitter_samples.strings('negative_tweets.json')

# > Prepare labeled data
def features(text):
    return {word: True for word in2 tokenizer.tokenize(text)}

train_data = [(features(t), "positive") for t in positive] + \
             [(features(t), "negative") for t in negative]

# > Train Naive Bayes
classifier = NaiveBayesClassifier.train(train_data)

# > Test
def test(text):
    print(classifier.classify(features(text)))

sample = input("Enter to test: ")
test(sample)