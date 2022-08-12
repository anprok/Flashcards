def check_w_letter(word):
    if word.find('w') >= 0:
        raise WordError("Character found")
    return word


class WordError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
