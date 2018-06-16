import praw
from multiprocessing import Process
import requests

reddit = praw.Reddit(user_agent='MySimpleBot v0.1',
                     client_id='!YOUR CLIENT ID FOR REDDIT',
                     client_secret='YOUR CLIENT SECRET FOR REDDIT',
                     username='!YOUR REDDIT USERNAME',
                     password='!YOUR REDDIT PASSWORD')


def pcmr():
    for submission in reddit.subreddit('pcmasterrace').stream.submissions():

        if submission.link_flair_text == "Giveaway":
            print(str(submission.subreddit) + ": " + str(submission.title))
            r = requests.post("https://api.pushover.net/1/messages.json",
                              data={'token': '!APP TOKEN', 'user': '!USER TOKEN',
                                    'message': str(submission.title), 'title': str(submission.subreddit),
                                    'url': str(submission.url)})


def gamedeals():
    for submission in reddit.subreddit('gamedeals').stream.submissions():
        if "free" in submission.title.lower():
            print(str(submission.subreddit) + ":    " + str(submission.title))
            s = requests.post("https://api.pushover.net/1/messages.json",
                              data={'token': '!APP TOKEN', 'user': '!USER TOKEN',
                                    'message': str(submission.title), 'title': str(submission.subreddit),
                                    'url': str(submission.url)})


if __name__ == '__main__':
    Process(target=pcmr).start()
    Process(target=gamedeals).start()
