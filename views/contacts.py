import json
from controller.base_request import BaseRequest
from models.contact import Contact


class Contacts(BaseRequest):

    def post(self, contact_id):
        contact_json = json.loads(self.request.body)['contact']
        contact_new = Contact(namespace='ac-abc123')
        contact_key = Contact.prepare_contact(contact_new, contact_json).put()

        self.response_write({'db_id': contact_key.urlsafe()})

    def get(self, contact_id=None):
        print(contact_id)
        if contact_id:
            self.response_write(Contact.get_contact(contact_id))
        else:
            contacts = []
            for contact in Contact.query(namespace='ac-abc123').fetch():
                # self.count_deals(contact.key.id())
                contact.db_id = contact.key.urlsafe()
                contact.amount_deals = 2
                contacts.append(contact.to_dict())

            self.response_write(contacts)
            # self.response.write(json.dumps([p.to_dict() for p in Property.query(namespace='ac-abc123').fetch()]))

    def put(self, contact_id=None):
        contact_json = json.loads(self.request.body)['contact']
        contact = Contact.get_contact(contact_id)
        Contact.prepare_contact(contact, contact_json).put()

        self.response_write('Success')

    def delete(self, contact_id):
        contact = Contact.get_contact(contact_id)
        contact.key.delete()
        self.response_write('Success')

    # @staticmethod
    # def count_deals(contact_id):
    #     deals = Deal(namespace="ac-abc123").query(contact_id == str(contact_id))
    #     print(deals)
    #     return 2
