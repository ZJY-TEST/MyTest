# -*- coding:utf-8 -*-
# @Time : 2020/6/4 10:52 
# @Author : Zhang Jingyao
# @File : test_baidudemo.py 
# @Software: PyCharm


import allure
import pytest
import yaml
from selenium import webdriver
import time


@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data1", yaml.safe_load(open("data/data.yaml")))
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入关键词:{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)
        assert test_data1 != "python1"

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("关闭浏览器"):
        driver.quit()


if __name__ == "__main__":
    pytest.main(['./test_baidudemo.py', '-s', '-v', '--alluredir=./result/'])
