#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Utilities.
# Copyright (c) 2010 happychickoo.
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import configuration

import re
import unicodedata
from google.appengine.ext import webapp
from gaefy.jinja2.code_loaders import FileSystemCodeLoader
from haggoo.template.jinja2 import render_generator
from functools import partial


# Conveninence wrapper to make sure int conversion uses a decimal base.
dec = partial(int, base=10)


def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
    return re.sub('[^a-zA-Z0-9-]+', '-', s).strip('-')
 
 
render_template = render_generator(loader=FileSystemCodeLoader, builtins=configuration.TEMPLATE_BUILTINS)

def render_cached_template(template_name, **kwargs):
    """
    Renders a template and caches the output in memcached.
    """
    cache_key = template_name + str(kwargs)
    response = memcache.get(cache_key)
    if not response:
        response = render_template(template_name, **kwargs)
        memcache.set(cache_key, response, 120)
    return response

if configuration.DEPLOYMENT_MODE == configuration.MODE_DEVELOPMENT:
    render_cached_template = render_template

class RequestHandler(webapp.RequestHandler):
    """
    Base handler for templates.
    """
    def render_to_response(self, template_name, **template_values):
        response = render_template(template_name, **template_values)
        self.response.out.write(response)

class CachingRequestHandler(RequestHandler):
    """
    Base handler for static templates.
    """
    def render_to_response(self, template_name, **template_values):
        response = render_cached_template(template_name, **template_values)
        self.response.out.write(response)
