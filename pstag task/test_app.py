import unittest
from app import app

class TestCarSearch(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_search(self):
        response = self.app.get('/search?color=red')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'red', response.data)

    def test_download(self):
        response = self.app.get('/download?color=red')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
