class Maybe:
    def __init__(self, value):
        self.value = value

    @property
    def is_empty(self):
        return self.value is None

    def bind(self, function):
        if self.is_empty:
            return self
        result = function(self.value)
        return Maybe(result)

    def __or__(self, function):
        return self.bind(function)

    def __repr__(self):
        return f"Maybe({repr(self.value)})"

    def __str__(self):
        return str(self.value)
