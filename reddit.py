import praw
import credentials

reddit = praw.Reddit(
    client_id = credentials.client_id,
    client_secret = credentials.client_secret,
    user_agent="python3:myapp:0.1 (by u/k2tlins)",
)
for submission in reddit.subreddit("eesti").hot(limit=10):
    print(submission.title)
    print(submission.id)
    print(submission.url)
    print(submission.author.name)
    top_level_comments = list(submission.comments)
    print(top_level_comments)
    



