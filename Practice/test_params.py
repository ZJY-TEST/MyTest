# -*- coding:utf-8 -*-
# @Time : 2020/6/3 10:39 
# @Author : Zhang Jingyao
# @File : test_params.py 
# @Software: PyCharm
# @Disc: fixture传递参数


import pytest


@pytest.fixture(params=[1, 2, 3])
def data(request):  # 传入的数据需要使用一个固定的参数名request来接收
    return request.param


def test_data(data):
    print(f"测试数据： {data}")
    assert data < 5


if __name__ == "__main__":
    pytest.main(['-v', '-s', './test_params.py'])
