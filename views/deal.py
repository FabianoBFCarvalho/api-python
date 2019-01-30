import json

from controller.base_request import BaseRequest
from models.deal import Deal


class DealHandler(BaseRequest):

    def put(self, deal_id):
        deal = Deal.get_by_id(int(deal_id), namespace='ac-abc123')
        deal_json = json.loads(self.request.body)['deal']
        Deal.prepare_deal(deal, deal_json).put()

        self.response_write('Success')

    def delete(self, deal_id):
        deal = Deal.get_by_id(int(deal_id), namespace='ac-abc123')
        deal.key.delete()
        self.response_write('Success')

