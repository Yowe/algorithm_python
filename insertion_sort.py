#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Yowe"

'''
插入排序
'''


def insert_sort(array):
    for j in range(0, len(array)):
        if j == 0:  # 首项不做处理
            continue
        key = array[j]  # 取出要排序的数字
        i = j - 1   # 前一项索引
        while i >= 0 and array[i] > key:    # 当前一项大于当前项时，前一项前移，继续与前一项比较
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key    # 找到最小项位置，并赋值


array = [3, 4, 1, 6, 2, 9, 7, 0, 8, 5]
insert_sort(array)
print(array)