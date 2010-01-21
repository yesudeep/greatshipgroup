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
from haggoo.db.properties import DecimalProperty
from dbhelper import SerializableModel
from aetycoon import TransformProperty

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

SUBSIDIARY_CHOICES = (
    'gges',
    'gil',
    'ggos',
    )

class Manager(SerializableModel):
    full_name = db.StringProperty()
    designation = db.StringProperty()
    description = db.TextProperty()
    description_html = db.TextProperty()
    
class AssetLiabilityStatement(SerializableModel):
    start_year = db.IntegerProperty()
    end_year = db.IntegerProperty()
    share_capital = DecimalProperty()
    reserves_and_surplus = DecimalProperty()
    secured_loans = DecimalProperty()
    total_liabilities = DecimalProperty()
    fixed_assets = DecimalProperty()
    investments = DecimalProperty()
    net_current_assets = DecimalProperty()
    total_assets = DecimalProperty()

class IncomeStatement(SerializableModel):
    start_year = db.IntegerProperty()
    end_year = db.IntegerProperty()
    total_revenue = DecimalProperty()
    pbdit = DecimalProperty()
    depreciation = DecimalProperty()
    interest = DecimalProperty()
    tax_provision = DecimalProperty()
    pat = DecimalProperty()
    eps = DecimalProperty()

class Vessel(SerializableModel):
    name = db.StringProperty()
    build_year = db.IntegerProperty()
    vessel_type = db.StringProperty(choices=VESSEL_TYPE_CHOICES)
    yard = db.StringProperty()
    deadweight_in_tons = DecimalProperty()
    design = db.StringProperty()
    bp_in_tons = DecimalProperty()
    dp = db.StringProperty()
    fifi = db.StringProperty()
    company = db.StringProperty(choices=SUBSIDIARY_CHOICES)
    when_available = db.DateProperty()
    
    # Classification in table.
    operational_status = db.StringProperty(choices=VESSEL_STATUS_CHOICES)
    generic_type = db.StringProperty(choices=VESSEL_GENERIC_TYPE_CHOICES)
    
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
