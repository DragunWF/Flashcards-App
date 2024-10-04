import logging
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from helpers.flashcard import Flashcard
from helpers.database_keys import Keys
from helpers.utils import Utils


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
    
    @staticmethod
    def create_flashcard_deck(topic: str, flashcards: list[Flashcard]) -> str:
        if not type(topic) is None or not type(flashcards) is list:
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
