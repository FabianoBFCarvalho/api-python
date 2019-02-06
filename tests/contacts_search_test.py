from google.appengine.ext import testbed
import webapp2
import webtest
import unittest
import json
from models.contact import Contact
from views.contacts_search import ContactsSearch
from google.appengine.api import search


class AppTest(unittest.TestCase):

    def setUp(self):
        app = webapp2.WSGIApplication([(r'/contacts/search', ContactsSearch)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_search_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_get(self):
        doc = search.Document(doc_id='123456', fields=[
            search.TextField(name='name', value='Fabiano'),
            search.NumberField(name='bedrooms', value=2)
        ])
        search.Index(name='contacts', namespace='ac-abc123').put(doc)
        response = self.testapp.get('/contacts/search?bedrooms_min=1')
        self.assertEqual(json.loads(response.body)['count'], 1)

    def test_get_not_found(self):
        doc = search.Document(doc_id='123456', fields=[
            search.TextField(name='name', value='Fabiano'),
            search.NumberField(name='bathrooms', value=2)
        ])
        search.Index(name='contacts', namespace='ac-abc123').put(doc)
        response = self.testapp.get('/contacts/search?bathrooms_min=3')
        self.assertEqual(json.loads(response.body)['count'], 0)
