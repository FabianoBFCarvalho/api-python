import webapp2
import json


class BaseRequest(webapp2.RequestHandler):

    def options(self, *args, **kwargs):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Access-Control-Allow-Origin'] = self.request.headers['Origin']
        self.response.headers['Access-Control-Allow-Headers'] = ('Origin, X-Requested-With, '
                                                                 'x-http-method-override, '
                                                                 'Content-Type, Accept, '
                                                                 'authorization')
        self.response.headers['Access-Control-Allow-Methods'] = ('DELETE, GET, HEAD, OPTIONS, '
                                                                 'PATCH, POST, PUT')
        self.response.headers['Access-Control-Allow-Credentials'] = 'true'
        self.response.headers['Access-Control-Max-Age'] = '600'

    def response_write(self, response):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(response))

    def prepare_query_profile(self):
        query = ""
        if self.request.get('bedrooms_min'):
            query += "bedrooms>="+self.request.get('bedrooms_min') + " AND "
        if self.request.get('bedrooms_max'):
            query += "bedrooms<="+self.request.get('bedrooms_max') + " AND "
        if self.request.get('bathrooms_min'):
            query += "bathrooms>=" + self.request.get('bathrooms_min') + " AND "
        if self.request.get('bathrooms_max'):
            query += "bathrooms<=" + self.request.get('bathrooms_max') + " AND "
        if self.request.get('vacancies_min'):
            query += "vacancies>=" + self.request.get('vacancies_min') + " AND "
        if self.request.get('vacancies_max'):
            query += "vacancies<=" + self.request.get('vacancies_max') + " AND "
        if self.request.get('area_min'):
            query += "area>=" + self.request.get('area_min') + " AND "
        if self.request.get('area_max'):
            query += "area<=" + self.request.get('area_max') + " AND "
        if self.request.get('value_min'):
            query += "value>=" + self.request.get('value_min') + " AND "
        if self.request.get('value_max'):
            query += "value<=" + self.request.get('value_max') + " AND "
        if self.request.get('neighborhood'):
            query += "neighborhood=" + self.request.get('neighborhood') + " AND "

        print(query)
        return query[:len(query)-5]
