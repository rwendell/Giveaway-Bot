import praw

reddit = praw.Reddit(user_agent='MySimpleBot v0.1',
                     client_id='!YOUR CLIENT ID FOR REDDIT',
                     client_secret='YOUR CLIENT SECRET FOR REDDIT',
                     username='!YOUR REDDIT USERNAME',
                     password='!YOUR REDDIT PASSWORD')

for submission in reddit.subreddit('all').stream.submissions():

    print(vars(submission).keys())
    print(submission.url)
