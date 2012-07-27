import os
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template


class MainPage(webapp.RequestHandler):
	authorized = False
	def get(self):
		#user = users.get_current_user()

		'''if not user:
			self.redirect(users.create_login_url(self.request.uri))
			return

		if user.nickname() != 'jkorkean':
			return
		'''
		if not self.authorized:
			self.response.out.write("""
				<form method="post">
				<input type="text" name="user"/>
				<input type="password" name="pass"/>
				<input type="submit" value="login"/>
				</form>""")
			return

		#self.response.headers['Content-Type'] = 'text/plain'
		#self.response.out.write('Hello, ' + user.nickname())
		template_values = {
		}
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, template_values))
		return

	def post(self):
		if self.request.get('user') == 'bob' and self.request.get('pass') == 'babylon':
			self.authorized = True
			template_values = {
			}
			path = os.path.join(os.path.dirname(__file__), 'index.html')
			self.response.out.write(template.render(path, template_values))
			return
		else:
			self.authorized = Dalse
			self.response.out.write("""
				<form method="post">
				<input type="text" name="user"/>
				<input type="password" name="pass"/>
				<input type="submit" value="login"/>
				</form>""")
			return


application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)



def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
