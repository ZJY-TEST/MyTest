# -*- coding:utf-8 -*-
# @Time : 2020/5/6 10:21 
# @Author : Zhang Jingyao
# @File : test_calc.py
# @Software: PyCharm

import pytest
from Practice.calc import Calc


# content of test_calc.py
class TestClass:
    def setup(self):
        self.calc = Calc()
    @pytest.mark.parametrize
    def test_addition(self):
        result = self.calc.addition(5.5, 5)
        assert result == 10.5

    def test_substarction(self):
        result = self.calc.substarction(5, 6)
        assert result == 10

    def test_multiplication(self):
        result = self.calc.multiplication(6, 6)
        assert result == 9

    def test_division(self):
        result = self.calc.division(9, 9)
        assert result == 1


if __name__ == '__main__':
    # pytest.main(["-s", "--html=report.html", "./Practice/test_calc.py"])
    pytest.main(["-vs", "./Practice/test_calc.py"])