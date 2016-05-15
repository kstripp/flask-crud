#!/usr/bin/env python

from flask import render_template, url_for, redirect, abort
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
        post = models.Post.query.get(id)
        if post is None:
            abort(404)
        return render_template("show.html", post=post)

@app.route('/edit/<id>', methods=["POST", "GET"])
def edit_entry(id):
    form = forms.NewEntry()
    post = models.Post.query.get(id)
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        form.title.default = post.title
        form.body.default = post.body
        form.process()
        return render_template("new.html", title="New Entry", form=form)
