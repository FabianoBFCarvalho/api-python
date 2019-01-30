import json

from controller.base_request import BaseRequest
from models.contact import Contact


class ContactHandler(BaseRequest):

    def put(self, contact_id):
        contact = Contact.get_by_id(int(contact_id), namespace='ac-abc123')
        contact_json = json.loads(self.request.body)['contact']
        Contact.prepare_contact(contact, contact_json).put()

        self.response_write('Success')

    def delete(self, contact_id):
        contact = Contact.get_by_id(int(contact_id), namespace='ac-abc123')
        contact.key.delete()
        self.response_write('Success')

