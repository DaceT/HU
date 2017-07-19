

import jinja_env
import logging
import webapp2
from models import food_log
from google.appengine.ext import ndb
from google.appengine.api import users

class RecommendHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("RecommendHandler")
		html_params = {
			"title": "Fresh Fit",
			"content": "",
			}
		template = jinja_env.env.get_template('templates/recommend.html')
		self.response.out.write(template.render(html_params))
		food =food_log.FoodModel.query().get()
		totalcal=food.BreakfastCal + food.LunchCal + food.DinnerCal
		logging.info("THIS CHECKS THAT MATH IS WORKING")
		logging.info(totalcal)

		if totalcal <= 2600:
			html_params ["imageurl"]= "https://static1.squarespace.com/static/503264b0e4b0dbdecd41e3f6/t/590a05131e5b6ce08768b593/1493828890055/polaroid2.png"
		if 2600 > totalcal < 3000:
			html_params ["imageurl"]= "https://s-media-cache-ak0.pinimg.com/originals/44/9e/10/449e10c78b919db9e9d7606c877e80ee.jpg"
		if totalcal <= 3000:
			html_params ["imageurl"] = "https://www.healthykids.nsw.gov.au/downloads/header/header_SR_SoccerKick_cb97_header.jpg"
		

	 
