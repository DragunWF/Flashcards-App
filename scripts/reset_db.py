import sys
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from rich import print


def start_database():
    firebase_admin.initialize_app(credentials.Certificate('../private/credentials.json'), {
        'databaseURL': "https://flashcards-app-58e80-default-rtdb.asia-southeast1.firebasedatabase.app/"
    })
    print(f"Database has been started in {__file__}")


def reset_db():
    # Enables helpers module to be imported
    sys.path.append(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    )
    from helpers.database_keys import Keys

    # Resets the DB, deletes all user-created keys
    ref = db.reference(Keys.FLASHCARDS.value)
    flashcards = ref.get()
    for key in flashcards:
        if key != 'TEST101':
            ref.child(key).delete()
            print(f"Deleted flashcard deck: {key}")
    print("All user-created decks has been successfully deleted!")


def main():
    start_database()
    reset_db()


if __name__ == '__main__':
    main()
