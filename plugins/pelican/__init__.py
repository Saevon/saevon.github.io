#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from plugins.pelican import add_jinja_functions


PLUGINS = (
    add_jinja_functions,
)
