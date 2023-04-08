import praw
import pandas as pd
 
reddit_read_only = praw.Reddit(client_id="hVGVldw07s3UNW4rd3zlSQ",         # your client id
                               client_secret="OsFqtnOsdyXyeTXXK6YhD_yjWV5uyg",      # your client secret
                               user_agent="Brian Ding")        # your user agent
 
 
subreddit = reddit_read_only.subreddit("investing")
 
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
i = 1
for post in posts:
    print("Title:", post.title)
    print("Content:", post.selftext)
    print("Top 5 Comments:")
    for comment in post.comments[:3]:
        print(str(i) + " " + comment.body)
        i = i + 1
        
    print("-----------------------------------------------")
    i = 1

# Scraping the top posts of the current month
posts = subreddit.top(time_filter = "week", limit = 5)
 
posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": [], "Post Comments": []
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

    comment_str = ""
    for comment in post.comments[:5]:
        comment_str += (str(i) + " " + comment.body)
        i += 1

    posts_dict["Post Comments"].append(comment_str)
    i = 1

# Saving the data in a pandas dataframe
top_posts = pd.DataFrame(posts_dict)
print(top_posts)

top_posts.to_csv("Top Posts.csv", index=True)
