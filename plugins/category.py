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

def category_preview_articles(category, num):
	articles = category[1]
	return sorted(articles, key=lambda val: val.date)[:num]

