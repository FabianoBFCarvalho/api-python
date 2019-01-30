import json
from google.appengine.ext import ndb

from controller.base_request import BaseRequest
from models.contact import Contact
from models.deal import Deal


class Contacts(BaseRequest):

    def post(self):
        contact_json = json.loads(self.request.body)['contact']
        contact_new = Contact(namespace='ac-abc123')
        contact_key = Contact.prepare_contact(contact_new, contact_json).put()

        self.response_write({'db_id': contact_key.id()})

    def get(self):
        contacts = []

        for contact in Contact.query(namespace='ac-abc123').fetch():
            # self.count_deals(contact.key.id())
            contact.db_id = contact.key.urlsafe()
            contact.amount_deals = 2
            contacts.append(contact.to_dict())

        self.response_write(contacts)
        # self.response.write(json.dumps([p.to_dict() for p in Property.query(namespace='ac-abc123').fetch()]))

    def put(self, contact_id):
        contact = ndb.Key(urlsafe=contact_id).get()
        contact_json = json.loads(self.request.body)['contact']
        Contact.prepare_contact(contact, contact_json).put()

        self.response_write('Success')

    def delete(self, contact_id):
        contact = ndb.Key(urlsafe=contact_id).get()
        contact.key.delete()
        self.response_write('Success')

    # @staticmethod
    # def count_deals(contact_id):
    #     deals = Deal(namespace="ac-abc123").query(contact_id == str(contact_id))
    #     print(deals)
    #     return 2
