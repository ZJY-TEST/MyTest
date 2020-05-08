# -*- coding:utf-8 -*-
# @Time : 2020/5/6 10:21 
# @Author : Zhang Jingyao
# @File : test_calc.py
# @Software: PyCharm

import pytest
from Practice.calc import Calc


# content of test_calc.py
class TestClass:
    calc = Calc()

    def test_addition_one(self):
        result = self.calc.addition(5, 5)
        assert result == 10

    def test_addition_two(self):
        result = self.calc.addition(5, 6)
        assert result == 10


if __name__ == '__main__':
    pytest.main(["-s", "--html=a.html", "./Practice/test_calc.py"])
