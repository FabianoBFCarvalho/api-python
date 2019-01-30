from google.appengine.ext import ndb


class Property(ndb.Model):
    db_id = ndb.KeyProperty()
    description = ndb.StringProperty(indexed=False)
    site = ndb.StringProperty(indexed=False)
    address = ndb.StringProperty(indexed=False)
    city = ndb.StringProperty(indexed=False)
    finality = ndb.StringProperty(indexed=False)
    value = ndb.StringProperty(indexed=False)

    @staticmethod
    def prepare_property(property_new, property_json):
        property_new.value = str(property_json.get('value'))
        property_new.site = property_json.get('site')
        property_new.city = property_json.get('city')
        property_new.finality = property_json.get('finality')
        property_new.description = property_json.get('description')
        property_new.address = property_json.get('address')
        return property_new

