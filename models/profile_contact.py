from google.appengine.ext import ndb


class ProfileContact(ndb.Model):
    image = ndb.StringProperty()
    neighborhood = ndb.StringProperty()
    bedrooms = ndb.IntegerProperty()
    bathrooms = ndb.IntegerProperty()
    vacancies = ndb.IntegerProperty()
    area = ndb.IntegerProperty()
    value = ndb.IntegerProperty()
