import praw
import sys
from datetime import datetime
from pprint import pprint 
from random import randint
from time import sleep
import os
import requests

WEBBIE = os.environ.get("me_discord_webbie")
USER = os.environ.get("gh_username")
ME = os.environ.get("me_discord_id")
def main():
    reddit = praw.Reddit(client_id=os.environ.get('r_cid'),
                         client_secret=os.environ.get('r_cs'),
                         user_agent=os.environ.get('r_ua'),
                         )    
    etf = reddit.redditor(USER)
    current_posts = []
    for x in etf.submissions.new(limit=3):
        current_posts.append({'id': x.id, 'url': x.url, 'date': datetime.fromtimestamp(x.created_utc).strftime('%Y%m%d %H:%M:%S')})
    pprint(current_posts)
    count = 0
    while True:
        new_posts = []
        for x in etf.submissions.new(limit=3):
            new_posts.append({'id': x.id, 'url': x.url, 'date': datetime.fromtimestamp(x.created_utc).strftime('%Y%m%d %H:%M:%S')})
        if (current_posts != new_posts):
            print("not same")
            print(f"NEW POST: {new_posts[0]}")
            requests.post(WEBBIE, data={"content": f"New reddit post {current_posts[0]['url']} <@{ME}>"})
        r = randint(3,10)
        print(f"loopin -> {r}")
        sleep(r)
    return 0

if __name__ == "__main__":
    sys.exit(main())