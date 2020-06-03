# -*- coding:utf-8 -*-
# @Time : 2020/6/1 16:20 
# @Author : Zhang Jingyao
# @File : test_fixture.py 
# @Software: PyCharm


import pytest


@pytest.fixture()
def login():
    print("这是个登录方法")
    return 'tom', '123'


@pytest.fixture()
def operate():
    print("登录后的操作")


def test_case1(login, operate):
    print(login)
    print("test_case1,需要登录")


def test_case2():
    print("test_case2,不需要登录")


def test_case3(login, operate):
    print(login)
    print("test_case3,需要登录")


if __name__ == "__main__":
    pytest.main(['-vs', './test_fixture.py'])
