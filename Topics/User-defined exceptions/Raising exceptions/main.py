def sum_with_exceptions(a, b):
    if a + b >= 0:
        return a + b
    raise NegativeSumError("Error!")


class NegativeSumError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
