#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals



############################
# Basic Details

AUTHOR = u'Saevon'
EMAIL =u'dot.saevon@gmail.com'
SITENAME = u'Saevon.ca'
SITEURL = u''
TIMEZONE = 'Canada/Eastern'
DEFAULT_LANG = u'en'
THEME = 'theme'



############################
# Content

# Taglines for auto-generated items with no page
TAG_TAGLINES = {
}
CATEGORY_TAGLINES = {
    'coding': 'Coding for fun! (and profit)',
    'review': 'Have fun, then write about why',
    'personal': 'Random miscellaneous articles',
    'roleplaying': 'My public campaign details and notes',
}

# Location of blog content
PATH = 'content'
ARTICLE_DIR = 'articles'

# Templates that mage a page, rather than being a layout
DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')

# Articles per page
DEFAULT_PAGINATION = 2

# Which direct templates should be paginated
PAGINATED_DIRECT_TEMPLATES = ()

# If the article is in a folder and doesn't have a category use the folder name as its category
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'personal'

# Disable the authors list page (as there is only one author)
AUTHORS_SAVE_AS = False


# Feed generation is usually not desired when developing
# FEED_ATOM = ('atom.xml')
FEED_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

FEED_DOMAIN = SITEURL
TRANSLATION_FEED = None



############################
# Coding
MD_EXTENSIONS = (
    'meta',
    'sane_lists',
    'smarty(smart_quotes=False)',
    'codehilite(css_class=highlight)',
    'extra',
    'del_ins',
    'alerts',
)

# Fix the import path, then get all the plugins
import sys
sys.path.append('.')
from plugins import JINJA_EXTENSIONS, JINJA_FILTERS


# Delete the output directory every time we generate the code
DELETE_OUTPUT_DIRECTORY = True



############################
# Urls

# Categories are the root directory under which articles go
CATEGORY_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'

# Articles go directly under their category
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
ARTICLE_URL = '{category}/{slug}/'

# No need for a categories page, as the index page already does that
# But any links to it should head to the right place
CATEGORIES_SAVE_AS = False
CATEGORIES_URL = ''

# The tags page is actually for tags and categories
TAGS_SAVE_AS = 'tags/index.html'
TAGS_URL = 'tags/'

# Individual tags have a page for each of them
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAG_URL = 'tags/{slug}/'



############################
# Menu bar Links

# Blog Links
LINKS =  (
    # (Menu Name, url),
)

# My Account Links
ACCOUNTS = (
    # (icon, url),
    ('github-square', 'https://github.com/Saevon'),
    ('linkedin-square', 'https://ca.linkedin.com/in/saevon'),
)



