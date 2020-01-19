import webapp2
import os
import jinja2
import json
from datetime import datetime
from datetime import timedelta
from google.appengine.api import users
from google.appengine.ext import ndb


jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def get_candidates(prefix):
  results = []
  if len(prefix) == 0:
    return results
  for candidates in Candidate:
    if candidates.lower().startswith(prefix.lower()):
      results.append(candidates)
    return results

  def get_events(prefix):
    results = []
    if len(prefix) == 0:
      return results
    for events in EVENTS:
      if events.lower().startswith(prefix.lower()):
        results.append(events)
        return results
    return results

class SeedDataHandler(webapp2.RequestHandler):
    def get(self):
        seed_data()



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/CandidateList', CandidateHandler),
    ("/calendar", CalendarHandler),
    ("/events", EventHandler),
    ('/blogpost', BlogPostHandler),
    ('/login', LoginPageHandler),
    ('/afterpost', AfterPostHandler),
    ('/blogpostlist', BlogPostListHandler),
    ("/seed_data", SeedDataHandler),

], debug=True)
