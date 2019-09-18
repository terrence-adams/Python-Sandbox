import requests

uri = 'https://api.github.com/search/repositories'
full_uri = ''
r = None
key_word = ''
q = '?q='

def open_session():
    default_keword = 'c#'
    full_uri = uri + q + default_keword
    s =  requests.Session()
    r = s.get(full_uri)
    return r

def get_status():
    my_resp = open_session()
    print('Mt status is %s for url: %s' % (my_resp.status_code, my_resp.url))

def get_headers():
    my_resp = open_session()
    if(my_resp.ok):
        return my_resp.headers
    else:
        print("My status code is %s" % my_resp.status_code)

def return_json():
    my_resp = open_session()



if __name__ == '__main__':
    open_session()
    get_status()
    print(get_headers())