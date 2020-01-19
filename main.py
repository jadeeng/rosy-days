import webapp2
import os
import jinja2
import json
from datetime import datetime
from datetime import timedelta



jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)





app = webapp2.WSGIApplication([
    ('/', MainHandler),


], debug=True)
