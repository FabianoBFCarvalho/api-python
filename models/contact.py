from google.appengine.ext import ndb
from google.appengine.api import search
from storage.bucket import Bucket


class Contact(ndb.Expando):
    db_id = ndb.StringProperty(indexed=False)
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()
    amount_deals = ndb.IntegerProperty()
    tags = ndb.StringProperty()
    image = ndb.StringProperty()
    neighborhood = ndb.StringProperty()
    bedrooms = ndb.IntegerProperty()
    bathrooms = ndb.IntegerProperty()
    vacancies = ndb.IntegerProperty()
    area = ndb.IntegerProperty()
    value = ndb.IntegerProperty()

    @staticmethod
    def prepare_contact(contact_new, contact_json):

        if contact_json.get('profile_image'):
            image_url = Bucket.upload_blob('my_bucket', 'ac-abc123/contacts/' + 'image',
                                           contact_json.get('profile_image'))
            contact_new.image = image_url

        contact_new.name = contact_json.get('name')
        contact_new.email = contact_json.get('email')
        contact_new.phone = contact_json.get('phone')
        contact_new.amount_deals = 2
        contact_new.tags = 'owner'
        contact_new.neighborhood = contact_json.get('profile')['neighborhood']
        contact_new.bedrooms = int(contact_json.get('profile')['bedrooms'])
        contact_new.vacancies = int(contact_json.get('profile')['vacancies'])
        contact_new.bathrooms = int(contact_json.get('profile')['bathrooms'])
        contact_new.area = int(contact_json.get('profile')['area'])
        contact_new.value = int(contact_json.get('profile')['value'])
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
            search.TextField(name='image', value=contact.image),
            search.TextField(name='neighborhood', value=contact.neighborhood),
            search.NumberField(name='bedrooms', value=contact.bedrooms),
            search.NumberField(name='bathrooms', value=contact.bathrooms),
            search.NumberField(name='vacancies', value=contact.vacancies),
            search.NumberField(name='area', value=contact.area),
            search.NumberField(name='value', value=contact.value),
        ]
        return fields

    @staticmethod
    def convert_index_search_in_contact(fields):
        contact = {}
        for field in fields:
            contact[field.name] = field.value
        return contact
