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


