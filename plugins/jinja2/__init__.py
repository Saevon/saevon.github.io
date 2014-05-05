#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from itertools import chain

from plugins.jinja2.debug_dump import dump, dump_all
from plugins.jinja2.category import find_category, category_preview_articles, mark
from plugins.jinja2.nav import is_cur_page
from plugins.jinja2.summary import summary
from plugins.jinja2.tags import update_count, tag_remap, tag_sort, tag_ratios


JINJA_FILTERS = {
    'find_category': find_category,
    'category_preview_articles': category_preview_articles,
    'mark': mark,

    'update_count': update_count,
    'tag_remap': tag_remap,
    'tag_ratios': tag_ratios,
    'tag_sort': tag_sort,
    'summary': summary,

    'merge': lambda *args: list(chain(*args)),

    'is_cur_page': is_cur_page,

    # DEBUG
    'dump': dump,
    'dump_all': dump_all,
}

JINJA_EXTENSIONS  = []
