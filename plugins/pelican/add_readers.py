#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from pelican import signals
from pelican import contents


class Contents(object):
    def __init__(self, data):
        self.content = data.content
        self.metadata = data.metadata

    def __getitem__(self, key):
        '''
        Returns the Meta-Data taken from the source file
        '''
        return self.get(key)

    def get(self, key, default=''):
        '''
        Alias for the key operator, but with a default value
        '''
        return self.metadata.get(key, default)

    def __unicode__(self):
        '''
        Returns the unicode format of the Contents (the actual contents of the file)
        '''
        # This ensures that the default usage returns the contents without much effort
        return unicode(self.content)


class Renderer(object):
    '''
    Wrapper that renders any given filename (from the main PATH) giving you
    the resulting object

    Made for use with jinja filters.

    You can render a file, displaying its contents

        {# renders a markdown file #}
        {{ 'filename.md'|render }}

    It also gives you access to the metadata, if there is any,

        {% set contents = 'filename.md'|render %}

        {# output the contents #}
        {{ contents }}

        {# Output some metadata #}
        {{ contents['title'] }}
        {{ contents['author'] }}

    You can also set defaults when accessing metadata,

        {% set contents = 'filename.md'|render %}

        {# Output some metadata with a default values #}
        {{ contents.get('author', default=AUTHOR) }}
    '''
    def __init__(self, generator):
        self.generator = generator

    def __call__(self, filename):
        return self.render(filename)

    @property
    def context(self):
        return self.generator.context

    def render(self, filename):
        data = self.generator.readers.read_file(
            base_path=self.context['PATH'],
            path=filename,
            content_class=contents.Page,
            context=self.context,
        )

        return Contents(data)


def add_readers(generator):
    '''
    Adds functions to the jinja2 scope
    '''
    generator.settings['JINJA_FILTERS'].update({
        'render': Renderer(generator),
    })


def register():
    '''
    Plugin registration.
    '''
    signals.generator_init.connect(add_readers)
