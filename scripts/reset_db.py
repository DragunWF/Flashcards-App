import sys
import os
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from rich import print


def start_database():
    load_dotenv()
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
        if not key in Keys.TEST_DATA.values:
            ref.child(key).delete()
            print(f"Deleted flashcard deck: {key}")
    print("All user-created decks has been successfully deleted!")


def main():
    start_database()
    reset_db()


if __name__ == '__main__':
    main()
