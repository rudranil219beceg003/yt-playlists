from http.server import BaseHTTPRequestHandler
from urllib import parse
import cgi

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		s = self.path
		dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
		self.send_response(200)
		self.send_header('Content-type','text/plain')
		self.end_headers()

		if "name" in dic:
			message = "Hello, " + dic["name"] + "!"
		else:
			message = "Hello, stranger!"

		self.wfile.write(message.encode())
		return

	def do_POST(self):
		try:
			s = self.path
			ctype, pdict = cgi.parse_header(self.headers['content-type'])
			print(ctype)
			print(pdict)
			self.end_headers()
			# pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
			# if ctype == 'multipart/form-data':
			# 	fields = cgi.parse_multipart(self.rfile, pdict)
			# 	restaurant_name = fields.get('newRestaurantName')
				
		except:
			print("Inside the exception block")
