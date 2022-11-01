#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses title of all hot articles, and prints sorted count of given keywords """
import requests
import sys
global_var = None
dictio = []

def count_words(subreddit, word_list):
    global global_var
    global dictio
    header = {'User-Agent': 'xica369'}
    get_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    param = {'after': after}

    response = requests.get(get_url, headers=header, allow_redirects=False, parameters=param)