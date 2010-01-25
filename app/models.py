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
from dbhelper import CACHE_DURATION, MAX_COUNT, SerializableModel, deserialize_entities, serialize_entities
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

render_markup = markup.render_markdown

VESSEL_STATUS_OPERATIONAL = 'operational'
VESSEL_STATUS_UNDER_CONSTRUCTION = 'under_construction'
VESSEL_STATUS_CHOICES = (
    VESSEL_STATUS_OPERATIONAL,
    VESSEL_STATUS_UNDER_CONSTRUCTION,
    )

VESSEL_GENERIC_TYPE_RIG = 'rig'
VESSEL_GENERIC_TYPE_VESSEL = 'vessel'
VESSEL_GENERIC_TYPE_CHOICES = (
    VESSEL_GENERIC_TYPE_RIG,
    VESSEL_GENERIC_TYPE_VESSEL,
    )

class Manager(SerializableModel):
    full_name = db.StringProperty()
    designation = db.StringProperty()
    description = db.TextProperty()
    description_html = TransformProperty(description, render_markup)
    photo_url = db.URLProperty()

class AssetLiabilityStatement(SerializableModel):
    start_year = db.StringProperty()
    end_year = db.StringProperty()
    share_capital = db.StringProperty()
    reserves_and_surplus = db.StringProperty()
    secured_loans = db.StringProperty()
    total_liabilities = db.StringProperty()
    fixed_assets = db.StringProperty()
    investments = db.StringProperty()
    net_current_assets = db.StringProperty()
    total_assets = db.StringProperty()

class IncomeStatement(SerializableModel):
    start_year = db.StringProperty()
    end_year = db.StringProperty()
    total_revenue = db.StringProperty()
    pbdit = db.StringProperty()
    depreciation = db.StringProperty()
    interest = db.StringProperty()
    tax_provision = db.StringProperty()
    pat = db.StringProperty()
    eps = db.StringProperty()


class VesselType(SerializableModel):
    vessel_type_name = db.StringProperty()
    vessel_type_shortname = db.StringProperty()
    
    def __str__(self):
        return self.vessel_type_name
    
    def __unicode__(self):
        return self.__str__()

class Vessel(SerializableModel):
    name = db.StringProperty()
    built = db.StringProperty()
    vessel_type = db.ReferenceProperty(VesselType, collection_name='vessels')
    yard = db.StringProperty()
    deadweight_in_tons = db.StringProperty()
    design = db.StringProperty()
    bp_in_tons = db.StringProperty()
    dp = db.StringProperty()
    fifi = db.StringProperty()
    company = db.StringProperty()
    when_available = db.DateProperty()
    specification_url = db.URLProperty()
    
    # Delivery status
    is_delivered = db.BooleanProperty(default=False)
    when_delivered = db.DateProperty()
    when_expected = db.StringProperty()
    
    # Classification in table.
    operational_status = db.StringProperty(choices=VESSEL_STATUS_CHOICES)
    generic_type = db.StringProperty(choices=VESSEL_GENERIC_TYPE_CHOICES)

    @classmethod
    def get_operating_vessels(cls):
        cache_key = 'Vessel.get_operating_vessels()'
        entities = deserialize_entities(memcache.get(cache_key))
        if not entities:
            entities = Vessel.all() \
                .filter('operational_status = ', VESSEL_STATUS_OPERATIONAL) \
                .filter('generic_type = ', VESSEL_GENERIC_TYPE_VESSEL) \
                .fetch(MAX_COUNT)
            memcache.set(cache_key, serialize_entities(entities), CACHE_DURATION)
        return entities

    @classmethod
    def get_operating_rigs(cls):
        cache_key = 'Vessel.get_operating_rigs()'
        entities = deserialize_entities(memcache.get(cache_key))
        if not entities:
            entities = Vessel.all() \
                .filter('operational_status = ', VESSEL_STATUS_OPERATIONAL) \
                .filter('generic_type = ', VESSEL_GENERIC_TYPE_RIG) \
                .fetch(MAX_COUNT)
            memcache.set(cache_key, serialize_entities(entities), CACHE_DURATION)
        return entities
        
    @classmethod
    def get_under_construction_vessels(cls):
        cache_key = 'Vessel.get_under_construction_vessels()'
        entities = deserialize_entities(memcache.get(cache_key))
        if not entities:
            entities = Vessel.all() \
                .filter('operational_status = ', VESSEL_STATUS_UNDER_CONSTRUCTION) \
                .fetch(MAX_COUNT)
            memcache.set(cache_key, serialize_entities(entities), CACHE_DURATION)
        return entities


class AnnualReport(SerializableModel):
    title = db.StringProperty()
    subtitle = db.StringProperty()
    start_year = db.StringProperty()
    end_year = db.StringProperty()
    document_url = db.URLProperty()

class LegalTerms(SerializableModel):
    title = db.StringProperty()
    short_name = db.StringProperty()
    slug = TransformProperty(short_name, utils.slugify)
    content = db.TextProperty(required=True)
    #content_html = TransformProperty(content, render_markup)
    content_html = db.TextProperty()
    
    @classmethod
    def get_by_slug(cls, slug):
        cache_key = 'LegalTerms.get_by_slug(%s)' % slug
        entity = deserialize_entities(memcache.get(cache_key))
        if not entity:
            entity = LegalTerms.all().filter('slug =', slug).get()
            memcache.set(cache_key, serialize_entities(entity), CACHE_DURATION)
        return entity
    
    def put(self):
        self.content_html = render_markup(self.content)
        super(LegalTerms, self).put()


