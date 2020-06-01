# -*- coding:utf-8 -*-
# @Time : 2020/6/1 15:20 
# @Author : Zhang Jingyao
# @File : test_run_step.py 
# @Software: PyCharm
import pytest


def setup_module():
    print("\nsetup_module,只执行一次，当有多个测试类的时候使用")


def teardown_module():
    print("\nteardown_module,只执行一次，当有多个测试类的时候使用")


class TestPytest1(object):

    @classmethod
    def setup_class(cls):
        print("\nsetup_class1,只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class1,只执行一次")

    def setup_method(self):
        print("\nsetup_method1,每个测试方法都执行一次")

    def teardown_method(self):
        print("\nteardown_method1,每个测试方法都执行一次")

    def setup(self):
        print("\nsetup1,每个测试方法都执行一次")

    def teardown(self):
        print("\nteardown1,每个测试方法都执行一次")

    def test_three(self):
        print("\ntest_three，测试用例")

    def test_four(self):
        print("\ntest_four，测试用例")


class TestPytest2(object):

    @classmethod
    def setup_class(cls):
        print("\nsetup_class2,只执行一次")

    @classmethod
    def teardown_class(cls):
        print("\nteardown_class2,只执行一次")

    def setup_method(self):
        print("\nsetup_method2,每个测试方法都执行一次")

    def teardown_method(self):
        print("\nteardown_method2,每个测试方法都执行一次")

    def setup(self):
        print("\nsetup2,每个测试方法都执行一次")

    def teardown(self):
        print("\nteardown2,每个测试方法都执行一次")

    def test_one(self):
        print("\ntest_one，测试用例")

    def test_two(self):
        print("\ntest_two，测试用例")


if __name__ == "__main__":
    pytest.main(['-vs', './test_run_step.py'])
