import json
import random
import unittest
from api.app import create_app


class TestApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config="testing")
        self.client = self.app.test_client
        currency = random.choice(['USD', 'EUR', 'ARS'])
        self.uri = f'/api?currency={currency}'

    def test_quotes(self):
        """ Test default currency GET request """
        response = self.client().get(self.uri)
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data['success'] is True

    def test_quotes_days_param(self):
        """ Test currency GET request for previous n days """
        days = random.randint(1, 7)

        response = self.client().get(f'{self.uri}&days={days}')
        data = json.loads(response.data)

        assert response.status_code == 200
        assert data['success'] is True
        assert len(data['quotes']) == days

    def test_quotes_order_param(self):
        """ Test currency GET request in ascending or descending order """
        first_response = self.client().get(f'{self.uri}&orderby=asc')
        second_response = self.client().get(f'{self.uri}&orderby=desc')

        assert first_response.status_code == 200
        assert second_response.status_code == 200

        first_data = json.loads(first_response.data)
        second_data = json.loads(second_response.data)

        assert first_data['success'] is True
        assert second_data['success'] is True

        first_quotes = first_data['quotes']
        second_quotes = second_data['quotes']

        assert first_quotes[0]['id'] == second_quotes[-1]['id']

        both_data = zip(first_quotes, list(reversed(second_quotes)))
        assert not any(a['id'] != b['id'] for a, b in both_data)

    def test_invalid_currency(self):
        """ Test a not supported currency request """
        currency = 'BRL'
        response = self.client().get(f'/api?currency={currency}')
        message = json.loads(response.data)['message']

        assert response.status_code == 400
        assert message['currency'] == "You have entered an invalid " \
                                      "currency. [Keep in mind that " \
                                      "we only work with ARS, EUR and USD]"

    def test_invalid_route(self):
        """ Test a not supported endpoint """
        response = self.client().get(f'/api/invalid')
        data = json.loads(response.data)

        assert response.status_code == 404
        assert data['message'] == "This route is not supported."


if __name__ == "__main__":
    unittest.main()
