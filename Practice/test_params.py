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


'''
如果测试数据需要在fixture方法中使用，同时也需要在测试用例中使用，可以在使用parametrize的时候
添加一个参数indirect=Ture，pytest可以实现将参数输入到fixture方法中，也可以在当前的测试用例
中使用
'''

test_user_data = ['Tome', 'Jerry']


@pytest.fixture(scope="module")
def login_r(request):
    #  通过request.param获取参数
    user = request.param
    print(f"\n 登录用户：{user}")
    return user


#  indirect参数设置为Ture，pytest会把argnames当作函数去执行，将argvalues作为参数传入到argvalues这个函数里
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login返回的值：{a}")
    assert a != ""


if __name__ == "__main__":
    pytest.main(['-v', '-s', './test_params.py'])
