# -*- coding:utf-8 -*-
# @Time : 2020/6/1 16:39 
# @Author : Zhang Jingyao
# @File : test_fixture_scope.py 
# @Software: PyCharm

import pytest


@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown !")
    print("最后关闭浏览器")


@pytest.mark.usefixtures("open")
def test_search1():
    print("test_search1")
    raise NameError
    pass


def test_search2():
    print("test_search2")
    pass


def test_search3():
    print("test_search3")
    pass


if __name__ == "__main__":
    pytest.main(['-vs', './test_fixture_scope.py'])
