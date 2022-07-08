from functools import partial

from requests import delete, get, head, options, patch, post, put

from monadiacpy.result_or_failure import ResultOrFailure


def get_response_body(response):
    response.raise_for_status()
    return response.json()


def monadiac_delete(url, **kwargs):
    return ResultOrFailure(url) | partial(delete, **kwargs) | get_response_body


def monadiac_get(url, params=None, **kwargs):
    return (
        ResultOrFailure(url) | partial(get, params=params, **kwargs) | get_response_body
    )


def monadiac_head(url, **kwargs):
    return ResultOrFailure(url) | partial(head, **kwargs) | get_response_body


def monadiac_options(url, **kwargs):
    return ResultOrFailure(url) | partial(options, **kwargs) | get_response_body


def monadiac_patch(url, data=None, **kwargs):
    return (
        ResultOrFailure(url) | partial(patch, data=data, **kwargs) | get_response_body
    )


def monadiac_post(url, data=None, json=None, **kwargs):
    return (
        ResultOrFailure(url)
        | partial(post, data=data, json=json, **kwargs)
        | get_response_body
    )


def monadiac_put(url, data=None, **kwargs):
    return ResultOrFailure(url) | partial(put, data=data, **kwargs) | get_response_body
