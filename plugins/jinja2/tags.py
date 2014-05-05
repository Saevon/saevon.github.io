#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals


def tag_remap(data):
    new = []
    for item in data:
        tag = item[0]
        tag.articles = item[1]
        tag.count = len(tag.articles)

        new.append(tag)

    return new

def tag_sort(tags):
    '''
    Sorts first by name
    '''
    return sorted(tags, key=lambda tag: unicode(tag).lower())

def tag_ratios(tags, lowest=10, highest=100, attr='percent'):
    '''
    Adds a percentage ratio of how close to the maximum the tag count was
    '''
    maximum = max(map(lambda val: val.count, tags))

    for tag in tags:
        tag.maximum = maximum
        tag.ratio = float(tag.count) / float(tag.maximum)
        setattr(tag, attr, (tag.ratio * (highest - lowest)) + lowest)

    return tags

def update_count(data, search):
    for tag in data:
        for item in search:
            if unicode(item[0]) == unicode(tag):
                tag.count = len(item[1])
                break

    return data


