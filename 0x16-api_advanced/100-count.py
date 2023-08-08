import requests

def sort_histogram(histogram):
    histogram.sort(key=lambda kv: (-kv[1], kv[0]))
    for word, count in histogram:
        print(f"{word}: {count}")

def count_words(subreddit, word_list, histogram=None, after=None):
    if histogram is None:
        histogram = {word: 0 for word in word_list}

    api_headers = {
        'User-Agent': 'Reddit Keyword Counter'
    }

    sort = 'hot'
    limit = 100
    res = requests.get(
        f'https://www.reddit.com/r/{subreddit}/.json?sort={sort}&limit={limit}&after={after}',
        headers=api_headers,
        allow_redirects=False
    )

    if res.status_code == 200:
        data = res.json()['data']
        posts = data['children']
        titles = [post['data']['title'] for post in posts]

        for word in word_list:
            word_lower = word.lower()
            histogram[word] += sum(title.lower().split().count(word_lower) for title in titles)

        if len(posts) >= limit and data['after']:
            count_words(subreddit, word_list, histogram, data['after'])
        else:
            sorted_histogram = sorted(histogram.items(), key=lambda kv: (-kv[1], kv[0]))
            sort_histogram(sorted_histogram)
    else:
        print(f"Error: Unable to fetch data from Reddit API ({res.status_code})")

# Example usage
count_words("python", ["python", "javascript", "java"])
