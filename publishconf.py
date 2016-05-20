#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import sys
sys.path.append('.')
from utils import filters


AUTHOR = 'Shauna Gordon'
SITENAME = 'Barefoot Shoe Showdown'
TAGLINE = 'Compare Vibram Five Fingers vs Xero Shoes'
SITEURL = 'http://shoes.shaunagordon.com'

PATH = 'content'

ARTICLE_PATHS = ['posts']
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

# Delete the contents of the output directory...
DELETE_OUTPUT_DIRECTORY = False

# ...but save the git stuff
OUTPUT_RETENTION = ('.git', '.gitignore')

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['summary']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
SUMMARY_USE_FIRST_PARAGRAPH = True
SUMMARY_BEGIN_MARKER = "<!-- summary -->"
SUMMARY_END_MARKER = "<!-- more -->"

# Theme
THEME = 'twenty'

# Theme Settings
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images', 'extra']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/travis.yml': {'path': '.travis.yml'}}
JINJA_FILTERS = { 'sidebar': filters.sidebar }

# Blogroll
LINKS = ()

# Social widgets
SOCIAL = ()

TWITTER_USERNAME = ''

# Comments
DISQUS_SITENAME = ''
DISQUS_SECRET_KEY = ''
DISQUS_PUBLIC_KEY = ''

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = False

# Special theme content