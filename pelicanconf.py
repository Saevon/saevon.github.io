#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


############################
# Basic Details

AUTHOR       = u'Saevon'
EMAIL        = u'dot.saevon@gmail.com'
SITENAME     = u'Saevon.ca'
SITEURL      = u''
TIMEZONE     = u'Canada/Eastern'
DEFAULT_LANG = u'en'


############################
# Content

# The theme folder to use
THEME = 'theme'
# The directory to copy statics into
THEME_STATIC_DIR = 'static'
STATIC_DIR = THEME_STATIC_DIR


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

# Templates that make a page, rather than being a layout
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'license', 'sitemap']

# Mapping of URL to title, for history
DIRECT_TEMPLATES.append('history_map_js')
HISTORY_MAP_JS_SAVE_AS = "static/js/history_map.js"
ENABLE_HISTORY_LINKS = True

# Show the Untold Story page (off for Dev)
SHOW_UNTOLD = False

# Articles per page
DEFAULT_PAGINATION = 5

# Which direct templates should be paginated
PAGINATED_DIRECT_TEMPLATES = ()

# If the article is in a folder and doesn't have a category use the folder name as its category
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'personal'

# The author page doesn't exist yet
AUTHOR_SAVE_AS = False
AUTHOR_URL = False
# Disable the authors list page (as there is only one author)
AUTHORS_SAVE_AS = False

# License File
LICENSE_FILE = '../LICENSE.md'
LICENSE_SAVE_AS = 'license/index.html'
LICENSE_URL = 'license/'



# Comments
DISQUS_SITENAME = "dev-blog-saevon"

# Facebook
FACEBOOK_LINK_PROTOCOL = "http"

# Whether to show the powered by pelicaon logo
INCLUDE_PELICAN_LINK = False


############################
# Coding

# Fix the import path, then get all the plugins
import sys
sys.path.append('.')
from plugins.markdown import MD_EXTENSIONS
from plugins.jinja2 import JINJA_EXTENSIONS, JINJA_FILTERS, JINJA_FUNCTIONS
from plugins.pelican import PLUGINS


# Delete the output directory every time we generate the code
DELETE_OUTPUT_DIRECTORY = True


######################################
# Sitemap
#   Used by robots to rank your site

# Sitemap file
SITEMAP_SAVE_AS = "sitemap.xml"

# My custom sitemap data
# Not for use with the pelican sitemap plugin
SITEMAP = {
    'format': 'xml',
    'articles': {
        'priority': 0.5,
        'changefreq': 'monthly',
    },
    'pages': {
        'priority': 0.5,
        'changefreq': 'monthly',
    },
}

###########################
# Feeds

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL

ENABLE_ATOM = False
if ENABLE_ATOM:
    FEED_ATOM = 'atom.xml'
    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    AUTHOR_FEED_ATOM = None
    CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
    TAG_FEED_ATOM = 'feeds/%s.atom.xml'
else:
    FEED_ATOM = None
    FEED_ALL_ATOM = None
    AUTHOR_FEED_ATOM = None
    CATEGORY_FEED_ATOM = None
    TAG_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None


ENABLE_RSS = False
if ENABLE_RSS:
    FEED_RSS = 'rss.xml'
    AUTHOR_FEED_RSS = None
    FEED_ALL_RSS = 'feeds/all.rss.xml'
    CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
    TAG_FEED_RSS = 'feeds/%s.rss.xml'
else:
    FEED_RSS = None
    FEED_ALL_RSS = None
    AUTHOR_FEED_RSS = None
    CATEGORY_FEED_RSS = None
    TAG_FEED_RSS = None
    TRANSLATION_FEED_RSS = None



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
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORIES_URL = 'categories'

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
    # (Menu Name, url, enabled),
)

# My Account Links
ACCOUNTS = (
    # (icon, url, enabled),

    ('rss-square', FEED_RSS, ENABLE_RSS),
    ('rss-square', FEED_ATOM, not ENABLE_RSS and ENABLE_ATOM),
    ('github-square', 'https://github.com/Saevon', True),
    ('linkedin-square', 'https://ca.linkedin.com/in/saevon', True),
)




