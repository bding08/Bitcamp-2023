import pandas as pd
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *

# nltk.download([
#      "names",
#      "stopwords",
#      "state_union",
#      "twitter_samples",
#      "movie_reviews",
#      "averaged_perceptron_tagger",
#      "vader_lexicon",
#      "punkt",
# ])
# sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."

# tokens = nltk.word_tokenize(sentence)

# print("tokens: " + str(tokens))

sia = SentimentIntensityAnalyzer()
# print(sia.polarity_scores("sachin really sucks but he is alright at coding"))
# print(sia.__dict__)

df = pd.read_csv("Top Posts.csv")
print(df)

for index, row in df.iterrows():
    polarity_score = sia.polarity_scores(row['Title'])
    # print("row " + str(index) + ": " + str(polarity_score))
    print("row " + str(index) + ": " + " Sentiment Analysis Compound Score: " + str(polarity_score['compound']))
    # print(f"row {index}: {row['name']} is {row['age']} years old and {row['gender']}.")

# vader = SentimentIntensityAnalyzer()

# f = lambda title: vader.polarity_scores(title)['compound']

