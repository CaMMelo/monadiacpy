from monadiacpy.requests import (
    monadiac_delete,
    monadiac_get,
    monadiac_head,
    monadiac_options,
    monadiac_patch,
    monadiac_post,
    monadiac_put,
)


def test_when_url_is_none_monadiac_delete_should_be_empty():
    result = monadiac_delete(None)

    assert result.is_empty is True


def test_when_url_is_none_monadiac_get_should_be_empty():
    result = monadiac_get(None)

    assert result.is_empty is True


def test_when_url_is_none_monadiac_head_should_be_empty():
    result = monadiac_head(None)

    assert result.is_empty is True


def test_when_url_is_none_monadiac_options_should_be_empty():
    result = monadiac_options(None)

    assert result.is_empty is True


def test_when_url_is_none_monadiac_patch_should_be_empty():
    result = monadiac_patch(None)

    assert result.is_empty is True


def test_when_url_is_none_monadiac_post_should_be_empty():
    result = monadiac_post(None)

    assert result.is_empty is True


def test_when_url_is_none_monadiac_put_should_be_empty():
    result = monadiac_put(None)

    assert result.is_empty is True
