import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class DatabaseHelper:
    @staticmethod
    def start_database():
        firebase_admin.initialize_app(credentials.Certificate('private/credentials.json'), {
            'databaseURL': 'https://flashcards-app-58e80.firebaseio.com'
        })
        logging.info("Successfully connected to Firebase Realtime Database!")
