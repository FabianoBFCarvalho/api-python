import json

from controller.base_request import BaseRequest
from models.contact import Contact
from models.deal import Deal
from models.property import Property

class Deals(BaseRequest):

    def post(self):
        deal_json = json.loads(self.request.body)['deal']
        deal_new = Deal(namespace='ac-abc123')
        deal_key = Deal.prepare_deal(deal_new, deal_json).put()

        self.response_write({'db_id': deal_key.id()})

    def get(self, ):
        deals = []
        for deal in Deal.query(namespace='ac-abc123').fetch():
            contact_response = self.prepare_contact(deal.contact_id)
            property_response = self.prepare_property(deal.property_id)
            deal_json = {
                'db_id': deal.key.id(),
                'value': deal.value,
                'interest': deal.interest,
                'title': deal.title,
                'status': deal.status,
            }
            if contact_response:
                deal_json['contact'] = {'db_id': deal.contact_id, 'name': contact_response.name}

            if property_response:
                deal_json['property'] = {'db_id': deal.property_id, 'address': property_response.address}

            deals.append(deal_json)

        self.response_write(deals)
        # self.response.write(json.dumps([p.to_dict() for p in Property.query(namespace='ac-abc123').fetch()]))

    @staticmethod
    def prepare_contact(contact_key):
        print(contact_key)
        if contact_key:
            return contact_key.get()
        else:
            return False


    @staticmethod
    def prepare_property(property_id):
        if property_id:
            return property_id.get()
        else:
            return False
