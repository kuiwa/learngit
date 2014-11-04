# -*- coding: utf-8 -*-

import web

web.config.debug = False

#urls = ( '/hello', 'Index' )
urls = (
	"/count", "count",
	"/reset", "reset"
)
#app = web.application(urls, globals())
app = web.application(urls, locals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'count': 0})

class count:
	def GET(self):
		session.count += 1
		return str(session.count)
		
class reset:
	def GET(self):
		session.kill()
		return ""
#render = web.template.render('templates/')
#render = web.template.render('templates/', base="layout")
class Index(object):
	def GET(self):
		return render.hello_form()
		#form = web.input(name="Nobody")
		#form = web.input(name="Nobody", greet=None)
		#add default value of greet
		#greeting = "Hello World"
		#sub_greeting = "Hello, %s, %s" % (form.name, form.greet)
		#用来在python和html之间传递变量，前面的是html里的，后面的是python里的，变量名可以不同
		#return render.index(greeting = sub_greeting)
		#return render.index("I'm very glad to see you,")
		
	def POST(self):
		form = web.input(name="Nobody", greet="Hello")
		greeting = "%s, %s" % (form.greet, form.name)
		return render.index(greeting = greeting)
if __name__ == "__main__":
	app.run()