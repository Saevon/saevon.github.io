#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from .article import is_untold


def find_category(categories, name):
    found = None
    for category in categories:
        if category[0] == name:
            found = category
            break

    if found is None:
        raise KeyError('Category not found: %s' % name)

    return found

def mark(items, type):
    for item in items:
        item.marked_type = type

    return items

def category_preview_articles(articles, num=None):
    articles = filter(lambda article: not is_untold(article), articles)
    articles = sorted(articles, key=lambda val: val.date, reverse=True)

    if num is not None:
        articles = articles[:num]

    return articles



