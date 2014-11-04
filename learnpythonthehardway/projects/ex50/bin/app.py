# -*- coding: utf-8 -*-

import web

urls = (
	'/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
	
	def GET(self):
		return render.hello_form()
		
	def POST(self):
		p_greeting = "This is p_greeting"
		form = web.input(name="Nobody", greet="Hello")
		p_form = "%s, %s" % (form.greet, form.name)
		return render.index(h_greeting = p_greeting, h_form = p_form)
		
if __name__ == "__main__":
	app.run()