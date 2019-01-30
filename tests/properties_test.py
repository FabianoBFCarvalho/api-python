from google.appengine.ext import testbed
import webapp2
import webtest
import unittest
import json
from views.properties import Properties
from models.property import Property


class AppTest(unittest.TestCase):

    def setUp(self):
        app = webapp2.WSGIApplication([('/properties/', Properties)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def testPost(self):
        params = {"property": {"address": "asd", "city": "asd", "finality": "das",
                               "value": "34", "site": "dsf", "description": "fds"}}
        response = self.testapp.post_json('/properties/', params)
        self.assertEqual(json.loads(response.body), {"db_id": 1})

    def testGet(self):
        Property(namespace="ac-abc123", address="Rua alba", city="Santos").put()

        response = self.testapp.get('/properties/')
        self.assertEqual(json.loads(response.body)[0].get('address'), 'Rua alba')
