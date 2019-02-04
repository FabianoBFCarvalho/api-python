from google.appengine.ext import ndb
from models.contact import Contact
from models.property import Property
from google.appengine.api import search


class Deal(ndb.Model):
    db_id = ndb.StringProperty(indexed=False)
    value = ndb.StringProperty()
    title = ndb.StringProperty()
    interest = ndb.StringProperty()
    status = ndb.StringProperty()
    contact_id = ndb.KeyProperty(kind=Contact)
    property_id = ndb.KeyProperty(kind=Property)

    @staticmethod
    def prepare_deal(deal_new, deal_json):

        deal_new.value = deal_json.get('value')
        deal_new.title = deal_json.get('title')
        deal_new.interest = deal_json.get('interest')
        deal_new.status = deal_json.get('status')
        deal_new.contact_id = ndb.Key(urlsafe=deal_json.get('contact_id'))
        deal_new.property_id = ndb.Key(urlsafe=deal_json.get('property_id'))

        return deal_new

    @staticmethod
    def make_fields_doc_index(deal):
        fields = [
            search.TextField(name='title', value=deal.title),
            search.TextField(name='interest', value=deal.interest),
            search.TextField(name='status', value=deal.status),
            
            search.TextField(name='tags', value=deal.tags),
            search.NumberField(name='value', value=deal.value)]
        return fields

    @staticmethod
    def get_deal(deal_id):
        return ndb.Key(urlsafe=deal_id).get()
