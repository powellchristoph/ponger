import json
import unittest

import ponger

class PongerTest(unittest.TestCase):

    def setUp(self):
        self.test_app = ponger.app.test_client()

    def test_ping_response(self):
        rv = self.test_app.get('/ping')
        self.assertEqual(200, rv.status_code)

        resp = json.loads(rv.data)
        self.assertEqual(resp, {'message': 'pong'})

if __name__ == '__main__':
    unittest.main()
