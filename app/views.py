#!/usr/bin/env python

from flask import render_template, url_for, redirect
from app import app, models, db

@app.route('/')
@app.route('/index')
def index():
    entries = models.Post.query.all()
    return render_template("index.html", entries=entries)

@app.route('/new', methods=["POST", "GET"])
def new_entry():
    post = models.Post(title="Hello", body="Test Message")
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))
