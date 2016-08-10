#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

import re



def title_case(title):
    '''
    Changes the title to be in proper title case
    '''
    parts = re.split(r'(\W+)', unicode(title))
    return ''.join([word[0:1].upper() + word[1:] for word in parts])

