from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import WebScraper.SentimentCalculator
import WebScraper.WebScraper
import pymongo_get_database

app = Flask(__name__, template_folder="template")
Bootstrap(app)

"""
@app.route("/")
def hello_world():
   return "<p>Hello, World!</p>"

"""
@app.route("/")
def index():
    # data = WebScraper.SentimentCalculator.calculate_sentiment(WebScraper.WebScraper.reddit_scraper("Investing")) 

    # json_obj_list = [serialize(x) for x in data]

    # for json_obj in json_obj_list:
    #     pymongo_get_database.insert_into_database(json_obj)

    final_list = pymongo_get_database.get_data_from_mongodb()
    print(final_list)
    return render_template("index.html", stocks=final_list)

   #data = [[f"Row {i+1}, Col {j+1}" for j in range(3)] for i in range(10)]
   #return render_template('index.html', data=data)


# render the index.html template with the data variable

# Flask App Setup 
# Step 1 -> Cmd+Shift+P -> Python: Create Environment
# Step 2 -> copy and paste code within brackets (include ".") to activate the environment in terminal
# <. newEnv/bin/activate>
# If you are missing any dependencies, such as flask, sqlalchemy, sqlalchemy-cockroachdb, or psycopg2
# pip install within the environment


def serialize(stock_obj):
    return {
        "stock_keyword" : str(stock_obj.stock_keyword),
        "tSentiment" : stock_obj.tSentiment,
        "cSentiment" : stock_obj.cSentiment,
        "price_change_percentage" : stock_obj.price_change_percentage
    } 