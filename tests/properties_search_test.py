from google.appengine.ext import testbed
import webapp2
import webtest
import unittest
import json
from google.appengine.api import search
from views.properties_search import PropertiesSearch


class AppTest(unittest.TestCase):

    def setUp(self):
        app = webapp2.WSGIApplication([(r'/properties/search', PropertiesSearch)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_search_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_get_found(self):
        doc = search.Document(doc_id='123456', fields=[
            search.TextField(name='address', value='Rua Bela Flor'),
            search.NumberField(name='value', value=50000)
        ])
        search.Index(name='properties', namespace='ac-abc123').put(doc)
        response = self.testapp.get('/properties/search?value_max=6000000')
        print(response)
        self.assertEqual(json.loads(response.body)['count'], 1)

    def test_get_not_found(self):
        doc = search.Document(doc_id='123456', fields=[
            search.TextField(name='address', value='Rua Bela Flor'),
            search.NumberField(name='vacancies', value=2)
        ])
        search.Index(name='properties', namespace='ac-abc123').put(doc)
        response = self.testapp.get('/properties/search?vacancies_min=3')
        self.assertEqual(json.loads(response.body)['count'], 0)
