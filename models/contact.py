from google.appengine.ext import ndb
from google.appengine.api import search


class Contact(ndb.Model):
    db_id = ndb.StringProperty(indexed=False)
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()
    amount_deals = ndb.IntegerProperty()
    tags = ndb.StringProperty()

    @staticmethod
    def prepare_contact(contact_new, contact_json):
        contact_new.name = contact_json.get('name')
        contact_new.email = contact_json.get('email')
        contact_new.phone = contact_json.get('phone')
        contact_new.amount_deals = 2
        contact_new.tags = 'owner'
        return contact_new

    @staticmethod
    def get_contact(contact_id):
        return ndb.Key(urlsafe=contact_id).get()

    @staticmethod
    def make_fields_doc_index(contact):
        fields = [
            search.TextField(name='name', value=contact.name),
            search.TextField(name='email', value=contact.email),
            search.TextField(name='phone', value=contact.phone),
            search.TextField(name='tags', value=contact.tags),
            search.NumberField(name='amount_deals', value=contact.amount_deals)]
        return fields

    @staticmethod
    def convert_index_search_in_contact(fields):
        contact = {}
        for field in fields:
            contact[field.name] = field.value
        return contact
