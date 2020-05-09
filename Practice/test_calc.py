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

    @pytest.mark.parametrize("x, y, z", [(1, 2, 3),
                                         (-1, -2, -3),
                                         (0.1, 0.2, 0.3),
                                         (0.005, 0.004, 0.01),
                                         (0.0000, 0.00000, 0.00),
                                         (3.001, -3.0, 0),
                                         (4.569, 0, 4.57)])
    def test_addition(self, x, y, z):
        result = self.calc.addition(x, y)
        assert result == z

    # @pytest.mark.parametrize()
    def test_substarction(self):
        result = self.calc.substarction(5, 6)
        assert result == 10

    # @pytest.mark.parametrize()
    def test_multiplication(self):
        result = self.calc.multiplication(6, 6)
        assert result == 9

    # @pytest.mark.parametrize()
    def test_division(self):
        result = self.calc.division(9, 9)
        assert result == 1


if __name__ == '__main__':
    pytest.main(["-s", "--html=report.html", "./Practice/test_calc.py"])
    # pytest.main(["-vs", "./Practice/test_calc.py"])
