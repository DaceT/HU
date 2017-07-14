
import jinja_env
import logging
import webapp2

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("AboutHandler")
        html_params = {
            "title": "Fresh Fit",
            "content": ""
        }
        template = jinja_env.env.get_template('templates/about.html')
        self.response.out.write(template.render(html_params))