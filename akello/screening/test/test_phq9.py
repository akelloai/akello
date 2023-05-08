"""
Unit tests for PHQ9 Screener
"""

import unittest
import responses
from akello.screening.mental_health import MentalHealth
from akello.settings import API_URL


class TestPHQ9(unittest.TestCase):
    """
    Unit tests for PHQ9 Screener
    """
    @responses.activate
    def test_phq9_object(self):
        """
        Simple test to load the PHQ9 object
        """
        responses.add(responses.POST, f'{API_URL}/akello-gpt', json={'score': 3}, status=200)
        mh = MentalHealth(screener='phq9', api=None)
        assert len(mh.screener.questions) == 9

if __name__ == '__main__':
    unittest.main()
