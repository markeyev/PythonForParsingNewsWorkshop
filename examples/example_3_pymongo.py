# https://pymongo.readthedocs.io/

from pymongo import MongoClient, ASCENDING

client = MongoClient('mongodb://localhost:27017/')

db = client.test_database

db.posts.create_index([('url', ASCENDING)], unique=True)

posts = db.posts

post = {
    'url': 'https://news.bitcoin.com/student-coin-stc-token-is-now-listed-on-bitcoin-com-exchange/',
    'feed_hash': '5e82763e721888e9dfa483cf15485e1c',
    'published': 1620907238,
    'title': 'Student Coin (STC) Token Is Now Listed on Bitcoin.com Exchange',
    'summary': 'PRESS RELEASE. Bitcoin.com Exchange is thrilled to announce the listing of STC, being available to '
               'trade on the 13th May 2021 at 10:00AM UTC. STC was created by the Student Coin team, as the reference '
               'currency for all tokens created on its terminal. STC will start trading with USDT, BTC and ETH pairs. ',
    'content': 'What is Student Coin? The aim of the project is to put the tokens and blockchain into the mainstream. '
               'Student Coin is the first platform that allows to perform the wide-scale tokenization for people, '
               'organizations, corporations, startups and decentralized finances (DeFi). Wide-scale tokenization is a '
               'process that needs an easy-to-use and universal ecosystem that is constructed by the Student Coin. '
               'With the STC ecosystem, everyone will be able to easily create any kind of token and develop it in the '
               'long run. Student Coin will allow for tokenizing people, firms and organizations, as well as, manage '
               'token utilities, perform crowdfunding and easily list new projects.University is an environment for '
               'innovation, new technology research, and the source of great ideas. Moreover, universities around the '
               'world are now more connected than ever before and have a lot of external value transfers. Finally, the '
               'global educational market is one of the fastest-growing sectors, creating a great environment to build '
               'disruptive blockchain-based solutions such as the Student Coin. These three factors made universities '
               'a perfect place to create the first wide-scale tokenization platform, similar to how the Internet and '
               'social media began.Student Coin is run by students, faculties, and entrepreneurs from over 20 '
               'universities, including the Kozminski University, New York University, and Harvard University. The '
               'global educational market is one of the fastest-growing sectors, creating a great environment to build '
               'the first wide-scale tokenization platform, similar to how the Internet and social media began.What is '
               'the STC token?The blockchain-based Student Coin ecosystem has its own currency – STC Token. The utility'
               ' and the usage of the STC Token are corresponding to the amenities of blockchain technology and '
               'tokenization. STC works as a reference currency for the equity flow in the whole ecosystem, powering '
               'the STC Terminal usage, STC Exchange trading and STC App applications.The key role of the STC Token is '
               'being the reference currency for all of the tokens ever created at STC Terminal, the personal, DeFi and'
               ' startup tokens will be traded at STC Exchange only to STC, making it the measure of the worth.',
    'tags': ['Press release', 'Bitcoin.com Exchange', 'Student Coin', 'STC']
}

post_id = posts.insert_one(post).inserted_id

print(post_id)

db.posts.delete_one({'_id': post_id})
