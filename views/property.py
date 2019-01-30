import json

from controller.base_request import BaseRequest
from models.property import Property


class PropertyHandler(BaseRequest):

    def put(self, property_id):
        property = Property.get_by_id(int(property_id), namespace='ac-abc123')
        property_json = json.loads(self.request.body)['property']
        Property.prepare_property(property, property_json).put()

        self.response_write('Success')

    def delete(self, property_id):
        property = Property.get_by_id(int(property_id), namespace='ac-abc123')
        property.key.delete()
        self.response_write('Success')

