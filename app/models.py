#!/usr/bin/env python

from app import db

class Post(db.Model):

    id = db.Column(db.Integer,  primary_key=True)
    title = db.Column(db.String(64),  index=True)
    body = db.Column(db.String(2048), index=True)

    def __repr__(self):
        return '<Post %r>' % (self.title)
