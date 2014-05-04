#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals


def find_category(categories, name):
	found = None
	for category in categories:
		if category[0] == name:
			found = category
			break

	if found is None:
		raise KeyError('Category not found: %s' % name)

	return found

def category_preview_articles(category, num=None):
	articles = category[1]
	articles = sorted(articles, key=lambda val: val.date)

	if num is not None:
		articles = articles[:num]

	return articles

