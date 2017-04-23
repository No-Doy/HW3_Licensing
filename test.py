from app import app
from flask_testing import TestCase
import unittest

class FlaskTestCase(unittest.TestCase):

	#ensure that flask was set up properly
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/')
		self.assertEqual(response.status_code, 200)
	
	#ensure that text displays
	def test_login_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/')
		self.assertTrue('Hello World' in response.data)

if __name__ == '__main__':
	unittest.main()