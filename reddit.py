from turtle import pos
import praw
import pandas as pd

# Read-only instance
reddit_read_only = praw.Reddit(client_id="cmr3_rsMryjWvkQGMaFknw",         # your client id
                               client_secret="IpzAr97DF1pA0LKtcDCJ1jPJNwCUaw",      # your client secret
                               user_agent="Scraping for class")        # your user agent
#creates table
post_dict = {"Title": [], "Post Text": [], "ID Number": [], "Score": [], "Total Comments": [], "Post URL": [], "Keyword": [], "Subreddit": []}

sub = input("Subreddit? (y/n) ") #asks user if they want to specify a subreddit
if sub == 'n': #if they dont want to specify
    subberreddit = "all" #r/all
    subreddit = reddit_read_only.subreddit(subberreddit)
    keyword = input("Enter keyword to search: ") #asks user to input a keyword to crawl for
    print()
    for i in subreddit.search(keyword, limit = None): #seaches for posts following keyword in r/all and then populates the table
        post_dict["Title"].append(i.title)
        post_dict["Post Text"].append(i.selftext)
        post_dict["ID Number"].append(i.id)
        post_dict["Score"].append(i.score)
        post_dict["Total Comments"].append(i.num_comments)
        post_dict["Post URL"].append(i.url)
        post_dict["Keyword"].append(keyword)
        post_dict["Subreddit"].append(subberreddit)
else: #anything other than 'n' is inputted
    subberreddit = input("Enter desired subreddit: ") #askes user for the subreddit to crawl through
    subreddit = reddit_read_only.subreddit(subberreddit) #r/(user input)
    keyword = input("Enter keyword to search: ") #asks user to input a keyword to crawl for
    print()
    for i in subreddit.search(keyword, limit = None): #seaches for posts following keyword in r/(user input) and then populates the table
        post_dict["Title"].append(i.title)
        post_dict["Post Text"].append(i.selftext)
        post_dict["ID Number"].append(i.id)
        post_dict["Score"].append(i.score)
        post_dict["Total Comments"].append(i.num_comments)
        post_dict["Post URL"].append(i.url)
        post_dict["Keyword"].append(keyword)
        post_dict["Subreddit"].append(subberreddit)

posts = pd.DataFrame(post_dict) #make it a table
posts
posts.to_csv("Reddit Crawl.csv", index=True) #export to csv