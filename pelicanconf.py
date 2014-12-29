#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'tu1978'
SITENAME = u'思いつきメモ'
SITEURL = 'https://formalism.github.io/blog/'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{date:%Y}/{date:%m}/{slug}/'
PAGE_SAVE_AS = 'pages/{date:%Y}/{date:%m}/{slug}/index.html'

THEME = "./pelican-themes/bootstrap"

DISPLAY_PAGES_ON_MENU = True
NEWEST_FIRST_ARCHIVES = True

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/tu1978'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = False

TWITTER_USERNAME="@tu1978"
