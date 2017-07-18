
import jinja_env
import logging
import webapp2

# from [folder] immprt [file]
from models import food_log 
class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("MainHandler")
        html_params = {
            "title": "Fresh Fit",
            "content": ""
        }
        template = jinja_env.env.get_template('templates/tmpl.html')
        self.response.out.write(template.render(html_params))
    def post(self):
    	logging.info("There was a post.")
    	r_breakfast=self.request.get("form_breakfast")
    	r_lunch=self.request.get("form_lunch")
    	r_dinner=self.request.get("form_dinner")
    	r_brkfst_calories=self.request.get("brkfst_calories")
    	r_lunch_calories=self.request.get("lunch_calories")
    	r_dinner_calories=self.request.get("dinner_calories")

    	new_food=food_log.FoodModel(
    		Breakfast=r_breakfast,
    		Lunch=r_lunch,
    		Dinner=r_dinner,
    		BreakfastCal=r_brkfst_calories,
    		LunchCal=r_breakfast,
    		DinnerCal=r_lunch,


    		)
    	new_food.put()
    	self.redirect("/recommend")
