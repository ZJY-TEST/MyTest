# -*- coding:utf-8 -*-
# @Time : 2020/6/3 16:08 
# @Author : Zhang Jingyao
# @File : test_mark_parametrize.py 
# @Software: PyCharm
# @Disc: 使用parametrize实现参数化

import pytest


@pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("7+2",9), ("7*5", 30)])
def test_eval(test_input, expected):
    #  eval 将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == expected


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [7, 8, 9])
def test_foo(x, y):
    print(f"测试数据组合x:{x}，y:{y}")




if __name__ == "__main__":
    pytest.main(['-v', '-s', './test_mark_parametrize.py'])