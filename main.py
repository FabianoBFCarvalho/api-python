

import webapp2

from views.contact import ContactHandler
from views.contacts import Contacts
from views.deal import DealHandler
from views.deals import Deals
from views.properties import Properties
from views.property import PropertyHandler

# [START app]
app = webapp2.WSGIApplication([
    webapp2.Route('/property/<property_id>', PropertyHandler),
    webapp2.Route('/properties', Properties, name='bank'),
    webapp2.Route(r'/contacts', Contacts),
    webapp2.Route('/contacts/<contact_id>', Contacts),
    webapp2.Route('/deals', Deals),
    webapp2.Route('/deal/<deal_id>', DealHandler),

], debug=True)
# [END app]
