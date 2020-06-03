# -*- coding:utf-8 -*-
# @Time : 2020/6/3 17:02 
# @Author : Zhang Jingyao
# @File : test_yaml.py 
# @Software: PyCharm

import pytest
import yaml


@pytest.mark.parametrize("a, b", yaml.safe_load(open("data.yml", encoding='utf-8')))
def test_foo(a, b):
    print(f"a + b = {a + b}")
    print(yaml.safe_load(open("data.yml", encoding='utf-8')))
    print(type(yaml.safe_load(open("data.yml", encoding='utf-8'))))


if __name__ == "__main__":
    pytest.main(['-v', '-s', './test_yaml.py'])
