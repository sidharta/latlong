from google.appengine.ext import ndb

class Local(ndb.Model):

    key = ndb.StringProperty()
    lat = ndb.FloatProperty()
    lng = ndb.FloatProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
