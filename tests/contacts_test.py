from google.appengine.ext import testbed
import webapp2
import webtest
import unittest
import json
from models.contact import Contact
from views.contacts import Contacts


class AppTest(unittest.TestCase):

    def setUp(self):
        app = webapp2.WSGIApplication([('/contacts', Contacts)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_post(self):
        params = {"contact": {"name": "Fabiano", "email": "google.com"}}
        response = self.testapp.post_json('/contacts', params)
        self.assertEqual(json.loads(response.body), {"db_id": 1})

    def test_get(self):
        Contact(namespace="ac-abc123", name="Fabiano").put()
        response = self.testapp.get('/contacts')
        self.assertEqual(json.loads(response.body)[0].get('name'), 'Fabiano')
