from google.appengine.ext import testbed
import webapp2
import webtest
import unittest
import json
from views.property import PropertyHandler
from models.property import Property


class AppTest(unittest.TestCase):

    def setUp(self):
        app = webapp2.WSGIApplication([('/property/<property_id>', PropertyHandler)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()
    #
    # def test_post(self):
    #
    #     property_key = Property(namespace='ac-abc123', address="Rua Alba", city="Santos").put()
    #     url = '/property/' + str(property_key.id())
    #     params = {"property": {"address": "Rua Garcia", "city": "Sao Paulo", "finality": "das",
    #                            "value": "34", "site": "dsf", "description": "fds"}}
    #     response = self.testapp.post_json(url, params)
    #     print(response)
    #     self.assertEqual(json.loads(response.body), {"db_id": 1})

