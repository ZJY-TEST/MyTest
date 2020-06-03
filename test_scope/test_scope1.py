# -*- coding:utf-8 -*-
# @Time : 2020/6/1 17:31 
# @Author : Zhang Jingyao
# @File : test_scope1.py 
# @Software: PyCharm

import pytest


def test_search1(open):
    print("test_search1")


def test_search2(open):
    print("test_search2")


def test_search3(open):
    print("test_search3")


if __name__ == "__main__":
    pytest.main()