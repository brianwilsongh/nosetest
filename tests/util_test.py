import requests
import responses
from nose.tools import assert_true, assert_is_not_none
import os
import sys
sys.path.append(os.getcwd())
import app.utils

@responses.activate
def test_getAllReturnsCorrectResultCountWithStub():
    test_url='http://www.google.com'
    responses.add(responses.GET, test_url, status=200, content_type="application/json", body="""{"results":[{"k1": "v1"}, {"k2": "v2"}]}""")
    all = app.utils.get_all(test_url)
    assert_true(len(all) == 2)