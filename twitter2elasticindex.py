from TwitterSearch import *
from elasticsearch import Elasticsearch
es = Elasticsearch()
es.indices.create(index='twitter', ignore=400)

tweet_dict = {}

try:
    tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
    tso.set_keywords(['covid', 'delta'])  # let's define all words we would like to have a look for
    tso.set_language('en')  # we want to see English tweets only
    tso.set_include_entities(True)  # and don't give us all those entity information

    # Please create a Twitter app key here https://apps.twitter.com
    ts = TwitterSearch(
        consumer_key='',
        consumer_secret='',
        access_token='',
        access_token_secret=''
    )
    count = 1
    # iterate through the tweets
    for tweet in ts.search_tweets_iterable(tso):
        #print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
        print (tweet['text'])
        es.index("twitter", body=tweet)
        count = count+1

except TwitterSearchException as e:  # take care of all those errors
    print(e)
