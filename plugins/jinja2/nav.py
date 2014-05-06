#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from jinja2 import contextfilter

@contextfilter
def is_cur_page(context, url, or_child=False):
    page = context.get('page_name')

    # Articles use a different API so check those as well
    article = context.get('article')
    if article is not None:
        page = article.url

    if or_child:
        return url in unicode(page)
    else:
        return url == page
