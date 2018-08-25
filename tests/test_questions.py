import unittest
import json
import os
import sys
from app import *

sys.path.insert(0, os.path.abspath(".."))

class QuestionTestCase(unittest.TestCase):
    """This test case represents test for a user and diary entry testcase"""
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client

    def test_index(self):
        result = self.client().get('/')
        self.assertEqual(result.status_code,200, {'message': 'Welcome to Stackoverflow-lite'})



if __name__ == '__main__':
    unittest.main()