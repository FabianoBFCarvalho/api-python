from google.appengine.ext import testbed
import webapp2
import webtest
import unittest
import json
from views.properties import Properties
from models.property import Property


class AppTest(unittest.TestCase):

    def setUp(self):
        app = webapp2.WSGIApplication([(r'/properties?/?([a-zA-Z0-9_-]*)', Properties)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_search_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_post(self):
        params = {"property": {"address": "Rua Bonfim", "city": "Sergipe", "finality": "Residential",
                               "value": "34", "site": "google.com", "description": "Casa",
                               'bedrooms': '1', 'bathrooms': '1', 'vacancies': '1',
                               'area': '1'
        }}
        response = self.testapp.post_json('/properties', params)
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        Property(namespace="ac-abc123", address="Rua alba", city="Santos").put()
        response = self.testapp.get('/properties/')
        self.assertEqual(json.loads(response.body)[0].get('address'), 'Rua alba')

    def test_get_one(self):
        property_key = Property(namespace="ac-abc123", address="Av Buenos Aires", city="Santos").put()
        response = self.testapp.get('/properties/'+property_key.urlsafe())
        self.assertEqual(json.loads(response.body).get('address'), 'Av Buenos Aires')

    def test_update(self):
        property_key = Property(namespace="ac-abc123", address="Av 2", city="Santos").put()
        params = {"property": {"address": 'Rua do Tatu', "city": "Rio de Janeiro", "value": "34",
                               "site": "google.com", "description": "Aeee",
                               'bedrooms': '1', 'bathrooms': '1', 'vacancies': '1',
                               'area': '1'}}
        response = self.testapp.put_json('/properties/' + property_key.urlsafe(), params)
        self.assertEqual(json.loads(response.body), 'Success')

    def test_delete(self):
        property_key = Property(namespace="ac-abc123", address="Av 2", city="Santos").put()
        response = self.testapp.delete('/properties/' + property_key.urlsafe())
        self.assertEqual(json.loads(response.body), 'Success')
