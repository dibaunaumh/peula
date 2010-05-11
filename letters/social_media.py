import urllib2
from django.utils import simplejson

TWITTER_SEARCH_URL = 'http://search.twitter.com/search.json?q={query}'


def get_mentions(s):
    """
    Get mentions from social media sources, for now only Twitter.
    """
    mentions = []
    url = TWITTER_SEARCH_URL.format(query=s)
    req = urllib2.urlopen(url)
    json = req.read()
    ret = simplejson.loads(json)
    for e in ret["results"]:
        mentions.append((e["from_user"], e["text"], e["profile_image_url"]))
    return mentions
        