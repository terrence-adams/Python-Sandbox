__author__ = 'adam0954'
import requests
import json
import _json


full_uri = None
default_qualifier = "user:terrence-adams"
uri = 'https://api.github.com/search/repositories'
key_word = 'c#'
q = '?q='

def build_full_uri(key_word='c#'):
    uri = 'https://api.github.com/search/repositories'
    full_uri = uri + q + key_word + "+sort=desc"
    print (full_uri)
    return full_uri

def verify_status(my_key_word = key_word):
    r = requests.get(uri + q + my_key_word)
    print(r.url)
    print('My status is: %s ' % r.status_code)

def print_response():
    r = requests.get(build_full_uri(), params=None)
    print(r.headers)
    print(r.request)
    print(r.json())




if __name__ == '__main__':
    build_full_uri()
    verify_status('trees')
    print_response()







