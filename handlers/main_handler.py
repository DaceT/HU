
import jinja_env
import logging
import webapp2
from google.appengine.api import users

# from [folder] immprt [file]
from models import food_log 
class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("MainHandler")
        html_params = {
            "title": "Fresh Fit",
            "html_login_url": users.create_login_url('/about'),
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))
    def post(self):
    	logging.info("There was a post.")
    	r_breakfast=self.request.get("form_breakfast")
    	r_lunch=self.request.get("form_lunch")
    	r_dinner=self.request.get("form_dinner")
    	r_brkfst_calories=float(self.request.get("brkfst_calories"))
    	r_lunch_calories=float(self.request.get("lunch_calories"))
    	r_dinner_calories=float(self.request.get("dinner_calories"))
    	r_user=self.request.get("user_name")
    	r_date=self.request.get("date")


    	logging.info("CHECK LOGGING!!!!!!!!!!!!!!!!")
    	logging.info(r_dinner_calories)


    	new_food=food_log.FoodModel(
    		Breakfast=r_breakfast,
    		Lunch=r_lunch,
    		Dinner=r_dinner,
    		BreakfastCal=r_brkfst_calories,
    		LunchCal=r_lunch_calories,
    		DinnerCal=r_dinner_calories,
    		User=r_user,
    		Date=r_date,
    		)
    	new_food.put()
    	self.redirect("/recommend")

