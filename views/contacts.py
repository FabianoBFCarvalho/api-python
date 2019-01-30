import json

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
            contact.key = contact.key.url_safe()
            contact.amount_deals = 2
            contacts.append(contact.to_dict())

        self.response_write(contacts)
        # self.response.write(json.dumps([p.to_dict() for p in Property.query(namespace='ac-abc123').fetch()]))

    # @staticmethod
    # def count_deals(contact_id):
    #     deals = Deal(namespace="ac-abc123").query(contact_id == str(contact_id))
    #     print(deals)
    #     return 2
