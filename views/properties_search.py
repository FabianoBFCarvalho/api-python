import json

from controller.base_request import BaseRequest
from models.property import Property
from google.appengine.api import search


class PropertiesSearch(BaseRequest):

    def get(self):
        properties = []
        querystring = self.prepare_query_profile()
        index = search.Index(name='properties', namespace='ac-abc123')
        search_query = search.Query(
            query_string=querystring,
            options=search.QueryOptions(
                limit=10))
        try:
            search_results = index.search(search_query)
            for doc in search_results:
                property = Property.convert_index_in_property(doc.fields)
                property['db_id'] = doc.doc_id
                properties.append(property)

            response = {
                "properties": properties,
                "count": search_results.number_found
            }
            self.response_write(response)
        except search.Error:
            print(search.Error)
