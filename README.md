# Bitcamp-2023
Project for Bitcamp 2023

Should you trust social media for your investment advice? Specifically, Reddit? This project scrapes investment-related subreddits and uses Natural Language Processing to provide sentiment analysis on popular stocks. The sentiment ratings are compared to the real performance of stocks to help you analyze if your Reddit advice is accurate!

We started by harvesting our data by web scraping Reddit using an API library called PRAW in addition to Python Regex. From there we worked to filter this raw data into usable data that contained keywords and stocks interesting to us. This involved using the Python library Pandas to visualize the data we collected as CSV files. Once we found the relevant posts we then ran Natural Language Processing on our data to quantity user sentiment towards a particular stock. Following this, we serialized our data into JSON format for ease of access and flexibility. We also used Flask to help visualize all this data. In the backend, we connected our MongoDB database and handled data generation. In the frontend we created a table view that displays the information we collected about each stock in each column. We combined the post and comment sentiment into an overall sentiment for the stock. Finally, we compared it to the actual stock performance in the last column and visualized the results.

In the future, we want to make the data a lot more comprehensive and provide a better user interface to allow for customization. We would like to allow the user to choose which subreddit to gather data on, and potentially expand to be a general sentiment tracker for subreddits and topics.

This project was the winner of Bitcamp 2023's "Best Use of MongoDB Atlas" Category
