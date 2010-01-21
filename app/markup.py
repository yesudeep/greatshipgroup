"""
Support for different markup languages for the body of a post.

The following markup languages are supported:
 - HTML
 - Plain text
 - ReStructured Text
 - Markdown
 - Textile

For ReStructuredText and Markdown syntax highlighting of source code is
available.
"""

# TODO: Add summary rendering.
# TODO: Docstrings.

import logging
import re
from cStringIO import StringIO

from django.utils import html
from django.utils import text

import configuration
import utils

# Import markup module from lib/
import markdown
import textile
from docutils.core import publish_parts

def render_rst(content):
  warning_stream = StringIO()
  parts = publish_parts(content, writer_name='html4css1',
                        settings_overrides={
                          '_disable_config': True,
                          'embed_stylesheet': False,
                          'warning_stream': warning_stream,
                          'report_level': 2,
                        })
  rst_warnings = warning_stream.getvalue()
  if rst_warnings:
      logging.warn(rst_warnings)
  return parts['html_body']


def render_markdown(content):
  md = markdown.Markdown()
  return md.convert(content)


def render_textile(content):
  return textile.textile(content.encode('utf-8'))


# Mapping: string ID -> (human readable name, renderer)
MARKUP_MAP = {
    'html':     ('HTML', lambda c: c),
    'txt':      ('Plain Text', lambda c: html.linebreaks(html.escape(c))),
    'markdown': ('Markdown', render_markdown),
    'textile':  ('Textile', render_textile),
    'rst':      ('ReStructuredText', render_rst),
}


def get_renderer(markup_type):
  """Returns a render based on markup type."""
  return MARKUP_MAP.get(markup_type)[1]
