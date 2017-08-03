#!/usr/bin/python env

__author__ = 'wangxiaodong'
__filename__ = 'Line_test'

# project name:pythonstudy
#   file name:Line_test
#   auther:wangxiaodong
#   create date:2017/8/2 21:06
#   change auther:
#   change date:
#   version:
#   using enviroment:Django 1.13.0
#   python version:python 3.5.2
#   usage:

import os

from pyecharts import Line

filename = __filename__+'.html'
filepath = 'g:/pyecharts'

attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ]
line = Line("折线图示例")
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
         mark_line=["average"], yaxis_formatter="°C")
line.show_config()
line.render(os.path.join(filepath, filename))

