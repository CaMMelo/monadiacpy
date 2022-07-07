from unittest.mock import MagicMock, sentinel

from monadiacpy.result_or_failure import ResultOrFailure


def test_result_or_failure_shoud_be_failure():
    failure = ResultOrFailure(failure=sentinel.failure)

    assert failure.is_failure
    assert failure.failure is sentinel.failure


def test_result_or_failure_shoud_not_be_failure():
    result = ResultOrFailure(result=sentinel.result)

    assert result.is_failure is False
    assert result.result is sentinel.result


def test_when_no_result_or_failure_result_should_be_empty():
    result = ResultOrFailure()

    assert result.is_empty


def test_when_failure_result_or_failure_should_not_be_empty():
    result = ResultOrFailure(failure=sentinel.failure)

    assert result.is_empty is False


def test_should_not_call_function_when_failure():
    result = ResultOrFailure(failure=sentinel.failure)
    function = MagicMock()
    result.bind(function)

    function.assert_not_called()


def test_should_not_call_function_when_empty():
    result = ResultOrFailure()
    function = MagicMock()
    result.bind(function)

    function.assert_not_called()


def test_should_call_function_with_result_or_failure_wrapped_value():
    result = ResultOrFailure(result=sentinel.result)
    function = MagicMock()
    result.bind(function)

    function.assert_called_with(sentinel.result)


def test_bind_result_should_be_result_or_failure_wrapped_function_return_value():
    result = ResultOrFailure(result=sentinel.result)
    function = MagicMock(return_value=sentinel.function_a)
    bind_result = result.bind(function)

    assert isinstance(bind_result, ResultOrFailure)
    assert bind_result.is_empty is False
    assert bind_result.is_failure is False
    assert bind_result.result is sentinel.function_a


def test_bind_result_shoud_be_result_or_failure_wrapped_function_raised_exception():
    result = ResultOrFailure(result=sentinel.result)
    function = MagicMock()
    raised_exception = Exception()
    function.side_effect = raised_exception
    bind_result = result.bind(function)

    assert isinstance(bind_result, ResultOrFailure)
    assert bind_result.is_empty is False
    assert bind_result.is_failure is True
    assert bind_result.failure is raised_exception


def test_or_operator_should_operate_as_bind():
    result = ResultOrFailure(result=sentinel.result)
    function = MagicMock(return_value=sentinel.function_a)
    bind_result = result | function

    function.assert_called_with(sentinel.result)
    assert isinstance(bind_result, ResultOrFailure)
    assert bind_result.is_empty is False
    assert bind_result.is_failure is False
    assert bind_result.result is sentinel.function_a


def test_should_be_able_to_chain_bind_operations():
    result = ResultOrFailure(result=sentinel.result)
    function_a = MagicMock(return_value=sentinel.function_a)
    function_b = MagicMock(return_value=sentinel.function_b)
    bind_result = result | function_a | function_b

    function_a.assert_called_with(sentinel.result)
    function_b.assert_called_with(sentinel.function_a)
    assert isinstance(bind_result, ResultOrFailure)
    assert bind_result.is_empty is False
    assert bind_result.is_failure is False
    assert bind_result.result is sentinel.function_b
