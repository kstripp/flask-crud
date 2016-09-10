flask-crud
==========

This is a simple app to demonstrate (err... I mean figure out)
CRUD apps with flask.

Database migrations
===================
Create the database and enable migrations

```
python db.py db init
```

Generate the (first) migration
```
python db.py db migrate
```

Apply migration to database
```
python db.py db upgrade
```

Documentation on flask-migrate can be found at:
http://flask-migrate.readthedocs.io/en/latest/
