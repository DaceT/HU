import os
import webapp2

from handlers import jinja_env
from handlers import main_handler
from handlers import about_handler
from handlers import recommend_handler


jinja_env.init(os.path.dirname(__file__))


app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/about', about_handler.AboutHandler),
    ('/recommend', recommend_handler.RecommendHandler),
], debug=True)

