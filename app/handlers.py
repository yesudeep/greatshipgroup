#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Main handlers.
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
from google.appengine.ext import db, webapp
from google.appengine.api import memcache
from google.appengine.ext.webapp.util import run_wsgi_app
from utils import render_template, render_cached_template, RequestHandler, CachingRequestHandler
from recaptcha.client import captcha
from models import Vessel, Feedback, SupplierInformation, LegalTerms
import logging
import appengine_admin
import utils

# Set up logging.
logging.basicConfig(level=logging.DEBUG)

class IndexHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('index.html')

# About
class AboutHandler(CachingRequestHandler):
    def get(self):
        self.render_to_response('about/mission.html')

class ManagementHandler(CachingRequestHandler):
    def get(self):
        from models import Manager, BoardDirector, Auditor, SeniorManagement
        managers = Manager.get_all()
        board_directors = BoardDirector.get_all()
        auditors = Auditor.get_all()
        senior_managers = SeniorManagement.get_all()
        self.render_to_response('about/management.html', managers=managers, board_directors=board_directors,auditors=auditors, senior_managers=senior_managers)

class OverseasHandler(CachingRequestHandler):
    def get(self):
        self.render_to_response('about/overseas.html')

class FinancialHandler(CachingRequestHandler):
    def get(self):
        self.render_to_response('about/financial.html')

class SitemapHandler(CachingRequestHandler):
    def get(self):
        self.render_to_response('sitemap.html')

# Services
class FleetHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        vessels = Vessel.get_all()
        self.render_to_response('services/fleet.html', vessels=vessels)

class FleetStatusHandler(CachingRequestHandler):
    def get(self):
        operating_vessels = Vessel.get_operating_vessels()
        operating_rigs = Vessel.get_operating_rigs()
        under_construction_vessels = Vessel.get_under_construction_vessels()
        d = utils.get_previous_month()
        previous_month = utils.datetimeformat(d, format="%B")
        previous_year = utils.datetimeformat(d, format="%Y")
        self.render_to_response("services/fleet_status.html", operating_vessels=operating_vessels, 
            operating_rigs=operating_rigs, 
            under_construction_vessels=under_construction_vessels,
            previous_month=previous_month,
            previous_year=previous_year)

class LogisticsHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('services/logistics.html')                     
        
class ConstructionHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('services/construction.html')           

class DrillingHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('services/drilling.html')
        
class QhseHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('services/qhse.html')


# Corporate relations
class OfficesHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('about/offices.html')

class SuppliersHandler(CachingRequestHandler):
    def get(self):
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
        captcha_challenge_field = self.request.get('recaptcha_challenge_field')
        captcha_response_field = self.request.get('recaptcha_response_field')
        captcha_response = captcha.submit(
            captcha_challenge_field,
            captcha_response_field,
            configuration.RECAPTCHA_PRIVATE_KEY,
            self.request.remote_addr
        )
        if captcha_response.is_valid:
            full_name = self.request.get('name')
            email = self.request.get('email')
            subject = self.request.get('subject')
            content = self.request.get('content')
            designation = self.request.get('designation')
            website_url = self.request.get('website_url')
            
            supplier_info = SupplierInformation()
            supplier_info.full_name = full_name
            supplier_info.email = email
            supplier_info.website_url = website_url
            supplier_info.designation = designation
            supplier_info.subject = subject
            supplier_info.content = content
            supplier_info.put()
            
            self.redirect('/')
        else:
            error = captcha_response.error_code
            self.redirect('/contact/suppliers?captcha_error=%s' % error)


class FeedbackHandler(CachingRequestHandler):
    def get(self):
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
        captcha_challenge_field = self.request.get('recaptcha_challenge_field')
        captcha_response_field = self.request.get('recaptcha_response_field')
        captcha_response = captcha.submit(
            captcha_challenge_field,
            captcha_response_field,
            configuration.RECAPTCHA_PRIVATE_KEY,
            self.request.remote_addr
        )
        if captcha_response.is_valid:
            full_name = self.request.get('name')
            email = self.request.get('email')
            subject = self.request.get('subject')
            content = self.request.get('content')
            
            feedback = Feedback()
            feedback.full_name = full_name
            feedback.email = email
            feedback.subject = subject
            feedback.content = content
            feedback.put()
            
            self.redirect('/')
        else:
            error = captcha_response.error_code
            self.redirect('/contact/feedback?captcha_error=%s' % error)

class CareersHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('careers/careers.html')

class TourHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('careers/tour.html')

class PressReleasesHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('press.html')

# Legal
class PolicyHandler(CachingRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render_to_response('legal/policy.html')

class TermsHandler(CachingRequestHandler):
    def get(self, slug):
        legal_terms = LegalTerms.get_by_slug(slug)        
        self.render_to_response('legal/terms.html', legal_terms=legal_terms)

urls = (
    (r'/', IndexHandler),
    (r'/about/?', AboutHandler),
    (r'/about/mission/?', AboutHandler),
    (r'/about/management/?', ManagementHandler),
    (r'/about/overseas/?', OverseasHandler),
    (r'/about/financial/?', FinancialHandler),
    (r'/careers/?', CareersHandler),
    (r'/careers/tour/?', TourHandler),
    (r'/contact/?', OfficesHandler),
    (r'/contact/offices/?', OfficesHandler),
    (r'/contact/suppliers/?', SuppliersHandler),
    (r'/contact/feedback/?', FeedbackHandler),
    (r'/legal/policy/?', PolicyHandler),
    (r'/legal/terms/(.*)/?', TermsHandler),
    (r'/press/?', PressReleasesHandler),
    (r'/services/?', FleetHandler),
    (r'/services/fleet/?', FleetHandler),
    (r'/services/fleet/status/?', FleetStatusHandler),
    (r'/services/fleet/construction/?', ConstructionHandler),
    (r'/services/fleet/drilling/?', DrillingHandler),
    (r'/services/fleet/logistics/?', LogisticsHandler),
    (r'/services/qhse/?', QhseHandler),
    (r'/sitemap/?', SitemapHandler),
    (r'(/admin)(.*)$', appengine_admin.Admin),
)
application = webapp.WSGIApplication(urls, debug=configuration.DEBUG)

def main():
    from gaefy.db.datastore_cache import DatastoreCachingShim
    DatastoreCachingShim.Install()
    run_wsgi_app(application)
    DatastoreCachingShim.Uninstall()

if __name__ == '__main__':
    main()

