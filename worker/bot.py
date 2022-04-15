# importing the module 
from datetime import time
import praw  
# initialize with appropriate values 
client_id = "6SVrWF9tph3rr3-r98E1VA" 
client_secret = "Jx_HLO3mLeVTTHMkAjHMSmbZqG2WcA" 
username = "SourceScanCSC468" 
password = "Group8jamds" 
user_agent = "SourceScan" 
  
# creating an authorized reddit instance 
reddit = praw.Reddit(client_id = client_id,  
                     client_secret = client_secret,  
                     username = username,  
                     password = password, 
                     user_agent = user_agent) 
                     
# to find the top most submission in the subreddit "news" 
subreddit = reddit.subreddit('news')
print("r/news\n")
for submission in subreddit.search('Russia', sort='top', limit=3): 
    # displays the submission title 
    print(submission.title)   
    # displays the net upvotes of the submission 
    print(submission.score)  
    # displays the url of the submission 
    print(submission.url)

subreddit = reddit.subreddit('worldnews')
print("\nr/worldnews\n")
for submission in subreddit.search('Russia', sort='top',  limit=3):
    #for submission in subreddit.top(limit = 3): 
        # displays the submission title 
    print(submission.title)   
        # displays the net upvotes of the submission 
    print(submission.score)  
        # displays the url of the submission 
    print(submission.url)