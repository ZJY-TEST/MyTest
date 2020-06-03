# -*- coding:utf-8 -*-
# @Time : 2020/6/1 17:14 
# @Author : Zhang Jingyao
# @File : conftest.py 
# @Software: PyCharm

import pytest


@pytest.fixture(scope="module")
def open():
    print("打开浏览器")
    yield

    print("执行teardown !")
    print("最后关闭浏览器")