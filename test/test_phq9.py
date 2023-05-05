import unittest
from screening.mental_health import PHQ9


class TestPHQ9(unittest.TestCase):

    def test_phq9_test(self):
        phq9 = PHQ9(akello_api_token='<token>')
        phq9.score_screener()
        assert (len(phq9.questions) == 9)
        assert(phq9.score > 0)

if __name__ == '__main__':
    unittest.main()
