# -*- coding:utf-8 -*-
# @Time : 2020/6/1 17:31 
# @Author : Zhang Jingyao
# @File : test_scope2.py 
# @Software: PyCharm


import pytest


class TestFunc():

    def test_case1(self):
        print("test_case1,需要登录")

    def test_case2(self):
        print("test_case2,不需要登录")

    def test_case3(self):
        print("test_case3,需要登录")


if __name__ == "__main__":
    pytest.main()
