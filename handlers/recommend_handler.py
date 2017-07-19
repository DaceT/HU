

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
			"html":"",
			"": "",
			"": "",
		}
		template = jinja_env.env.get_template('templates/recommend.html')
		self.response.out.write(template.render(html_params))
		food =food_log.FoodModel.query().get()
		totalcal=food.BreakfastCal + food.LunchCal + food.DinnerCal
		logging.info("THIS CHECKS THAT MATH IS WORKING")
		logging.info(totalcal)

		if totalcal <= 2600:
			<img src = {{ }}>

		if 2600 > totalcal < 3000:
			<img src = "https://s-media-cache-ak0.pinimg.com/originals/44/9e/10/449e10c78b919db9e9d7606c877e80ee.jpg">


		if totalcal <= 3000:
			<img src = "https://www.healthykids.nsw.gov.au/downloads/header/header_SR_SoccerKick_cb97_header.jpg">
		

	 
