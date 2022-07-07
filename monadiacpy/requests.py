from functools import partial

from requests import delete, get, head, options, patch, post, put
from requests.exceptions import JSONDecodeError

from monadiacpy.result_or_failure import ResultOrFailure


def extract_result(result):
    try:
        return result.json()
    except JSONDecodeError:
        return result.content


def monadiac_delete(url, **kwargs):
    return ResultOrFailure(url) | partial(delete, **kwargs) | extract_result


def monadiac_get(url, params=None, **kwargs):
    return ResultOrFailure(url) | partial(get, params=params, **kwargs) | extract_result


def monadiac_head(url, **kwargs):
    return ResultOrFailure(url) | partial(head, **kwargs) | extract_result


def monadiac_options(url, **kwargs):
    return ResultOrFailure(url) | partial(options, **kwargs) | extract_result


def monadiac_patch(url, data=None, **kwargs):
    return ResultOrFailure(url) | partial(patch, data=data, **kwargs) | extract_result


def monadiac_post(url, data=None, json=None, **kwargs):
    return (
        ResultOrFailure(url)
        | partial(post, data=data, json=json, **kwargs)
        | extract_result
    )


def monadiac_put(url, data=None, **kwargs):
    return ResultOrFailure(url) | partial(put, data=data, **kwargs) | extract_result
