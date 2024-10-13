import logging
import os
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from helpers.flashcard import Flashcard
from helpers.database_keys import Keys
from helpers.utils import Utils


class DatabaseHelper:
    @staticmethod
    def start_database():
        if not firebase_admin._apps:  # Check if Firebase is already initialized
            load_dotenv()
            logging.info("Successfully loaded environment variables")

            try:
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
                logging.info(
                    "Successfully connected to Firebase Realtime Database!"
                )
            except Exception as e:
                logging.error(f"Error initializing Firebase app: {e}")

    @ staticmethod
    def get_flashcards(code: str) -> tuple[str, list[Flashcard]] | None:
        ref = db.reference(f"{Keys.FLASHCARDS.value}/{code}")
        if ref is None:
            return None

        flashcards = []
        data = ref.get()
        if data is None:
            return None
        for key in data:
            if key == Keys.TOPIC.value:
                continue
            flashcards.append(Flashcard(data[key][Keys.ANSWER.value],
                                        data[key][Keys.DEFINITION.value]))

        return (data["topic"], flashcards)

    @ staticmethod
    def create_flashcard_deck(topic: str, flashcards: list[Flashcard]) -> str:
        if type(topic) is None or type(flashcards) is None:
            return None
        ref = db.reference(Keys.FLASHCARDS.value)

        # Validates newly generated codes to make sure a duplicate does not exist
        new_code = Utils.generate_code()
        while True:
            has_duplicate = False
            for code in ref.get():
                if new_code == code:
                    has_duplicate = True
                    break
            if has_duplicate:
                new_code = Utils.generate_code()
            else:
                break

        # Adds the flashcard data into the database
        new_flashcard_deck = {"topic": topic}
        for i, flashcard in enumerate(flashcards):
            new_flashcard_deck[f"flashcard{i + 1}"] = flashcard.to_dict()
        ref.child(new_code).set(new_flashcard_deck)

        return new_code
