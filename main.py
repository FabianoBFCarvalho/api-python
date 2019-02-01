

import webapp2

from views.contacts import Contacts
from views.deals import Deals
from views.properties import Properties

# [START app]
app = webapp2.WSGIApplication([(r'/contacts?/?(\w*)', Contacts)])

app = webapp2.WSGIApplication([
    (r'/properties?/?([a-zA-Z0-9_-]*)', Properties),
    (r'/contacts?/?([a-zA-Z0-9_-]*)', Contacts),
    (r'/deals?/?([a-zA-Z0-9_-]*)', Deals),
], debug=True)
# [END app]
