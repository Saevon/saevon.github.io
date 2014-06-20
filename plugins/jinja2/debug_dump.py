#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from jinja2 import contextfilter

from pprint import pformat
from cgi import escape as html_escape


def html_format(variable):
    data = pformat(variable, indent=4)
    data = html_escape(data)
    data = data.replace('    ', '&nbsp;&nbsp;&nbsp;&nbsp;')
    data = data.replace('\n', '<br />')
    return data


def dump(variable):
    return html_format(variable)

@contextfilter
def dump_all(context, var):
    return html_format(context.items())

files = {}
def dump_file(filename):
    ret = files.get(filename, False)
    if ret:
        return ret

    with open(filename, 'r') as fp:
        data = fp.read()

    files[filename] = data
    return data

urls = {}
def dump_url(url):
    ret = urls.get(url, False)
    if ret:
        return ret

    import urllib2
    response = urllib2.urlopen(url)
    html = response.read()

    urls[url] = html

    return html


