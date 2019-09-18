import requests
import json
from requests import exceptions
from requests.exceptions import HTTPError


uri = 'https://api.github.com/search/repositories'
full_uri = ''
key_word = ''
q = '?q='
r = None
s = None
default_keyword = 'c#'
full_uri = uri + q + default_keyword + '&sort=stars' + '&order=desc' #default path for execution

#open session
try:
    #Main session created for requests
    s = requests.Session()
    r = s.get(full_uri)
except HTTPError as http_error:
    print(f'Http error occured {http_error}')

def get_status():
    print('Mt status is %s for url: %s' % (r.status_code, r.url))

def get_headers():
    if r.ok:
        return r.headers
    else:
        print("My status code is %s" % r.status_code)

def return_json():
    if r.ok:
        return r.json()

def return_content():
    return r.text

def return_headers():
    return(r.json())

def display_content():
    print(json.dumps(r.text, sort_keys=True, indent=4 ))

def display_headers():
    for k, v in r.headers.items():
        print(f'{k} : {v}')

def write_json_to_file():
    resp_in_json = json.loads(r.text) # converts to text
    with open('test.txt', 'a') as json_file:
        json.dump(resp_in_json, json_file, sort_keys=True, indent=3)


def write_header_to_file():
    header_file = r.headers
    with open('header.txt', 'a') as hf:
        for k, v in r.headers.items():
            hf.write("%s : %s" % (k,v))
            hf.writelines('\n')


if __name__ == '__main__':
    get_status()
    display_headers()
    write_json_to_file()
    write_header_to_file()