
import jinja_env
import logging
import webapp2

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("AboutHandler")