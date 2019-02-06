import json

from controller.base_request import BaseRequest
from models.deal import Deal


class Deals(BaseRequest):

    def post(self, deal_id):
        deal_json = json.loads(self.request.body)['deal']
        deal_new = Deal(namespace='ac-abc123')
        deal_key = Deal.prepare_deal(deal_new, deal_json).put()

        self.response_write({'db_id': deal_key.urlsafe()})

    def get(self, deal_id=None):
        if deal_id:
            self.response_write(Deal.get_deal(deal_id))
        else:
            deals = []
            for deal in Deal.query(namespace='ac-abc123').fetch():
                contact_response = self.prepare_contact(deal.contact_id)
                property_response = self.prepare_property(deal.property_id)
                deal_json = {
                    'db_id': deal.key.urlsafe(),
                    'value': deal.value,
                    'interest': deal.interest,
                    'title': deal.title,
                    'status': deal.status,
                }
                if contact_response:
                    deal_json['contact'] = {'db_id': deal.contact_id.urlsafe(), 'name': contact_response.name}

                if property_response:
                    deal_json['property'] = {'db_id': deal.property_id.urlsafe(), 'address': property_response.address}

                deals.append(deal_json)
            self.response_write(deals)

    def put(self, deal_id):
        deal = Deal.get_deal(deal_id)
        deal_json = json.loads(self.request.body)['deal']
        Deal.prepare_deal(deal, deal_json).put()
        self.response_write('Success')

    def delete(self, deal_id):
        deal = Deal.get_deal(deal_id)
        deal.key.delete()
        self.response_write('Success')

    @staticmethod
    def prepare_contact(contact_key):
        if contact_key:
            return contact_key.get()
        else:
            return False

    @staticmethod
    def prepare_property(property_key):
        if property_key:
            return property_key.get()
        else:
            return False
