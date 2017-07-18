
import jinja_env
import logging
import webapp2

class HistoryHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("HistoryHandler")
        html_params = {
            "title": "Fresh Fit",
            "content": ""
        }
        template = jinja_env.env.get_template('templates/history.html')
        self.response.out.write(template.render(html_params))
