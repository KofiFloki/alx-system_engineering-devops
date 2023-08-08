#!/usr/bin/python3
"""
Provides a function that queries the Reddit API
and prints the tittles of the first 10 hot posts
listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    # Get the JSON response from the Reddit API.
    response = requests.get(
        "https://api.reddit.com/r/{}/hot/.json".format(subreddit),
        headers={"User-Agent": "my-app/0.0.1"},
    )
    # Check if the response was successful.
    if response.status_code != 200:
        print("Invalid subreddit")
        return
    # Get the JSON response from the Reddit API.
    response_json = response.json()
    # Get the titles of the first 10 hot posts.
    titles = [post["title"] for post in response_json["data"]["children"][:10]]
    # Print the titles of the first 10 hot posts.
    for title in titles:
        print(title)
