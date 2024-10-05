import random
from string import ascii_letters, digits

class Utils:
    CODE_CHAR_COUNT_LIMIT = 7

    @staticmethod
    def generate_code() -> str:
        char_pool = ascii_letters + digits
        code = ""
        for i in range(Utils.CODE_CHAR_COUNT_LIMIT):
            code += char_pool[random.randint(0, len(char_pool) - 1)]
        return code