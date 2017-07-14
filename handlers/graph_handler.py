
import jinja_env
import logging
import webapp2

class GraphHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GraphHandler")