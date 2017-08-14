# -*- coding: utf-8 -*-
import flask_testing

from hamcrest import *
from mock import patch

from app import app, HOME_TIMELINE_URL, POST_TWEET_URL, oauth_req


class MasterTest(flask_testing.TestCase):
    def create_app(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = True
        return self.app


    def setUp(self):
        self.client = self.app.test_client()

    def tearDown(self):
        pass


class MainTests(MasterTest):

    def test_oauth_req_0(self):
        self.skipTest('TODO')