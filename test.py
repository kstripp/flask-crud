#!/usr/bin/env python
"""Tests for flask-crud"""

import os
import unittest
import tempfile
from app import app, db
from flask.ext.migrate import Migrate 

class CrudTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.fname = tempfile.mkstemp()
        dbase_uri = 'sqlite://' + os.path.join(self.fname)
        app.config["SQLALCHEMY_DATABASE_URI"] = dbase_uri
        #app.config['TESTING'] = True
        migrate = Migrate(app, db)
        
        self.app = app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.fname)
    
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

