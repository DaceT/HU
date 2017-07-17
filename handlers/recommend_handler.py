
import jinja_env
import logging
import webapp2

class RecommendHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("RecommendHandler")
        html_params = {
            "title": "Fresh Fit",
            "content": ""
        }
        template = jinja_env.env.get_template('templates/recommend.html')
        self.response.out.write(template.render(html_params))