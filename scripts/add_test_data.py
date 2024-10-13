import sys
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from rich import print

from flashcard_test_decks import TEST_101, TEST_102, TEST_103, TEST_104, TEST_105

# Enables the helpers modules to be imported
sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))
)
from helpers.database_helper import DatabaseHelper
from helpers.database_keys import Keys


def start_database():
    firebase_admin.initialize_app(credentials.Certificate({
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("UNIVERSE_DOMAIN")
    }), {
        'databaseURL': os.getenv("DATABASE_URL")
    })
    print(f"Database has been started in {__file__}")


def delete_test_data():
    ref = db.reference(Keys.FLASHCARDS.value)
    flashcards = ref.get()
    for key in flashcards:
        if key in Keys.TEST_DATA.value:
            ref.child(key).delete()
            print(f"Deleted flashcard deck: {key}")
    print("Deleted old test flashcard decks")


def insert_test_data():
    flashcard_test_decks = (TEST_101, TEST_102, TEST_103, TEST_104, TEST_105)
    for i, deck in enumerate(flashcard_test_decks):
        NEW_CODE = f"TEST10{i + 1}"
        DatabaseHelper.create_flashcard_deck(
            deck["topic"], deck["flashcards"], NEW_CODE
        )
        print(f"Inserted new flashcard deck: {NEW_CODE}")
    print("Successfully inserted test data")


def main():
    # Enables helpers module to be imported
    start_database()
    delete_test_data()
    insert_test_data()
    print("Operation completed successfully")


if __name__ == '__main__':
    main()
