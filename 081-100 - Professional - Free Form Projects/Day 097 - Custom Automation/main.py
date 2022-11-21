## FreshRSS to Wordpress Daily Digest Poster

import feedparser
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods import posts
import datetime

cur_date = datetime.datetime.now().strftime(('%A %Y-%m-%d'))

# URL of Fresh RSS Feed
# By default the "hours" at the end is like 192,
# it should be changed to 24 to just get the last day.
freshrss_url = ""
# Wordpress Username
wp_user = ""
# Wordpress Password
wp_pass = ""
## URL of the Wordpress Site
wp_url = ""

## Category to post under.  This can be a list of Categories
categories=[""]
## Tag to post under.  This can be a list of Categories
tags=[""]

def get_feed(feed_url):
    NewsFeed = feedparser.parse(feed_url)
    return NewsFeed

def make_post(NewsFeed):
    wp = Client(f'https://{wp_url}/xmlrpc.php', wp_user, wp_pass)

    post = WordPressPost()
    post.title = f"{cur_date} - Link List"
    post.terms_names = {'category': categories, 'post_tag': tags}
    post.content = f"<p>Link List for {cur_date}</p>"
    for each in NewsFeed.entries:
        post.content += f'{each.published[5:-15].replace(" ", "-")} - <a href="{each.links[0].href}">{each.title}</a></p>'

    post.post_status = 'publish'
    post.id = wp.call(NewPost(post))

NewsFeed = get_feed(freshrss_url)
if len(NewsFeed.entries) > 0:
    make_post(NewsFeed)