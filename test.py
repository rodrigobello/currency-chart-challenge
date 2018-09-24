import unittest
from api.app import create_app
from utils.currencies import CURRENCIES
import random


class TestQuotations(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config="testing")
        self.client = self.app.test_client

    def test_get_quotes(self):
        """ Test all quotes [GET Request] """
        response = self.client().get('/api/quotes')
        assert response.status_code == 200

    def test_get_currency(self):
        """ Test specific currency quotes [GET Request] """
        currency = random.choice(CURRENCIES)[0]

        response = self.client().get(f'/api/quotes/{currency}')

        if currency in ['USD', 'EUR', 'ARS']:
            assert response.status_code == 200
        else:
            assert response.status_code == 404


if __name__ == "__main__":
    unittest.main()
