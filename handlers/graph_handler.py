
import jinja_env
import logging
import webapp2

class GraphHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("GraphHandler")
         html_params = {
            "title": "Fresh Fit",
            "content": ""
        }
        template = jinja_env.env.get_template('templates/graph.html')
        self.response.out.write(template.render(html_params))