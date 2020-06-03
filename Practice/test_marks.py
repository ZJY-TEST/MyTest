# -*- coding:utf-8 -*-
# @Time : 2020/6/3 10:51 
# @Author : Zhang Jingyao
# @File : test_marks.py 
# @Software: PyCharm
# @Disc: 运行指定标签的用例

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

    @pytest.mark.run(order=4)
    # @pytest.mark.mymark1
    def test_mymark1(self):
        print("test_mymark1,测试用例")

    @pytest.mark.run(order=5)
    # @pytest.mark.mymark2
    def test_mymark2(self):
        print("test_mymark2,测试用例")

# if __name__ == "__main__":
#     # pytest.main(['-v', '-s', './test_marks.py'])
#     pytest.main(['-m', 'mymark1'])