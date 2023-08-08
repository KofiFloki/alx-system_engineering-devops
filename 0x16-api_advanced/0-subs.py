#!/usr/bin/python3
"""
A function that queries the
Reddit API and returns the number of
subscribers
"""
import requests


def number_of_subscribers(subreddit):
    # Get the JSON response from the Reddit API.
    response = requests.get(
        "https://api.reddit.com/r/{}/about".format(subreddit),
        headers={"User-Agent": "my-app/0.0.1"},
    )
    # Check if the response was successful.
    if response.status_code != 200:
        return 0
    # Get the number of subscribers from the JSON response.
    response_json = response.json()
    return response_json["subscribers"]
