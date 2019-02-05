import json
from controller.base_request import BaseRequest
from models.contact import Contact
from google.appengine.api import search


class Contacts(BaseRequest):

    def post(self, contact_id):
        contact_json = json.loads(self.request.body)['contact']
        contact_new = Contact(namespace='ac-abc123')

        contact_key = Contact.prepare_contact(contact_new, contact_json).put()
        search.Index(name='contacts', namespace='ac-abc123')

        doc = search.Document(doc_id=contact_key.urlsafe(), fields=Contact.make_fields_doc_index(
            Contact.get_contact(contact_key.urlsafe())))

        try:
            search.Index(name='contacts', namespace='ac-abc123').put(doc)

        except search.Error:
            print(search.Error)

        self.response_write({'db_id': contact_key.urlsafe()})

    def get(self, contact_id=None):
        if contact_id:
            self.response_write(self.prepare_json_contact(Contact.get_contact(contact_id)))
        elif self.request.get('search_text'):
            self.search_get(self.request.get('search_text'))
        else:
            contacts = []
            for contact in Contact.query(namespace='ac-abc123').fetch():
                contacts.append(self.prepare_json_contact(contact))
            self.response_write(contacts)

    def put(self, contact_id=None):
        contact_json = json.loads(self.request.body)['contact']
        contact = Contact.get_contact(contact_id)
        contact_new = Contact.prepare_contact(contact, contact_json)
        contact_new.put()
        try:
            doc = search.Document(doc_id=contact_id, fields=Contact.make_fields_doc_index(contact_new))
            search.Index(name='contacts', namespace='ac-abc123').put(doc)
        except search.Error:
            pass
        self.response_write('Success')

    def delete(self, contact_id):
        contact = Contact.get_contact(contact_id)
        index = search.Index(name='contacts', namespace='ac-abc123')
        index.delete(contact_id)
        contact.key.delete()
        self.response_write('Success')

    def search_get(self, search_text):
        contacts = []
        querystring = search_text
        try:
            index = search.Index(name='contacts', namespace='ac-abc123')
            search_query = search.Query(
                query_string=querystring,
                options=search.QueryOptions(
                    limit=10))
            search_results = index.search(search_query)
            for doc in search_results:
                contacts.append(Contact.convert_index_search_in_contact(doc.fields))
            self.response_write(contacts)
        except search.Error:
            print(search.Error)

    @staticmethod
    def prepare_json_contact(contact):
        contact_json = {
            'db_id': contact.key.urlsafe(),
            'amount_deals': 2,
            'tags': 'Owner',
            'name': contact.name,
            'email': contact.email,
            'phone': contact.phone,
            'profile': {
                'neighborhood': contact.neighborhood,
                'value': contact.value,
                'vacancies': contact.vacancies,
                'bedrooms': contact.bedrooms,
                'bathrooms': contact.bathrooms,
                'area': contact.area
            }
        }
        return contact_json
