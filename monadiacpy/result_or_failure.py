class ResultOrFailure:
    def __init__(self, result=None, failure=None):
        self.result = result
        self.failure = failure

    @staticmethod
    def result(value):
        return ResultOrFailure(result=value)

    @staticmethod
    def failure(value):
        return ResultOrFailure(failure=value)

    @staticmethod
    def empty():
        return ResultOrFailure()

    @property
    def is_failure(self):
        return self.failure is not None

    @property
    def is_empty(self):
        return self.is_failure is False and self.result is None

    @property
    def value(self):
        return self.failure if self.is_failure else self.result

    def bind(self, function):
        if self.is_empty:
            return self
        try:
            result = function(self.value)
            if isinstance(result, ResultOrFailure):
                result = result.value
        except Exception as failure:
            return ResultOrFailure(failure=failure)
        return ResultOrFailure(result=result)

    def bind_result(self, function):
        if self.is_failure:
            return self
        return self.bind(function)

    def bind_failure(self, function):
        if self.is_failure is False:
            return self
        return self.bind(function)

    def __or__(self, function):
        return self.bind_result(function)

    def __and__(self, function):
        return self.bind_failure(function)

    def __repr__(self):
        return f"ResultOrFailure({repr(self.value)})"

    def __str__(self):
        return str(self.value)
