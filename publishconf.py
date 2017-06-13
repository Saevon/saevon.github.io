#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)

from pelicanconf import *


############################################
# Site details
SITEURL = '//blog.saevon.ca'
RELATIVE_URLS = False


########################################
# Features

# Hide Untold Stories
SHOW_UNTOLD = True


########################################
# Feeds


FEED_RSS = None
FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = True


########################################
# External Resources

DISQUS_SITENAME = 'blog-saevon'
#GOOGLE_ANALYTICS = ""
