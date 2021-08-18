# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 10:03 下午
# @Author  : sunxy
# @Email   : xsun449@gmail.com
# @File    : 魔术方法.py
# @Software: PyCharm

class ClassDemo(object):

    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        # print("这个是new方法")
        return super().__new__(cls)

    # 必须return字符串
    def __str__(self):
        print(self.name)
        return self.name


m2 = ClassDemo("sunxy")

str(m2)
print(m2)
format(m2)
