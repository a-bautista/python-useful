'''
Base Test

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically and
make sure that is is new, blank database each time.
'''
from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):
    def setUp(self):
        # Make sure the database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        # Get a test client
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()





