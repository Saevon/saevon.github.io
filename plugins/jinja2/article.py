#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals


def is_untold(article):
    style = getattr(article, 'style', [])

    return "untold" in style and article.settings['SHOW_UNTOLD']



