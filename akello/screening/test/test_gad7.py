"""
Unit tests for GAD7 Screener
"""

import unittest
import responses
from akello.screening.mental_health import MentalHealth
from akello.settings import API_URL


class TestGAD7(unittest.TestCase):
    """
    GAD7 Unit Tests
    """

    @responses.activate
    def test_gad7_object(self):
        """
        Test loading the GAD7 object
        """
        responses.add(responses.POST, f'{API_URL}/akello-gpt', json={'score': 3}, status=200)
        mh = MentalHealth(screener='gad7', api=None)
        assert len(mh.screener.questions) == 7


if __name__ == '__main__':
    unittest.main()
