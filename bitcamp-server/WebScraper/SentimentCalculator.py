import WebScraper
import pandas as pd
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from models import Stock

# when running on your own laptop, uncomment the following below to download
# necessary dependencies and NLTK libraries: 

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

# example of tokenizing a string: 

# sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
# tokens = nltk.word_tokenize(sentence)
# print("tokens: " + str(tokens))

def calculate_sentiment(csv_file):
    output = ""
    sia = SentimentIntensityAnalyzer()

    df = pd.read_csv("filtered_post_data.csv")
    Stock_List = []
    for index, row in df.iterrows():
        polarity_score_title = sia.polarity_scores(row['Title'])

        if (row['Post Comments']):
            polarity_score_post_comments = sia.polarity_scores(str(row['Post Comments']))
            Stock_List.append(Stock(row['Stock Keyword']), str(polarity_score_title['compound']),str(polarity_score_post_comments['compound']))
        else:
            Stock_List.append(Stock(row['Stock Keyword']), str(polarity_score_title['compound']),"No Comments")
    return Stock_List

# calculate_sentiment(WebScraper.reddit_scraper("Investing"))