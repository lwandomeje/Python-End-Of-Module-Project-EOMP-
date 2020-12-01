import unittest
from test import *
class TestLottoTestCase(unittest.TestCase):
    def test_win(self):
        lwando= com()
        assert lwando.win() == True,"Must return True"
