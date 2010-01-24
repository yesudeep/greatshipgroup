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


from google.appengine.ext import db
from google.appengine.api import memcache
from dbhelper import SerializableModel
from aetycoon import TransformProperty
import appengine_admin

import static
import utils
import markup
import hashlib
import datetime
import dbhelper
import logging


if configuration.DEFAULT_MARKUP in markup.MARKUP_MAP:
    DEFAULT_MARKUP = configuration.DEFAULT_MARKUP
else:
    DEFAULT_MARKUP = 'html'

VESSEL_STATUS_CHOICES = (
    'operational',
    'under_construction',
    'available',
    )

VESSEL_TYPE_CHOICES = (
    '350_ic_jackup_rig',
    'psv',
    'ahtsv',
    'mpssv',
    'msv',
    'rov_support',
    )

VESSEL_GENERIC_TYPE_CHOICES = (
    'rig',
    'vessel',
    )

class Manager(SerializableModel):
    full_name = db.StringProperty()
    designation = db.StringProperty()
    description = db.TextProperty()
    description_html = TransformProperty(description, markup.render_markdown)

class AssetLiabilityStatement(SerializableModel):
    start_year = db.DateProperty()
    end_year = db.DateProperty()
    share_capital = db.StringProperty()
    reserves_and_surplus = db.StringProperty()
    secured_loans = db.StringProperty()
    total_liabilities = db.StringProperty()
    fixed_assets = db.StringProperty()
    investments = db.StringProperty()
    net_current_assets = db.StringProperty()
    total_assets = db.StringProperty()

class IncomeStatement(SerializableModel):
    start_year = db.DateProperty()
    end_year = db.DateProperty()
    total_revenue = db.StringProperty()
    pbdit = db.StringProperty()
    depreciation = db.StringProperty()
    interest = db.StringProperty()
    tax_provision = db.StringProperty()
    pat = db.StringProperty()
    eps = db.StringProperty()

class Vessel(SerializableModel):
    name = db.StringProperty()
    build_year = db.DateProperty()
    vessel_type = db.StringProperty(choices=VESSEL_TYPE_CHOICES)
    yard = db.StringProperty()
    deadweight_in_tons = db.StringProperty()
    design = db.StringProperty()
    bp_in_tons = db.StringProperty()
    dp = db.StringProperty()
    fifi = db.StringProperty()
    company = db.StringProperty()
    when_available = db.DateProperty()
    specification_url = db.URLProperty()
    
    # Classification in table.
    operational_status = db.StringProperty(choices=VESSEL_STATUS_CHOICES)
    generic_type = db.StringProperty(choices=VESSEL_GENERIC_TYPE_CHOICES)

    @classmethod
    def get_all(cls):
        cache_key = 'Vessel.get_all'
        entities = dbhelper.deserialize_entities(memcache.get(cache_key))
        if not entities:
            entities = Vessel.all().fetch(100)
            memcache.set(cache_key, dbhelper.serialize_entities(entities))
        return entities

class AnnualReport(SerializableModel):
    title = db.StringProperty()
    subtitle = db.StringProperty()
    start_year = db.DateProperty()
    end_year = db.DateProperty()
    document_url = db.URLProperty()

