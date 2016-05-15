#!/usr/bin/env python
"""Tests for flask-crud"""

import os
import unittest
import tempfile
from app import app, db
from  config import basedir

class DBInit(unittest.TestCase):

    def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
		self.app = app.test_client()
		db.create_all()

    def tearDown(self):
		db.session.remove()
		db.drop_all()

class EmptyDBTestCase(DBInit):

    def setUp(self):
        DBInit.setUp(self)

    def tearDown(self):
        DBInit.tearDown(self)
    
    def test_empty_db(self):
        rv = self.app.get('/')
        #print rv.data
        assert "No entries" in rv.data

    def test_bad_entry_id(self):
        rv = self.app.get('/show/5')
        #print rv
        assert "404" in rv.data

    def test_new_message(self):
        retval = self.app.post('/new', data = dict(
            title="Hello",
            body="Test Message"),
            follow_redirects=True)
        assert "No entries" not in retval.data
        assert "Hello" in retval.data

class CrudDBTestCase(DBInit):

    def setUp(self):
        DBInit.setUp(self)
        self.app.post('/new', data = dict(
            title="Hello",
            body="Test Message"),
            follow_redirects=True)
        self.app.post('/new', data = dict(
            title="Hello2",
            body="Another Test Message"),
            follow_redirects=True)

    def tearDown(self):
        DBInit.tearDown(self)

    def test_show_message(self):
        retval =  self.app.get('/show/1')
        assert "Hello" in retval.data
        assert "Test Message" in retval.data
        assert "Another" not in retval.data

    def test_edit_message(self):
        retval = self.app.get('/edit/2')
        assert "Another Test" in retval.data
        retval = self.app.post('/edit/2', data = dict(
            title="Edited",
            body="Edited test message"),
            follow_redirects=True)
        assert "Edited" in retval.data

if __name__ == '__main__':
    unittest.main()

