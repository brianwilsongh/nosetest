import requests
import responses
from nose.tools import assert_true, assert_is_not_none, assert_raises
import os
import sys
sys.path.append(os.getcwd())
import app.utils
import csv

@responses.activate
def test_getAllReturnsCorrectResultCountWithStub():
    test_url='https://swapi.co/api/people/'
    responses.add(responses.GET, test_url, status=200, content_type="application/json", body="""{"results":[{"k1": "v1"}, {"k2": "v2"}]}""")
    all = app.utils.get_all(test_url)
    assert_true(len(all) == 2)

@responses.activate
def test_getAllThrowsErrorOnBadStatus():
    test_url='https://swapi.co/api/people/'
    responses.add(responses.GET, test_url, status=500, content_type="application/json", body="""{"results":[{"k1": "v1"}, {"k2": "v2"}]}""")
    assert_raises(Exception, app.utils.get_all, test_url)
    
@responses.activate
def test_getOneReturnsCorrectResultCountWithStub():
    test_url="https://swapi.co/api/people/5/"
    responses.add(responses.GET, test_url, status=200, content_type="application/json", body="""{"results":[{"k1": "v1"}]}""")
    all = app.utils.get_one(test_url)
    assert_true(type(all) is dict)
    
@responses.activate
def test_getOneThrowsErrorOnBadStatus():
    test_url="https://swapi.co/api/people/5/"
    responses.add(responses.GET, test_url, status=500, content_type="application/json", body="""{"results":[{"k1": "v1"}]}""")
    assert_raises(Exception, app.utils.get_one, test_url)
    
@responses.activate
def test_sendFileToURLReturnsTrue():
    test_url="http://httpbin.org/post"
    responses.add(responses.POST, test_url, status=200)
    FILENAME = "util_test_temp.csv"
    with open(FILENAME, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["dummyfile"])
    assert_raises(Exception, app.utils.send_file_to_url(test_url, FILENAME))
    os.remove(FILENAME)
    

