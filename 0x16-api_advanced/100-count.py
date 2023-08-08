#!/usr/bin/python3
"""
Provides a recursive function that queries the Reddit API
parses the title of all hot articles and prints a sorted
count of given keywords.
"""

from collections import Counter
import requests
import json
def count_words(subreddit, word_list):
    """
    Queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).
    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to search for.
    """
    url = "https://www.reddit.com/r/{}.json?limit=10".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'My User Agent'})
    if response.status_code == 200:
        result = response.json()
        titles = [item['data']['title'] for item in result['data']['children']]
        counts = {word: 0 for word in word_list}
        for title in titles:
            for word in word_list:
                if word.lower() in title.lower():
                    counts[word] += 1
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(word, count)
    else:
        print('Invalid subreddit.')
if __name__ == '__main__':
    subreddit = input('Enter a subreddit: ')
    word_list = input('Enter a list of words, separated by spaces: ').split()
    count_words(subreddit, word_list)
