import json

from controller.base_request import BaseRequest
from models.property import Property


class Properties(BaseRequest):

    def post(self, property_id):
        property_json = json.loads(self.request.body)['property']
        property_new = Property(namespace='ac-abc123')
        property_key = Property.prepare_property(property_new, property_json).put()

        self.response_write({'db_id': property_key.urlsafe()})

    def get(self, property_id):
        if property_id:
            self.response_write(Property.prepare_property(property_id))
        properties = []
        for prop in Property.query(namespace='ac-abc123').fetch():
            prop.db_id = prop.key.urlsafe()
            properties.append(prop.to_dict())

        self.response_write(properties)
        # self.response.write(json.dumps([p.to_dict() for p in Property.query(namespace='ac-abc123').fetch()]))

    def put(self, property_id):
        property = Property.get_property(property_id)
        property_json = json.loads(self.request.body)['property']
        Property.prepare_property(property, property_json).put()

        self.response_write('Success')

    def delete(self, property_id):
        property = Property.prepare_property(property_id)
        property.key.delete()
        self.response_write('Success')
