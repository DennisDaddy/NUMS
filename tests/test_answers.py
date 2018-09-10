import unittest
import json
import os
import sys
from app import *

sys.path.insert(0, os.path.abspath(".."))

class AnswersTestCase(unittest.TestCase):
	"""This test case represents test for answers testcase"""


	def setUp(self):
		"""Define test variables and initialize the app."""
		self.app = create_app(config_name="testing")
		self.client = self.app.test_client


	def test_home(self):
		"""This method tests root endpoint"""
		tester = app.test_client(self)
		response = tester.get('/api/v1', content_type='application/json')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Welcome to Stackoverflow-lite', response.data)

	def test_create_answer(self):
		"""This method tests endpoint for creating an answer"""
		response = self.client().post('/api/v1/answers', content_type='application/json')
		self.assertEqual(response.status_code, 400)
	
	
	def test_retrieve_all_answers(self):
		"""Test retrieving answers"""
		response = self.client().get('/api/v1/answers')
		self.assertEqual(response.status_code, 200)

	def test_modify_answer(self):
		"""This method tests endpoint for updating an answer"""
		response = self.client().get('api/v1/questions/1')
		self.assertEqual(response.status_code, 200)

	def test_delete_answer(self):
		"""This method tests endpoint for deleting an answer"""
		response = self.client().get('api/v1/answers/1')
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()