
import jinja_env
import logging
import webapp2

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("HistoryHandler")