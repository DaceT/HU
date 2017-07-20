

import jinja_env
import logging
import webapp2
from models import food_log
from google.appengine.ext import ndb
from google.appengine.api import users

class RecommendHandler(webapp2.RequestHandler):
	def get(self):
		r_b_cal=self.request.get("brkfst_calories")
		r_l_cal=self.request.get("lunch_calories")
		r_d_cal=self.request.get("dinner_calories")
		if r_b_cal == "":
			self.redirect("/") 
			return

		totalCal =float(r_b_cal) + float(r_l_cal) + float(r_d_cal)
		logging.info(totalCal)
		logging.info("RecommendHandler")
		html_params = {
			"title": "Fresh Fit",
			"content": "",
			"totalCal":totalCal
			}
		template = jinja_env.env.get_template('templates/recommend.html')

		if totalCal <= 2600:
			html_params ["imageurl"]= "http://hipnewjersey.com/wp-content/uploads/2017/06/istock-499609170-1.jpg"
			html_params["suggestions"]="You are eating enough calories in a day. Just make sure that they are healthy calories from fruits and vegetables. Try yoga, it is a great way to increased muscle strength and tone improves respiration, energy and vitality and it maintains a balanced metabolism."
		elif totalCal < 3000:
			html_params ["imageurl"]= "https://squashskills.com/images/sized/1400x660/1063618794-poi824.290-qx100.png"
			html_params["suggestions"]="You are eating a little too many calories in a day. I would suggest going for a run to make sure you burn those excess calories."
		elif totalCal >= 3000:
			html_params ["imageurl"] = "http://www.blakedating.com/wp-content/uploads/2016/11/Gym-Course.jpg"
			html_params["suggestions"]="Since you ate so many calories today. Try to go to the gym and do a mix of cardio and weights."
		self.response.out.write(template.render(html_params))


