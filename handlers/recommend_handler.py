
import jinja_env
import logging
import webapp2
from models import food_log

class RecommendHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("RecommendHandler")
		html_params = {
			"title": "Fresh Fit",
			"content": ""
		}
		template = jinja_env.env.get_template('templates/recommend.html')
		self.response.out.write(template.render(html_params))
		food =food_log.FoodModel.query().get()
		totalcal=food.BreakfastCal + food.LunchCal + food.DinnerCal
		logging.info("THIS CHECKS THAT MATH IS WORKING")
		logging.info(totalcal)
		#if totalcal >= 2600 &&

	 
