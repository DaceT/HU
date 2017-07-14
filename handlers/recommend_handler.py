
import jinja_env
import logging
import webapp2

class RecommendHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("RecommendHandler")