# pip install git+https://github.com/markeyev/feedparser_wrapper.git

from feedparser_wrapper.feedparser_wrapper import Feed

feed = Feed(feed_url='https://news.bitcoin.com/feed/', modified=0, etag='')

data = feed.parse()

post = data['posts'][0]

print('title:', post['title'])
print('published:', post['published'])
print('summary:', post['summary'])
print('-' * 40)
print('content:', post['content'])
