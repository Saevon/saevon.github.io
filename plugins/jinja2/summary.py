#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import re

SUMMARY_RE = re.compile(
    # r'^(?P<content>.*?)(?P<headertag><h[1-6].*?>)',
    r'^(?P<content>.*?)(?P<section><[^<>]*?class="[^"]*?section)',
    re.DOTALL,
)


def summary(content):
    match = SUMMARY_RE.match(content)
    if match is None:
        return content

    return match.group('content')


def summary_raw(content):
    return strip_tags(summary(content))


from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def handle_starttag(self, tag, attrs):
        if tag == "br":
            self.fed.append("\n")

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
