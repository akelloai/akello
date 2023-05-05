import unittest
from screening.mental_health import GAD7


class TestGAD7(unittest.TestCase):

    def test_gad7_test(self):
        gad7 = GAD7(akello_api_token='<token>')
        gad7.score_screener()
        assert (len(gad7.questions) == 7)
        assert(gad7.score > 0)

if __name__ == '__main__':
    unittest.main()
