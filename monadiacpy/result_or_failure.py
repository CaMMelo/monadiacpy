class ResultOrFailure:
    def __init__(self, result=None, failure=None):
        self.result = result
        self.failure = failure

    @property
    def is_failure(self):
        return self.failure is not None

    @property
    def is_empty(self):
        return self.is_failure is False and self.result is None

    def bind_result(self, function):
        if self.is_failure or self.is_empty:
            return self
        try:
            result = function(self.result)
        except Exception as failure:
            return ResultOrFailure(failure=failure)
        return ResultOrFailure(result=result)

    def bind_failure(self, function):
        if self.is_empty or self.is_failure is False:
            return self
        try:
            result = function(self.failure)
        except Exception as failure:
            return ResultOrFailure(failure=failure)
        return ResultOrFailure(result=result)

    def __or__(self, function):
        return self.bind_result(function)

    def __and__(self, function):
        return self.bind_failure(function)

    def __repr__(self):
        if self.is_failure:
            return f"ResultOrFailure({repr(self.failure)})"
        return f"ResultOrFailure({repr(self.result)})"

    def __str__(self):
        if self.is_failure:
            return str(self.failure)
        return str(self.result)
