#!/usr/bin/env python

from flask import render_template, url_for, redirect
from app import app, models, db, forms

@app.route('/')
@app.route('/index')
def index():
    entries = models.Post.query.all()
    return render_template("index.html", entries=entries)

@app.route('/new', methods=["POST", "GET"])
def new_entry():
    form = forms.NewEntry()
    if form.validate_on_submit():
        post = models.Post(title=form.title.data, body=form.body.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template("new.html", title="New Entry", form=form)

@app.route('/show/<id>')
def show_entry(id):
        # post = 
        return render_template("show.html")
