from enum import Enum


class Keys(Enum):
    # Root
    FLASHCARDS = "/flashcards"

    # Flashcard Keys
    ANSWER = "answer"
    DEFINITION = "definition"
    TOPIC = "topic"

    # Preset Flashcard Decks
    TEST_DATA = ("TEST101", "TEST102", "TEST103", "TEST104", "TEST105")
