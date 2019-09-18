import requests
import json
import unittest
import nose
import TestSuite
from TestSuite import Search as Search
__author__ ="Terrence Adams"



class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'https://api.github.com/search/repositories'
        cls.q = '?q='
        cls.keyword = 'tetris'
        cls.sort = '&stars'
        cls.order = '&desc'
        cls.qualifiers = '+language:assembly'
        cls.search = Search.Search()
        cls.response = cls.search.get_response(cls.base_url, cls.keyword, cls.qualifiers,cls.sort, cls.order)



    @classmethod
    def test_verify_status(cls):
        cls.assertTrue(cls.response.status_code, 200, msg='Status response is not 200')
        cls.assertTrue(cls.response.ok, True, msg='Failed status check')

    @classmethod
    def test_status_ok(cls):
        cls.assertTrue(cls.response.ok, True, msg= 'Status check is not ok.')

   # @classmethod
    #def test_status_code_less_than_200(cls):
     #   cls.assertGreater(cls.response.status_code, 500, msg='Fail')

    #@classmethod
    #def test_status_code_500(cls):
        #cls.assertGreaterEqual(cls.response.status_code, 500, 'Status code is 5xx')




if __name__ == '__main__':
    unittest.main()



