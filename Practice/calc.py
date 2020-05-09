# -*- coding:utf-8 -*-
# @Time : 2020/5/8 16:12 
# @Author : Zhang Jingyao
# @File : calc.py 
# @Software: PyCharm


class Calc:

    # 加法
    def addition(self, x: float, y: float):
        """
        :param x: float
        :param y: float
        :return: x+y
        """
        z = x + y
        return round(z, 2)

    # 减法
    def substarction(self, x: float, y: float):
        """
        :param x: float
        :param y: float
        :return: x-y
        """
        z = x - y
        return round(z, 2)

    # 乘法
    def multiplication(self, x: float, y: float):
        """
        :param x: float
        :param y: float
        :return: x*y
        """
        z = x * y
        return round(z, 2)

    # 除法
    def division(self, x: float, y: float):
        """
        :param x: float
        :param y: float,y!=0
        :return: x/y
        """
        if y ==0:
            return "分母不能为0"
        else:
            z = x / y
            return round(z, 2)




