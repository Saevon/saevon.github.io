#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals



############################
# Basic Details

AUTHOR = u'Saevon'
SITENAME = u'Saevon.ca'
SITEURL = ''
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
THEME = './'



############################
# Content

# Location of blog content
PATH = 'content'
ARTICLE_DIR = 'articles'

# Articles per page
DEFAULT_PAGINATION = 2

# Which direct templates should be paginated
PAGINATED_DIRECT_TEMPLATES = ()

# If the article is in a folder and doesn't have a category use the folder name as its category
USE_FOLDER_AS_CATEGORY = True

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
MD_EXTENSIONS = [
	'meta',
	'sane_lists',
	'smarty(smart_quotes=False)',
	'codehilite(css_class=highlight)',
	'extra',
	'del_ins',
	'alerts',
]

# Fix the import path
import sys
sys.path.append('.')

JINJA_EXTENSIONS  = []
from plugins.debug_dump import dump, dump_all
from plugins.category import find_category, category_preview_articles
from plugins.summary import summary
from plugins.tags import update_tags_count
JINJA_FILTERS = {
	'find_category': find_category,
	'category_preview_articles': category_preview_articles,
	'update_tags_count': update_tags_count,
	'summary': summary,

	# DEBUG
	'dump': dump,
	'dump_all': dump_all,
}



############################
# Links

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

# Blog Links
LINKS =  (

)

# My Account Links
ACCOUNTS = (
    # (icon, url)
    ('github-square', 'https://github.com/Saevon'),
    ('linkedin-square', 'https://ca.linkedin.com/in/saevon'),
)

# Social widget
SOCIAL = (
    ('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

