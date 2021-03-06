import webapp2

from views.contact_photo import ContactPhoto
from views.contacts import Contacts
from views.contacts_search import ContactsSearch
from views.deals import Deals
from views.properties import Properties
from views.properties_search import PropertiesSearch

app = webapp2.WSGIApplication([(r'/contacts?/?(\w*)', Contacts)])

app = webapp2.WSGIApplication([
    (r'/properties/search', PropertiesSearch),
    (r'/contacts/search', ContactsSearch),
    (r'/contacts/photo', ContactPhoto),
    (r'/properties?/?([a-zA-Z0-9_-]*)', Properties),
    (r'/contacts?/?([a-zA-Z0-9_-]*)', Contacts),
    (r'/deals?/?([a-zA-Z0-9_-]*)', Deals),
], debug=True)
# [END app]
