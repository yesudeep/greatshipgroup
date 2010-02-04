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

import logging
import utils
import tornado.web
import tornado.wsgi

from google.appengine.api import memcache
from google.appengine.ext import db, webapp
from google.appengine.ext.webapp.util import run_wsgi_app


from models import Post, Vessel, Feedback, SupplierInformation, LegalTerms, VesselType
from utils import BaseRequestHandler

# Set up logging.
logging.basicConfig(level=logging.DEBUG)

class IndexHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        posts = Post.get_latest(3)
        self.render('index.html', truncate=utils.truncate, posts=posts)

# About
class AboutHandler(BaseRequestHandler):
    def get(self):
        self.render('mission.html')

class ManagementHandler(BaseRequestHandler):
    def get(self):
        from models import Manager, BoardDirector, Auditor, SeniorManagement
        managers = Manager.get_all()
        board_directors = BoardDirector.get_all()
        auditors = Auditor.get_all()
        senior_managers = SeniorManagement.get_all()
        self.render('management.html', managers=managers, board_directors=board_directors,auditors=auditors, senior_managers=senior_managers)

class OverseasHandler(BaseRequestHandler):
    def get(self):
        self.render('overseas.html')

class FinancialHandler(BaseRequestHandler):
    def get(self):
        from models import AnnualReport
        annual_reports = AnnualReport.get_all()
        self.render('financial.html', annual_reports=annual_reports)

class SitemapHandler(BaseRequestHandler):
    def get(self):
        self.render('sitemap.html')

# Services
class FleetHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        vessel_types = VesselType.get_all()
        vessels = Vessel.get_all()
        self.render('fleet.html', vessels=None, vessel_types=vessel_types, content_title="Fleet browser.")

class FleetStatusHandler(BaseRequestHandler):
    def get(self):
        operating_vessels = Vessel.get_operating_vessels()
        operating_rigs = Vessel.get_operating_rigs()
        under_construction_vessels = Vessel.get_under_construction_vessels()
        d = utils.get_previous_month()
        previous_month = utils.datetimeformat(d, format="%B")
        previous_year = utils.datetimeformat(d, format="%Y")
        self.render("fleet_status.html", operating_vessels=operating_vessels,
            operating_rigs=operating_rigs, 
            under_construction_vessels=under_construction_vessels,
            previous_month=previous_month,
            previous_year=previous_year)

class LogisticsHandler(BaseRequestHandler):
    def get(self):
        vessels = Vessel.get_all_logistics()
        self.render('fleet.html', vessels=vessels,
            content_title="Logistics fleet browser.")
        
class ConstructionHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        vessels = Vessel.get_all_construction()
        self.render('fleet.html', vessels=vessels,
            content_title='Construction fleet browser.')

class DrillingHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        vessels = Vessel.get_all_drilling()
        self.render('fleet.html', vessels=vessels,
            content_title='Drilling fleet browser.')
        
class QhseHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render('qhse.html')


# Corporate relations
class OfficesHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render('offices.html')

class SuppliersHandler(BaseRequestHandler):
    def get(self):
        from recaptcha.client import captcha
        captcha_error_code = self.get_argument('captcha_error', None)

        captcha_html = captcha.displayhtml(
            public_key = configuration.RECAPTCHA_PUBLIC_KEY,
            use_ssl = False,
            error = captcha_error_code
            )
        from models import LegalTerms
        legal_terms_list = LegalTerms.get_all()
        
        self.render('suppliers.html', legal_terms_list=legal_terms_list, captcha_html=captcha_html)

    def post(self):
        from recaptcha.client import captcha
        captcha_challenge_field = self.get_argument('recaptcha_challenge_field')
        captcha_response_field = self.get_argument('recaptcha_response_field')
        captcha_response = captcha.submit(
            captcha_challenge_field,
            captcha_response_field,
            configuration.RECAPTCHA_PRIVATE_KEY,
            self.request.remote_ip
        )
        if captcha_response.is_valid:
            full_name = self.get_argument('name')
            email = self.get_argument('email')
            subject = self.get_argument('subject')
            content = self.get_argument('content')
            designation = self.get_argument('designation')
            website_url = self.get_argument('website_url')
            
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


class FeedbackHandler(BaseRequestHandler):
    def get(self):
        from recaptcha.client import captcha
        captcha_error_code = self.get_argument('captcha_error', None)
        
        captcha_html = captcha.displayhtml(
            public_key = configuration.RECAPTCHA_PUBLIC_KEY,
            use_ssl = False,
            error = captcha_error_code
            )
        self.render('feedback.html', captcha_html=captcha_html)

    
    def post(self):
        from recaptcha.client import captcha
        captcha_challenge_field = self.get_argument('recaptcha_challenge_field')
        captcha_response_field = self.get_argument('recaptcha_response_field')
        captcha_response = captcha.submit(
            captcha_challenge_field,
            captcha_response_field,
            configuration.RECAPTCHA_PRIVATE_KEY,
            self.request.remote_ip
        )
        if captcha_response.is_valid:
            full_name = self.get_argument('name')
            email = self.get_argument('email')
            subject = self.get_argument('subject')
            content = self.get_argument('content')
            
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

class CareersHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render('careers.html')

class TourHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render('tour.html')

class PressReleasesHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        posts = Post.get_latest(40)
        self.render('press.html', datetimeformat=utils.datetimeformat, posts=posts)

# Note singular
class PressReleaseHandler(BaseRequestHandler):
    def get(self, path):
        post = Post.get_by_path(path)
        if post:
            self.render('press.html', datetimeformat=utils.datetimeformat, posts=[post])
        else:
            self.redirect('/press')

# Legal
class PolicyHandler(BaseRequestHandler):
    """Handles the home page requests."""
    def get(self):
        self.render('policy.html')

class TermsHandler(BaseRequestHandler):
    def get(self, slug):
        legal_terms = LegalTerms.get_by_slug(slug)        
        self.render('terms.html', legal_terms=legal_terms)

# Feeds
class PressFeedAtomHandler(BaseRequestHandler):
    def get(self):
        from datetime import datetime
        posts = Post.get_latest()
        config = dict(host=configuration.HOST_NAME, 
            subtitle="Press Releases",
            title=configuration.APPLICATION_TITLE,
            developer_url=configuration.DEVELOPER_URL,
            developer_name=configuration.DEVELOPER_NAME)
        self.set_header("Content-Type", "application/atom+xml")
        self.render('feeds/atom.xml', posts=posts, datetimeformat=utils.datetimeformat, **config)

settings = {
    "debug": configuration.DEBUG,
    #"xsrf_cookies": True,
    "template_path": configuration.TEMPLATE_PATH,
}
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
    (r'/press/post(.*)', PressReleaseHandler),
    (r'/services/?', FleetHandler),
    (r'/services/fleet/?', FleetHandler),
    (r'/services/fleet/status/?', FleetStatusHandler),
    (r'/services/fleet/construction/?', ConstructionHandler),
    (r'/services/fleet/drilling/?', DrillingHandler),
    (r'/services/fleet/logistics/?', LogisticsHandler),
    (r'/services/qhse/?', QhseHandler),
    (r'/sitemap/?', SitemapHandler),
    (r'/press/feed/atom.xml?', PressFeedAtomHandler),
    #(r'/press/feed/rss.xml?', PressFeedRssHandler),
)
application = tornado.wsgi.WSGIApplication(urls, **settings)

def main():
    from gaefy.db.datastore_cache import DatastoreCachingShim
    DatastoreCachingShim.Install()
    run_wsgi_app(application)
    DatastoreCachingShim.Uninstall()

if __name__ == '__main__':
    main()

