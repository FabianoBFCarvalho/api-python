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
        app = webapp2.WSGIApplication([(r'/deals?/?([a-zA-Z0-9_-]*)', Deals)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_search_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_post(self):
        contact_key = Contact(namespace="ac-abc123", name="Fabiano").put()
        property_key = Property(namespace="ac-abc123", address="Rua Alba").put()

        params = {"deal": {"value": "45000", "title": "deal title", "contact_id": contact_key.urlsafe(),
                           "property_id": property_key.urlsafe()}}
        response = self.testapp.post_json('/deals', params)
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        contact_key = Contact(namespace="ac-abc123", name="Fabiano").put()
        property_key = Property(namespace="ac-abc123", address="Rua Alba").put()

        Deal(namespace='ac-abc123', value='500', title='deal title',
             contact_id=contact_key,
             property_id=property_key
             ).put()
        response = self.testapp.get('/deals')
        self.assertEqual(json.loads(response.body)[0]['contact']['name'], 'Fabiano')

    def test_update(self):
        deal_key = Deal(namespace='ac-abc123', value='500', title='deal title').put()
        params = {"deal": {"value": '8000', "title": "google"}}
        response = self.testapp.put_json('/deals/' + deal_key.urlsafe(), params)
        self.assertEqual(json.loads(response.body), 'Success')

    def test_delete(self):
        deal_key = Deal(namespace='ac-abc123', value='500', title='deal title').put()
        response = self.testapp.delete('/deals/' + deal_key.urlsafe())
        self.assertEqual(json.loads(response.body), 'Success')
