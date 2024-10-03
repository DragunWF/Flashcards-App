class Flashcard:
    def __init__(self, answer: str, definition: str):
        self.__answer = answer
        self.__definition = definition

    def get_answer(self):
        return self.__answer

    def get_definition(self):
        return self.__definition
