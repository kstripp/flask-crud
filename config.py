#!/usr/bin/env python
""" Config file for pylight """

import os

FLASK_HOST="127.0.0.1"
FLASK_PORT=5000

WTF_CRSF_ENABLED = True
SECRET_KEY = 'gdygjklkhytdestgio845yhgfdrfh'

basedir = os.path.abspath(os.path.dirname(__file__))

# Database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_TRACK_MODIFICATIONS = False

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
