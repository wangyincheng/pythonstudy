#!/usr/bin/python env

__author__ = 'wangxiaodong'
__filename__ = 'Bar_test1'

# project name:pythonstudy
#   file name:Bar_test1
#   auther:wangxiaodong
#   create date:2017/8/2 21:16
#   change auther:
#   change date:
#   version:
#   using enviroment:Django 1.13.0
#   python version:python 3.5.2
#   usage:

import os

import math

filename = __filename__+'.html'
filepath = 'g:/pyecharts'

from pyecharts import Bar


attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
bar = Bar("柱状图示例")
bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"],
        is_datazoom_show=True, datazoom_range=[50, 80])
bar.show_config()
bar.render(os.path.join(filepath, filename))