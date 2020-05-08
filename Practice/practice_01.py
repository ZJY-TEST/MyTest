# -*- coding:utf-8 -*-
# @Time : 2020/5/6 10:21 
# @Author : Zhang Jingyao
# @File : practice_01.py 
# @Software: PyCharm

import sys
import os

# 猜数字游戏

# target_num = int(input("Please input target number:"))
# input_num = int(input("Please input a number:"))
#
# while target_num != input_num:
#     if target_num > input_num:
#         input_num = int(input("The number is little small, please input again:"))
#     elif target_num < input_num:
#         input_num = int(input("The number is little big, please input again:"))
# else:
#     print("Congratulations!! You got it!!")

#
# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(__file__))
# print(os.path.join(os.path.dirname(__file__),'txt.txt'))

# file_dir = os.path.join(os.path.dirname(__file__), 'txt.txt')
# with open(file_dir, 'r', encoding='utf-8') as f:
#     read_data = f.read()
#     f.close()
# print(read_data)

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

