import praw
import pandas as pd
import re

def reddit_scraper(subreddit):
    # Assigns PRAW API object to a variable
    reddit_read_only = praw.Reddit(
        client_id="hVGVldw07s3UNW4rd3zlSQ",                  # your client id
        client_secret="OsFqtnOsdyXyeTXXK6YhD_yjWV5uyg",      # your client secret
        user_agent="Brian Ding")                             # your user agent
    
    #Reads data from subreddit
    subreddit = reddit_read_only.subreddit(subreddit)
    df = pd.read_csv("stock_info_filtered.csv")

    # Scraping the top posts of the current month
    posts = subreddit.top(time_filter = "month", limit = 200)
    
    posts_dict = {"Title": [], 
                  "Post Text": [],
                  "ID": [], "Score": [],
                  "Total Comments": [], 
                  "Post URL": [], 
                  "Post Comments": [], 
                  "Stock Keyword": []
                }
    #Regex to check whether string matches either Ticker Symbol or Company Name
    stock_regex = r"\b(" + "|".join(df['Ticker'] + "|" + df['Name']) + r")\b"

    i = 1
    for post in posts:
        if post.link_flair_text != 'Meme':
            matches = re.findall(stock_regex, post.title)
            if matches and len(matches[0]) > 1:
                # Title of each post
                posts_dict["Title"].append(post.title)
                
                # Text inside a post
                posts_dict["Post Text"].append(post.selftext)
                
                # Unique ID of each post
                posts_dict["ID"].append(post.id)
                
                # The score of a post
                posts_dict["Score"].append(post.score)
                
                # Total number of comments inside the post
                posts_dict["Total Comments"].append(post.num_comments)
                
                # URL of each post
                posts_dict["Post URL"].append(post.url)

                comment_str = ""
                for comment in post.comments[:5]:
                    comment_str += (str(i) + " " + comment.body)
                    i += 1

                posts_dict["Post Comments"].append(comment_str)
                i = 1

                posts_dict["Stock Keyword"].append(matches[0])

    # Saving the data in a pandas dataframe
    post_data = pd.DataFrame(posts_dict)
    # print(top_posts)

    post_data.to_csv("Filtered Post Data.csv", index=False)

reddit_scraper("Investing")


#Testing Methods

# print(df)
# ticker_column = df['Ticker']
# name_column = (df['Name'].str.replace(' Inc.', '').str.replace(' Technologies', '').str.replace(' Inc', '').str.replace(' Ltd', '')).apply(re.escape)
# df['Name'] = df['Name'].str.replace(' Inc.', '').str.replace(' Technologies', '').str.replace(' Inc', '').str.replace(' Ltd', '')
# df.to_csv("stock_info_filtered.csv", index=False)
# print(ticker_column)
# print(name_column)

# df['Ticker']= df['Ticker'].apply(re.escape)
# df['Name'] = df['Name'].str.replace(' Inc.', '').str.replace(' Technologies', '').str.replace(' Inc', '').str.replace(' Ltd', '')
# df['Name'] = df['Name'].apply(re.escape)
# df.to_csv("stock_info_filtered.csv", index=False)

# Display the name of the Subreddit
# print("Display Name:", subreddit.display_name)
 
# Display the title of the Subreddit
# print("Title:", subreddit.title)
 
# Display the description of the Subreddit
# print("Description:", subreddit.description)

# Printing and Testing
# posts = subreddit.top(time_filter = "month", limit = 200)
# i = 1
# stock_regex = r"\b(" + "|".join(df['Ticker'] + "|" + df['Name']) + r")\b"
# # stock_regex = r'\bGoogle\b'
# for post in posts:
#     if post.link_flair_text != 'Meme':
#         matches = re.findall(stock_regex, post.title)
#         if matches and len(matches[0]) > 1:
#             print(f"Post title: {post.title}")
#             print("Content:", post.selftext)
#             print(f"Matches: {matches}")
#             print("Top Couple Comments:")
#             for comment in post.comments[:5]:
#                 print(str(i) + " " + comment.body)
#                 i = i + 1
#             print("-----------------------------------------------")
#             i = 1
            
    # if post.link_flair_text != 'Meme' and re.search(stock_regex, post.title):
    #     print("Title:", post.title)
    #     print("Content:", post.selftext)
    #     print("Top 5 Comments:")

        # for comment in post.comments[:3]:
        #     print(str(i) + " " + comment.body)
        #     i = i + 1
            
        # print("-----------------------------------------------")
        # i = 1
