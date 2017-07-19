
import jinja_env
import logging
import webapp2
from models import food_log
from google.appengine.ext import ndb
from google.appengine.api import users


class GraphHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user == None:
            self.redirect("/")
        logging.info("GraphHandler")
        html_params = {
            "title": "Fresh Fit",
            "content": "",
            
        }
        template = jinja_env.env.get_template('templates/graph.html')
        self.response.out.write(template.render(html_params))
        user_query = food_log.FoodModel.query(food_log.FoodModel.user == user.email())
        user_foods = user_query.fetch()
        logging.info("Num comments "+ str(len(user_comments)))
      	#user =food_log.FoodModel.query(food_log.FoodModel.User).get()

