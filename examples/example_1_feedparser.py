# ! pip install feedparser

import feedparser

feed = feedparser.parse('https://news.bitcoin.com/feed/')

# print('what\'s available on feed level', feed.keys())

post = feed['entries'][0]  # latest post

# print('what\'s available on post level', post.keys())

print('title:', post['title'])
print('published:', post.published)
print('author:', post['author'])
print('summary:', post['summary'])
print('-' * 40)
print('content:', post['content'][0]['value'])
