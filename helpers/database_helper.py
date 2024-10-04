import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from helpers.flashcard import Flashcard
from helpers.database_keys import Keys


class DatabaseHelper:
    @staticmethod
    def start_database():
        firebase_admin.initialize_app(credentials.Certificate('private/credentials.json'), {
            'databaseURL': "https://flashcards-app-58e80-default-rtdb.asia-southeast1.firebasedatabase.app/"
        })
        logging.info("Successfully connected to Firebase Realtime Database!")

    @staticmethod
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
