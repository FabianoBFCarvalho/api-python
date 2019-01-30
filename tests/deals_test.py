from google.appengine.ext import testbed
import webapp2
import webtest
import unittest
import json
from models.deal import Deal
from views.deals import Deals
from models.contact import Contact
from models.property import Property


class AppTest(unittest.TestCase):

    def setUp(self):
        app = webapp2.WSGIApplication([('/deals', Deals)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_post(self):
        contact_key = Contact(namespace="ac-abc123", name="Fabiano").put()
        property_key = Property(namespace="ac-abc123", address="Rua Alba").put()

        params = {"deal": {"value": "45000", "title": "deal title", "contact_id": contact_key.urlsafe(),
                           "property_id": property_key.urlsafe()}}
        response = self.testapp.post_json('/deals', params)
        self.assertEqual(json.loads(response.body), {"db_id": 3})

    def test_get(self):
        contact_key = Contact(namespace="ac-abc123", name="Fabiano").put()
        property_key = Property(namespace="ac-abc123", address="Rua Alba").put()

        Deal(namespace='ac-abc123', value='500', title='deal title',
             contact_id=contact_key.urlsafe(),
             ).put()
        response = self.testapp.get('/deals')
        print(response)

        self.assertEqual(json.loads(response.body)[0]['contact']['name'], 'Fabiano')
