import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = pd.read_csv("Top Posts.csv")
print(df)

# vader = SentimentIntensityAnalyzer()

# f = lambda title: vader.polarity_scores(title)['compound']
