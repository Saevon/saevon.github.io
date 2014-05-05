#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from pelican import signals


def add_functions(generator):
    '''
    Adds functions to the jinja2 scope
    '''
    for key, function in generator.settings['JINJA_FUNCTIONS'].iteritems():
        generator.env.globals[key] = function


def register():
    '''
    Plugin registration.
    '''
    signals.generator_init.connect(add_functions)
