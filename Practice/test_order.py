# -*- coding:utf-8 -*-
# @Time : 2020/6/1 15:54 
# @Author : Zhang Jingyao
# @File : test_order.py 
# @Software: PyCharm
# @Disc: 用pytest-ordering插件控制用例执行顺序

import pytest


class TestPytest(object):

    @pytest.mark.run(order=-2)
    def test_two(self):
        print("test_two,测试用例")

    @pytest.mark.run(order=-1)
    def test_one(self):
        print("test_one,测试用例")

    @pytest.mark.run(order=3)
    def test_three(self):
        print("test_three,测试用例")


if __name__ == "__main__":
    pytest.main(['-vs', './test_order.py'])
