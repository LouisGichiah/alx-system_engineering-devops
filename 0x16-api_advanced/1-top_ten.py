#!/usr/bin/python3
"""function that queries the Reddit API and prints titles of first 10 hot posts listed for a given subreddit."""
import requests
import sys

def top_ten(subreddit):
    """if not a valid subreddit, print None."""
    header = {'User-Agent': 'xica369'}
    get_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    param = {'limit': 10}
    response = requests.get(get_url, headers=header, allow_redirects=False, parameters=param)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)