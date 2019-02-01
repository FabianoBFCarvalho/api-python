from google.appengine.ext import ndb


class Contact(ndb.Model):
    db_id = ndb.StringProperty(indexed=False)
    name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    phone = ndb.StringProperty(indexed=False)
    amount_deals = ndb.IntegerProperty(indexed=False)
    tags = ndb.StringProperty(indexed=False)

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
