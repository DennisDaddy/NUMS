import unittest
import json
import os, sys
sys.path.insert(0, os.path.abspath(".."))
from app import *

class UserTeastCase(unittest.TestCase):
    """This testcase represents the user model testcase"""
    def setUp(self):
        """Initialize test variables"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.user = {
            'username': "dennis"
        }
    def test_home(self):
        response = self.client.get('/api/v1')
        self.assertEqual(response.status_code, 200)
    

    def test_user_registration(self):
        pass