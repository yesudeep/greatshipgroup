#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Main handlers.
# Copyright (c) 2009 happychickoo.
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
from gaefy.db.datastore_cache import DatastoreCachingShim
from google.appengine.ext import db, webapp
from google.appengine.api import memcache
from google.appengine.ext.webapp.util import run_wsgi_app
from gaefy.jinja2.code_loaders import FileSystemCodeLoader
from haggoo.template.jinja2 import render_generator
import logging

# Set up logging.
logging.basicConfig(level=logging.DEBUG)

render_template = render_generator(loader=FileSystemCodeLoader, builtins=configuration.TEMPLATE_BUILTINS)

def render_cached_template(template_name, **kwargs):
    cache_key = template_name + str(kwargs)
    response = memcache.get(cache_key)
    if not response:
        response = render_template(template_name, **kwargs)
        memcache.set(cache_key, response, 120)
    return response

if configuration.DEPLOYMENT_MODE == configuration.MODE_DEVELOPMENT:
    render_cached_template = render_template

class IndexHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('index.html')
        self.response.out.write(response)

# About
class AboutHandler(webapp.RequestHandler):
    def get(self):
        response = render_cached_template('about/mission.html')
        self.response.out.write(response)

class ManagementHandler(webapp.RequestHandler):
    def get(self):
        response = render_cached_template('about/management.html')
        self.response.out.write(response)

class OverseasHandler(webapp.RequestHandler):
    def get(self):
        response = render_cached_template('about/overseas.html')
        self.response.out.write(response)

class FinancialHandler(webapp.RequestHandler):
    def get(self):
        response = render_cached_template("about/financial.html")
        self.response.out.write(response)

class SitemapHandler(webapp.RequestHandler):
    def get(self):
        response = render_cached_template("sitemap.html")
        self.response.out.write(response)

# Services
class FleetHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('services/fleet.html')
        self.response.out.write(response)
        
class LogisticsHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('services/logistics.html')
        self.response.out.write(response)                        
        
class ConstructionHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('services/construction.html')
        self.response.out.write(response)            

class DrillingHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('services/drilling.html')
        self.response.out.write(response)
        
class QhseHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('services/qhse.html')
        self.response.out.write(response)


# Corporate relations
class OfficesHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('about/offices.html')
        self.response.out.write(response)

class SuppliersHandler(webapp.RequestHandler):
    def get(self):
        response = render_cached_template("about/suppliers.html")
        self.response.out.write(response)

class CareersHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('careers.html')
        self.response.out.write(response)

class TourHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('tour.html')
        self.response.out.write(response)

class PolicyHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('legal/policy.html')
        self.response.out.write(response)
        
class PressReleasesHandler(webapp.RequestHandler):
    """Handles the home page requests."""
    def get(self):
        response = render_cached_template('press_releases.html')
        self.response.out.write(response)


urls = (
    ('/', IndexHandler),
    ('/about/?', AboutHandler),
    ('/about/mission/?', AboutHandler),
    ('/about/management/?', ManagementHandler),
    ('/about/overseas/?', OverseasHandler),
    ('/about/financial/?', FinancialHandler),
    ('/careers/?', CareersHandler),
    ('/careers/tour/?', TourHandler),
    ('/contact/?', OfficesHandler),
    ('/contact/offices/?', OfficesHandler),
    ('/contact/suppliers/?', SuppliersHandler),
    ('/legal/policy/?', PolicyHandler),
    ('/press/?', PressReleasesHandler),
    ('/services/construction/?', ConstructionHandler),
    ('/services/drilling/?', DrillingHandler),
    ('/services/fleet/?', FleetHandler),
    ('/services/logistics/?', LogisticsHandler),
    ('/services/qhse/?', QhseHandler),
    ('/sitemap/?', SitemapHandler),
)
application = webapp.WSGIApplication(urls, debug=configuration.DEBUG)

def main():
    DatastoreCachingShim.Install()
    run_wsgi_app(application)
    DatastoreCachingShim.Uninstall()

if __name__ == '__main__':
    main()

