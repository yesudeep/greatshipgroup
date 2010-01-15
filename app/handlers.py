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

class StaticRequestHandler(RequestHandler):
    """
    Base handler for static templates.
    """
    def render_to_response(self, template_name, **template_values):
        response = render_cached_template(template_name, **template_values)
        self.response.out.write(response)


class IndexHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('index.html')

# About
class AboutHandler(StaticRequestHandler):
    def get(self):
        self.render_to_response('about/mission.html')

class ManagementHandler(StaticRequestHandler):
    def get(self):
        self.render_to_response('about/management.html')

class OverseasHandler(StaticRequestHandler):
    def get(self):
        self.render_to_response('about/overseas.html')

class FinancialHandler(StaticRequestHandler):
    def get(self):
        self.render_to_response('about/financial.html')

class SitemapHandler(StaticRequestHandler):
    def get(self):
        self.render_to_response('sitemap.html')

# Services
class FleetHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('services/fleet.html')

        
class LogisticsHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('services/logistics.html')                     
        
class ConstructionHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('services/construction.html')           

class DrillingHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('services/drilling.html')
        
class QhseHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('services/qhse.html')


# Corporate relations
class OfficesHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('about/offices.html')

class SuppliersHandler(StaticRequestHandler):
    def get(self):
        from recaptcha.client import captcha
        captcha_error_code = self.request.get('captcha_error')
        if not captcha_error_code:
            captcha_error_code = None

        captcha_html = captcha.displayhtml(
            public_key = configuration.RECAPTCHA_PUBLIC_KEY,
            use_ssl = False,
            error = captcha_error_code
            )
        self.render_to_response('about/suppliers.html', captcha_html=captcha_html)

    def post(self):
        from recaptcha.client import captcha
        captcha_challenge_field = self.request.get('recaptcha_challenge_field')
        captcha_response_field = self.request.get('recaptcha_response_field')
        captcha_response = captcha.submit(
            captcha_challenge_field,
            captcha_response_field,
            configuration.RECAPTCHA_PRIVATE_KEY,
            self.request.remote_addr
        )
        if captcha_response.is_valid:
            self.redirect('/')
        else:
            error = captcha_response.error_code
            self.redirect('/contact/suppliers?captcha_error=%s' % error)


class FeedbackHandler(StaticRequestHandler):
    def get(self):
        from recaptcha.client import captcha
        captcha_error_code = self.request.get('captcha_error')
        if not captcha_error_code:
            captcha_error_code = None

        captcha_html = captcha.displayhtml(
            public_key = configuration.RECAPTCHA_PUBLIC_KEY,
            use_ssl = False,
            error = captcha_error_code
            )
        self.render_to_response('about/feedback.html', captcha_html=captcha_html)

    
    def post(self):
        from recaptcha.client import captcha
        captcha_challenge_field = self.request.get('recaptcha_challenge_field')
        captcha_response_field = self.request.get('recaptcha_response_field')
        captcha_response = captcha.submit(
            captcha_challenge_field,
            captcha_response_field,
            configuration.RECAPTCHA_PRIVATE_KEY,
            self.request.remote_addr
        )
        if captcha_response.is_valid:
            self.redirect('/')
        else:
            error = captcha_response.error_code
            self.redirect('/contact/feedback?captcha_error=%s' % error)

class CareersHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('careers/careers.html')

class TourHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('careers/tour.html')

class PolicyHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('legal/policy.html')
        
        
class PressReleasesHandler(StaticRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('press.html')


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
    ('/contact/feedback/?', FeedbackHandler),
    ('/legal/policy/?', PolicyHandler),
    ('/press/?', PressReleasesHandler),
    ('/services/?', FleetHandler),
    ('/services/fleet/?', FleetHandler),
    ('/services/construction/?', ConstructionHandler),
    ('/services/drilling/?', DrillingHandler),
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

