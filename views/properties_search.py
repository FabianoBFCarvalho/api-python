import json

from controller.base_request import BaseRequest
from models.property import Property
from google.appengine.api import search


class PropertiesSearch(BaseRequest):

    def get(self):
        properties = []
        querystring = self.prepare_query()
        print('**************************************************************************')
        print(querystring)
        index = search.Index(name='properties', namespace='ac-abc123')
        search_query = search.Query(
            query_string=querystring,
            options=search.QueryOptions(
                limit=10))
        try:

            search_results = index.search(search_query)
            for doc in search_results:
                properties.append(Property.convert_index_in_property(doc.fields))

            response = {
                "properties": properties,
                "count": search_results.number_found
            }
            self.response_write(response)
        except search.Error:
            print(search.Error)

    def prepare_query(self):
        query = ""
        if self.request.get('bedrooms'):
            query += "bedrooms="+self.request.get('bedrooms') + " AND "
        if self.request.get('bathrooms'):
            query += "bathrooms=" + self.request.get('bathrooms') + " AND "
        if self.request.get('vacancies'):
            query += "vacancies=" + self.request.get('vacancies') + " AND "
        if self.request.get('area'):
            query += "area=" + self.request.get('area') + " AND "
        if self.request.get('neighborhood'):
            query += "neighborhood=" + self.request.get('neighborhood') + " AND "
        if self.request.get('value'):
            query += "value=" + self.request.get('value')

        return query