class Post(SerializableModel):
    path = db.StringProperty()
    checksum = db.StringProperty()

    title = db.StringProperty()
    place = db.StringProperty()
    when_published = db.DateTimeProperty()
    content = db.TextProperty()
    content_html = db.TextProperty()
    markup_type = db.StringProperty(choices=set(markup.MARKUP_MAP), default=DEFAULT_MARKUP)
    
    def format_post_path(self, num=0, format='/%(year)d/%(month)02d/%(slug)s'):
        slug = utils.slugify(self.title)
        if num > 0:
            slug += "-" + str(num)
        return format % {
            'slug': slug,
            'year': self.when_published.year,
            'month': self.when_published.month,
            'day': self.when_published.day,
            }
    
    def publish(self):
        if not self.checksum or self.checksum != self.hash:
            self.when_published = datetime.datetime.utcnow()
            if not self.path:
                num = 0
                entity = Post.get_by_path(path)
                while entity:
                    path = self.format_post_path(num)
                    logging.info(path)
                    entity = Post.get_by_path(path)
                    num += 1
                self.path = path
            self.content_html = self.rendered
            self.checksum = self.hash
            self.put()

    @classmethod
    def get_by_path(cls, path):
        cache_key = 'Post.' + path
        entity = dbhelper.deserialize_entities(memcache.get(cache_key))
        if not entity:
            entity = Post.all().filter('path =', path).get()
            memcache.set(cache_key, dbhelper.serialize_entities(entity))
        return entity

    @property
    def hash(self):
        return hashlib.sha1(str((self.title, self.content, self.place, self.when_published))).hexdigest()
    
    @property
    def rendered(self):
        renderer = markup.get_renderer(self.markup_type)
        return renderer(self.content)

class Feedback(SerializableModel):
    full_name = db.StringProperty()
    email = db.EmailProperty()
    subject = db.StringProperty()
    content = db.TextProperty()

class SupplierInformation(SerializableModel):
    full_name = db.StringProperty()
    designation = db.StringProperty()
    email = db.EmailProperty()
    subject = db.StringProperty()
    content = db.TextProperty()


class AdminAssetLiabilityStatement(appengine_admin.ModelAdmin):
    model = AssetLiabilityStatement
    listFields = ('start_year', 'end_year', 'share_capital', 
        'reserves_and_surplus', 'secured_loans', 'total_liabilities',
        'fixed_assets', 'investments', 'net_current_assets', 'total_assets')
    editFields = ('start_year', 'end_year', 'share_capital', 
        'reserves_and_surplus', 'secured_loans', 'total_liabilities',
        'fixed_assets', 'investments', 'net_current_assets', 'total_assets')
    readonlyFields = ('when_created', 'when_modified')

class AdminFeedback(appengine_admin.ModelAdmin):
    model = Feedback
    listFields = ('full_name', 'email', 'subject', 'content')
    editFields = ('full_name', 'email', 'subject', 'content')
    readonlyFields = ('when_created', 'when_modified')

class AdminSupplierInformation(appengine_admin.ModelAdmin):
    model = SupplierInformation
    listFields = ('full_name', 'designation', 'email', 'subject', 'content')
    editFields = ('full_name', 'designation', 'email', 'subject', 'content')
    readonlyFields = ('when_created', 'when_modified')

class AdminManager(appengine_admin.ModelAdmin):
    model = Manager
    listFields = ('full_name', 'designation', 'description')
    editFields = ('full_name', 'designation', 'description')
    readonlyFields = ('when_created', 'when_modified', 'description_html')

class AdminAnnualReport(appengine_admin.ModelAdmin):
    model = AnnualReport
    listFields = ('title', 'subtitle', 'start_year', 'end_year', 'document_url')
    editFields = ('title', 'subtitle', 'start_year', 'end_year', 'document_url')
    readonlyFields = ('when_created', 'when_modified')

class AdminVessel(appengine_admin.ModelAdmin):
    model = Vessel
    listFields = ('name', 'build_year', 'vessel_type', 'generic_type', 'yard', 
        'deadweight_in_tons', 'design', 'bp_in_tons', 'dp', 'fifi', 'company', 'when_available',
        'operational_status')
    editFields = ('name', 'build_year', 'vessel_type', 'generic_type', 'yard',  
        'deadweight_in_tons', 'design', 'bp_in_tons', 'dp', 'fifi', 'company', 'when_available',
        'operational_status')
    readonlyFields = ('when_created', 'when_modified')

appengine_admin.register(AdminFeedback, 
    AdminSupplierInformation, 
    AdminManager,
    AdminAssetLiabilityStatement,
    AdminVessel,
    AdminAnnualReport)
