import requests
import json

class Search:

    q = '?q='
    r = None
    cls_base_url = 'https://api.github.com/search/repositories'
    cls_keyword = 'tetris'
    cls_sort = '&stars'
    cls_order = '&desc'
    cls_qualifiers = '+language:assembly'


    def verify_status(self, full_url):
        r = requests.get(full_url)
        if r.ok:
            return 200
        else:
            return r.status_code

    def get_response(self, base_url, keyword = None, qualifiers = None, sort = None, order = None):
        full_url = base_url + self.q + keyword + qualifiers + sort + order
        self.r = requests.get(full_url)
        return self.r

    def save_response(self):
        response_to_save = self.get_response(self.cls_base_url, self.cls_keyword, self.cls_qualifiers, self.cls_sort, self.cls_order)
        content = json.loads(response_to_save.text)
        with open("response.txt", 'a') as rf:
            json.dump(content, rf, sort_keys= True, indent= 3)

        header_to_save = response_to_save.headers

        with open("headers.txt", 'a') as hf:
            for k, v in header_to_save.items():
                hf.write("%s : %s" % (k,v))
                hf.writelines('\n')






if __name__ == '__main__':
    search = Search()
    search.save_response()