class BoardDirector(SerializableModel):
    full_name = db.StringProperty()
    designation = db.StringProperty()

class SeniorManagement(SerializableModel):
    full_name = db.StringProperty()
    designation = db.StringProperty()
    
class Auditor(SerializableModel):
    full_name = db.StringProperty()
    designation = db.StringProperty()
    
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
    website_url = db.URLProperty()
    subject = db.StringProperty()
    content = db.TextProperty()

class FleetSearchTerms(SerializableModel):
    search_terms = db.StringProperty()
    remote_addr = db.StringProperty()
    user_agent = db.StringProperty()

class AdminAssetLiabilityStatement(appengine_admin.ModelAdmin):
    model = AssetLiabilityStatement
    listFields = ('start_year', 'end_year', 'share_capital', 
        'reserves_and_surplus', 'secured_loans', 'total_liabilities',
        'fixed_assets', 'investments', 'net_current_assets', 'total_assets')
    editFields = ('start_year', 'end_year', 'share_capital', 
        'reserves_and_surplus', 'secured_loans', 'total_liabilities',
        'fixed_assets', 'investments', 'net_current_assets', 'total_assets')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by end_year desc'

class AdminIncomeStatement(appengine_admin.ModelAdmin):
    model = IncomeStatement
    listFields = ('start_year', 'end_year', 'total_revenue', 
        'pbdit', 'depreciation', 'interest',
        'tax_provision', 'pat', 'eps')
    editFields = ('start_year', 'end_year', 'total_revenue', 
        'pbdit', 'depreciation', 'interest',
        'tax_provision', 'pat', 'eps')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by end_year desc'

class AdminFeedback(appengine_admin.ModelAdmin):
    model = Feedback
    listFields = ('full_name', 'email', 'subject', 'content')
    editFields = ('full_name', 'email', 'subject', 'content')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by when_created desc'

class AdminSupplierInformation(appengine_admin.ModelAdmin):
    model = SupplierInformation
    listFields = ('full_name', 'designation', 'website_url', 'email', 'subject', 'content')
    editFields = ('full_name', 'designation', 'website_url', 'email', 'subject', 'content')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by when_created desc'

class AdminManager(appengine_admin.ModelAdmin):
    model = Manager
    listFields = ('full_name', 'designation', 'description', 'photo_url')
    editFields = ('full_name', 'designation', 'description', 'photo_url')
    readonlyFields = ('when_created', 'when_modified', 'description_html')
    listGql = 'order by full_name asc'

class AdminBoardDirector(appengine_admin.ModelAdmin):
    model = BoardDirector
    listFields = ('full_name', 'designation')
    editFields = ('full_name', 'designation')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by full_name asc'

class AdminSeniorManagement(appengine_admin.ModelAdmin):
    model = SeniorManagement
    listFields = ('full_name', 'designation')
    editFields = ('full_name', 'designation')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by full_name asc'

class AdminAuditor(appengine_admin.ModelAdmin):
    model = Auditor
    listFields = ('full_name', 'designation')
    editFields = ('full_name', 'designation')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by full_name asc'

class AdminLegalTerms(appengine_admin.ModelAdmin):
    model = LegalTerms
    listFields = ('title', 'short_name', 'slug', 'content')
    editFields = ('title', 'short_name', 'content')
    readonlyFields = ('slug', 'when_created', 'when_modified', 'content_html')
    listGql = 'order by slug asc'

class AdminAnnualReport(appengine_admin.ModelAdmin):
    model = AnnualReport
    listFields = ('title', 'subtitle', 'start_year', 'end_year', 'document_url')
    editFields = ('title', 'subtitle', 'start_year', 'end_year', 'document_url')
    readonlyFields = ('when_created', 'when_modified')
    listGql = 'order by end_year desc'

class AdminVesselType(appengine_admin.ModelAdmin):
    model = VesselType
    listFields = ('vessel_type_shortname', 'vessel_type_name',)
    editFields = ('vessel_type_shortname', 'vessel_type_name',)
    readonlyFields = ('vessels', 'when_created', 'when_modified')

class AdminVessel(appengine_admin.ModelAdmin):
    model = Vessel
    listFields = ('name', 'built', 'vessel_type', 'generic_type', 'yard',
        'deadweight_in_tons', 'design', 'bp_in_tons', 'dp', 'fifi', 'company', 'when_available',
        'operational_status', 'is_delivered', 'when_delivered', 'when_expected')
    editFields = ('name', 'built', 'vessel_type', 'generic_type', 'yard', 'specification_url',
        'deadweight_in_tons', 'design', 'bp_in_tons', 'dp', 'fifi', 'company', 'when_available',
        'operational_status', 'is_delivered', 'when_delivered', 'when_expected')
    readonlyFields = ('when_created', 'when_modified')

class AdminFleetSearchTerms(appengine_admin.ModelAdmin):
    model = FleetSearchTerms
    listFields = ('search_terms', 'remote_addr', 'user_agent', 'when_created')
    editFields = ()
    readonlyFields = ('search_terms', 'remote_addr', 'user_agent', 'when_created', 'when_modified')
    listGql = 'order by when_created desc'

appengine_admin.register(AdminFeedback, 
    AdminSupplierInformation, 
    AdminManager,
    AdminAssetLiabilityStatement,
    AdminIncomeStatement,
    AdminVessel,
    AdminAnnualReport,
    AdminLegalTerms,
    AdminVesselType,
    AdminBoardDirector,
    AdminSeniorManagement,
    AdminAuditor)
