from google.appengine.ext import ndb

class FoodModel(ndb.Model):
    Breakfast = ndb.StringProperty()
    Lunch = ndb.StringProperty()
    Dinner = ndb.StringProperty()
    BreakfastCal = ndb.FloatProperty()
    LunchCal = ndb.FloatProperty()
    DinnerCal = ndb.FloatProperty()
    User=ndb.StringProperty()
    Date=ndb.DateProperty(auto_now_add= True)
    Sex=ndb.StringProperty()