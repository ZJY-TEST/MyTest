# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:21 
# @Author : Zhang Jingyao
# @File : test_calc.py
# @Software: PyCharm

import pytest
import os
from Practice.calc import Calc


# content of test_calc.py
class TestClass:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("x, y, z", [(1, 2, 3),
                                         (9, -3, 6),
                                         (-9.999, 1.111, -8.89),
                                         (0, 6, 6)
                                         ])
    def test_addition(self, x, y, z):
        result = self.calc.addition(x, y)
        assert result == z

    def test_substarction(self):
        result = self.calc.substarction(1, 1)
        assert result == 0

    def test_multiplication(self):
        result = self.calc.multiplication(1, 1)
        assert result == 1

    """
    有效等价类：
        分子：整数、负数、浮点数、0
        分母：分子：整数、负数、浮点数
    无效等价类：
        分子：非数字（字母、字符等）
        分母：0、非数字（字母、字符等）
    """

    @pytest.mark.parametrize("x, y, z", [(9, 3, 3),
                                         (9, -3, -3),
                                         (-9.999, 1.111, -9.00),
                                         (0, 6, 0),
                                         (5, 0, "分母不能为0"),
                                         ("x", "y", "z")
                                         ])
    def test_division(self, x, y, z):
        result = self.calc.division(x, y)
        assert result == z


if __name__ == '__main__':
    # pytest.main(["-s", "--html=report.html", "./Practice/test_calc.py"])
    pytest.main(["-vs", "F:/Hogwarts/Practice/test_calc.py]"])
