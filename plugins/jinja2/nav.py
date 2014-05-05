#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from jinja2 import contextfilter

@contextfilter
def is_cur_page(context, url, or_child=False):
    page = context.get('page_name')
    if or_child:
        return url in unicode(page)
    else:
        return url == page

