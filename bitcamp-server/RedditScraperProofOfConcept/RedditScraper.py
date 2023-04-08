import praw
import pandas as pd
 
reddit_read_only = praw.Reddit(client_id="hVGVldw07s3UNW4rd3zlSQ",         # your client id
                               client_secret="OsFqtnOsdyXyeTXXK6YhD_yjWV5uyg",      # your client secret
                               user_agent="Brian Ding")        # your user agent
 
 
subreddit = reddit_read_only.subreddit("wallstreetbets")
 
# Display the name of the Subreddit
print("Display Name:", subreddit.display_name)
 
# Display the title of the Subreddit
print("Title:", subreddit.title)
 
# Display the description of the Subreddit
# print("Description:", subreddit.description)


# subreddit = reddit_read_only.subreddit("Python")
 
# for post in subreddit.top(limit=5):
#     print(post.title)
#     print()
posts = subreddit.top(time_filter = "week", limit = 5)

for post in posts:
    print("Title:", post.title)
    print("Content:", post.selftext)
    print("-----------------------------------------------")

# Scraping the top posts of the current month
posts = subreddit.top(time_filter = "week", limit = 5)
 
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }
 
for post in posts:
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
 
# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
print(top_posts)

top_posts.to_csv("Top Posts.csv", index=True)
