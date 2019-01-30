from google.appengine.ext import ndb
from models.contact import Contact
from models.property import Property


class Deal(ndb.Model):
    db_id = ndb.StringProperty(indexed=False)
    value = ndb.StringProperty(indexed=False)
    title = ndb.StringProperty(indexed=False)
    interest = ndb.StringProperty(indexed=False)
    status = ndb.StringProperty(indexed=False)
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
