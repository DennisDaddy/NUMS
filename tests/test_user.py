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
            'username': "dennis",
            'email': "dennis@gmail.com",
            'password': "foobar",
            'password_confirmation': "foobar"
        }

    def test_home(self):
        """This is a method for testing root endpoint"""
        response = self.client.get('/api/v1')
        self.assertEqual(response.status_code, 200)    

    def test_register_user(self):
        """This is a method for testing user registration"""
        response = self.client.post('/api/v1/auth/register', data=json.dumps(
            dict(username="dennis", email="dennis@gmail.com", password="foobar",
            password_confirmation="foobar")),
            content_type="application/json")
        self.assertEqual(response.status_code, 200)    

    def test_user_login(self):
        """This is a method for testing user login"""
        response = self.client.post('/api/v1/auth/login', data=json.dumps(
            dict(username="dennis", email="dennis@gmail.com", password="foobar",
            password_confirmation="foobar")),
            content_type="application/json")
        self.assertEqual(response.status_code, 200)
    
    def test_user_account(self):
        """This is a method for testing user account information"""
        response = self.client.get('/api/v1/account/1')
        self.assertEqual(response.status_code, 200)