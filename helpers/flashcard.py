class Flashcard:
    def __init__(self, answer: str, definition: str):
        self.__answer = answer
        self.__definition = definition

    def get_answer(self) -> str:
        return self.__answer

    def get_definition(self) -> str:
        return self.__definition

    def to_dict(self) -> dict:
        return { "answer": self.__answer, "definition": self.__definition }