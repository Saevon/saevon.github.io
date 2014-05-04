#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from jinja2 import contextfilter


@contextfilter
def update_tags_count(context, tags):
	for tag in tags:
		for search in context['tags']:
			if unicode(search[0]) == unicode(tag):
				tag.count = len(search[1])
				break

	return tags


