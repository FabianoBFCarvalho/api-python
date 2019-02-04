from google.appengine.ext import ndb
from google.appengine.api import search


class Property(ndb.Model):
    db_id = ndb.StringProperty(indexed=False)
    description = ndb.StringProperty(indexed=False)
    site = ndb.StringProperty()
    address = ndb.StringProperty()
    city = ndb.StringProperty()
    finality = ndb.StringProperty()
    neighborhood = ndb.StringProperty()
    value = ndb.IntegerProperty()
    bedrooms = ndb.IntegerProperty()
    bathrooms = ndb.IntegerProperty()
    vacancies = ndb.IntegerProperty()
    area = ndb.IntegerProperty()

    @staticmethod
    def prepare_property(property_new, property_json):
        property_new.value = int(property_json.get('value'))
        property_new.site = property_json.get('site')
        property_new.city = property_json.get('city')
        property_new.finality = property_json.get('finality')
        property_new.description = property_json.get('description')
        property_new.address = property_json.get('address')
        property_new.neighborhood = property_json.get('neighborhood')
        property_new.bedrooms = int(property_json.get('bedrooms'))
        property_new.bathrooms = int(property_json.get('bathrooms'))
        property_new.vacancies = int(property_json.get('vacancies'))
        property_new.area = int(property_json.get('area'))
        return property_new

    @staticmethod
    def make_fields_doc_index(property):
        fields = [
            search.TextField(name='site', value=property.site),
            search.TextField(name='address', value=property.address),
            search.TextField(name='city', value=property.city),
            search.TextField(name='finality', value=property.finality),
            search.TextField(name='neighborhood', value=property.neighborhood),
            search.NumberField(name='value', value=property.value),
            search.NumberField(name='bedrooms', value=property.bedrooms),
            search.NumberField(name='bathrooms', value=property.bathrooms),
            search.NumberField(name='area', value=property.area),
            search.NumberField(name='vacancies', value=property.vacancies)]
        return fields

    @staticmethod
    def get_property(property_id):
        return ndb.Key(urlsafe=property_id).get()

    @staticmethod
    def convert_index_in_property(fields):
        proeprty = {}
        for field in fields:
            proeprty[field.name] = field.value
        return proeprty
