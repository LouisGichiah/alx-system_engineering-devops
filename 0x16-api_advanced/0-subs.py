#!/usr/bin/python3
"""function queries Reddit API and returns no of subscribers for given subreddit"""
import requests
import sys
def number_of_subscribers(subreddit):
    """If not a valid subreddit, return 0."""
    header = {'User-Agent': 'LouisGichiah'}
    get_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(get_url, headers=header, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return 0
