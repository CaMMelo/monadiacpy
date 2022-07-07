from unittest.mock import MagicMock, sentinel
from monadiacpy.maybe import Maybe


def test_maybe_should_be_empty():
    maybe = Maybe(None)
    assert maybe.is_empty is True


def test_maybe_should_not_be_empty():
    maybe = Maybe(object())
    assert maybe.is_empty is False

def test_should_not_call_function_when_maybe_is_empty():
    maybe = Maybe(None)
    function = MagicMock()
    maybe.bind(function)
    
    function.assert_not_called()

def test_should_call_function_with_maybe_wraped_value():
    maybe = Maybe(sentinel.value)
    function = MagicMock()
    maybe.bind(function)

    function.assert_called_with(sentinel.value)


def test_bind_result_should_be_maybe_wraped_function_result():
    maybe = Maybe(sentinel.value)
    function = MagicMock(return_value=sentinel.result)
    result = maybe.bind(function)

    assert isinstance(result, Maybe)
    assert result.is_empty is False
    assert result.value is sentinel.result


def test_or_operator_should_operate_as_bind():
    maybe = Maybe(sentinel.value)
    function = MagicMock(return_value=sentinel.result)
    result = maybe | function

    function.assert_called_with(sentinel.value)
    assert isinstance(result, Maybe)
    assert result.is_empty is False
    assert result.value is sentinel.result


def test_should_be_able_to_chain_bind_operations():
    maybe = Maybe(sentinel.value)
    function_a = MagicMock(return_value=sentinel.result_a)
    function_b = MagicMock(return_value=sentinel.result_b)
    result = maybe | function_a | function_b

    function_a.assert_called_with(sentinel.value)
    function_b.assert_called_with(sentinel.result_a)
    assert isinstance(result, Maybe)
    assert result.is_empty is False
    assert result.value is sentinel.result_b