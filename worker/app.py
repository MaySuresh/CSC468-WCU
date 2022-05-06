from flask import Flask, render_template, request
from datetime import time
import praw

import os
template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,'templates')
working = 'webui \\ templates'

working == template_dir
app=Flask(__name__,template_folder = template_dir)
subred = None


@app.route('/')
def index():
    return render_template('index.html')




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

@app.route('/', methods=['POST'])
def getvalue():
    global subred 
    subred = request.form['name']

    subreddit = reddit.subreddit('news')
    news =("\nNews Subreddit: r/news\n")
    for submission in subreddit.search(subred, sort='top',time_filter='week', limit=3): 
        title = ("Article Title : {}".format(submission.title))   
        score =("Net Upvotes: {} ".format( submission.score))     
        url=("URL : {}".format(submission.url))

    subreddit = reddit.subreddit('worldnews')
    wNews = ("\nNews Subreddit: r/worldnews\n")
    for submission in subreddit.search(subred, sort='top', time_filter='week', limit=3):
        wTitle = ("Article Title : {}".format(submission.title))      
        wScore = ("Net Upvotes: {} ".format( submission.score))        
        wUrl = ("URL : {}".format(submission.url))


    subreddit = reddit.subreddit('politics')
    pn = ("\nNews Subreddit: r/politics\n")
    for submission in subreddit.search(subred, sort='top', time_filter='week', limit=3):
            
        pt = ("Article Title : {}".format(submission.title))   
          
        ps = ("Net Upvotes: {} ".format( submission.score))  
         
        pu = ("URL : {}".format(submission.url))
    subreddit = reddit.subreddit('technews')
    tn = ("\nNews Subreddit:r/technews\n")
    for submission in subreddit.search('Russia', sort='top', time_filter='week', limit=3):
        tt =("Article Title : {}".format(submission.title))   
        ts =("Net Upvotes: {} ".format( submission.score))  
        tu =("URL : {}".format(submission.url))

    return render_template('pass.html', n=subred, ne = news,t= title, s = score, u = url, w = wNews, wt = wTitle, ws = wScore,wu = wUrl
    , pn = pn, pt = pt, ps = ps, pu = pu, tn = tn, tt = tt, ts = ts, tu = tu)

    
'''               
   

''' 
