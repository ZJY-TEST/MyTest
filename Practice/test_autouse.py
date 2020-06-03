# -*- coding:utf-8 -*-
# @Time : 2020/6/3 10:29 
# @Author : Zhang Jingyao
# @File : test_autouse.py 
# @Software: PyCharm


import pytest


@pytest.fixture(autouse="ture") # 当autouse="ture"，用例自动执行fixture，无需传入
def myfixture():
    print("this is my fixture")


class TestAutouse():

    def test_one(self): # 用例自动执行fixture，无需传入
        print("执行test_one")
        assert 1 + 2 == 3

    def test_two(self): # 用例自动执行fixture，无需传入
        print("执行test_two")
        assert 1 == 1

    def test_three(self): # 用例自动执行fixture，无需传入
        print("执行test_three")
        assert 1 + 1 == 2


if __name__ == "__main__":
    pytest.main(['-v', '-s', './test_autouse.py'])
