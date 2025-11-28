import nltk
nltk.download('twitter_samples')

from nltk.corpus import twitter_samples

positive = twitter_samples.strings('positive_tweets.json')
negative = twitter_samples.strings('negative_tweets.json')

print("Positive example:", positive[0])
print("Negative example:", negative[0])
