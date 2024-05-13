# import facebook_scraper as fs
# for post in fs.get_posts('nintendo', pages=1):
#     print(post['text'][:50])

# from twitter_scraper import get_tweets
# for tweet in get_tweets('twitter', pages=1):
#  print(tweet['text'])

import requests

def get_tweets(username, pages=1):
  print("Hi")
  url = f"https://publish.twitter.com/oembed?url=https://twitter.com/{username}"
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
  }
  print(url)
  print(headers)
  for page in range(pages):
      print(page)
      params = {"align": "center", "hide_thread": "on"} if page > 0 else {}
      response = requests.get(url, headers=headers, params=params)
      print(response.raise_for_status())
      # try:
      #     response.raise_for_status()
      #     html = response.json()["items_html"]
      #     yield from gen_tweets(html)
      # except requests.exceptions.HTTPError as e:
      #     print(f"HTTP error: {e}")
      # except requests.exceptions.JSONDecodeError as e:
      #     print(f"JSONDecodeError: {e}")
      # except Exception as e:
      #     print(f"Unexpected error: {e}")

get_tweets("WNiezorawska")