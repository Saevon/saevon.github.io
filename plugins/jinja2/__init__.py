#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from itertools import chain

from plugins.jinja2.debug_dump import dump, dump_all, dump_file, dump_url
from plugins.jinja2.category import find_category, category_preview_articles, mark
from plugins.jinja2.nav import is_cur_page, get_main
from plugins.jinja2.summary import summary, summary_raw
from plugins.jinja2.tags import update_count, tag_remap, tag_sort, tag_ratios
from plugins.jinja2.date import date_to_xmlschema
from datetime import datetime


JINJA_FILTERS = {
    'find_category': find_category,
    'category_preview_articles': category_preview_articles,
    'mark': mark,

    'update_count': update_count,
    'tag_remap': tag_remap,
    'tag_ratios': tag_ratios,
    'tag_sort': tag_sort,
    'summary': summary,
    'summary_raw': summary_raw,

    'merge': lambda *args: list(chain(*args)),

    'is_cur_page': is_cur_page,

    'date_to_xmlschema': date_to_xmlschema,

    # DEBUG
    'dump': dump,
    'dump_all': dump_all,
}

JINJA_FUNCTIONS = {
    'today': datetime.today,

    'get_main': get_main,
    'dump_file': dump_file,
    'dump_url': dump_url,
}

JINJA_EXTENSIONS  = []
