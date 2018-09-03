import unittest
import json
import os
import sys
from app import *

sys.path.insert(0, os.path.abspath(".."))

class QuestionTestCase(unittest.TestCase):
	"""This test case represents test for question testcase"""
	def test_home(self):
		"""This method tests root endpoint"""
		tester = app.test_client(self)
		response = tester.get('/', content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Welcome to Stackoverflow-lite', response.data)


if __name__ == '__main__':
    unittest.main()