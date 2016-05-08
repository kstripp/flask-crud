#!/usr/bin/env python
"""Tests for flask-crud"""

import os
import unittest
import tempfile
from app import app, db
from  config import basedir

class CrudTestCase(unittest.TestCase):

    def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
		self.app = app.test_client()
		db.create_all()

    def tearDown(self):
		db.session.remove()
		db.drop_all()
    
    def test_empty_db(self):
        rv = self.app.get('/')
        print rv
        assert "No entries" in rv.data

    def test_new_message(self):
        retval = self.app.post('/new', data = dict(
            title="Hello",
            body="Test Message"),
            follow_redirects=True)
        assert "No entries" not in retval.data
        assert "Hello" in retval.data
        assert "Test Message" in retval.data

if __name__ == '__main__':
    unittest.main()

