from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import os
from google.appengine.ext.webapp import template

class Component(webapp.RequestHandler):
    def get(self):



        params = self.request.get('params').split(',')
        component_name = params[0]
        component_url = params[1]

        #component_url = self.request.get('src')
        #component_name = self.request.get('name')
        
        template_values = {
            'url' : component_url,
            'name': component_name,
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))
        
application = webapp.WSGIApplication(
                                     [('/component.html', Component)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()        