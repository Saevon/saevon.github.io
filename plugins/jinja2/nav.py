#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from jinja2 import contextfilter, contextfunction

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


from collections import defaultdict
from itertools import repeat

def factory(value):
    return repeat(value).next


@contextfunction
def get_main(context):
    main = context.get('article', False)

    if not main:
        main = context.get('page', False)

    if not main:
        main = defaultdict(factory(False))

    # context.set('main', main)
    return main
