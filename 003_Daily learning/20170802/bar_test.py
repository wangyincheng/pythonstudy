#!/usr/bin/python env

__author__ = 'wangxiaodong'
# project name:pythonstudy
#   file name:bar_test
#   auther:wangxiaodong
#   create date:2017/8/2 20:38
#   change auther:
#   change date:
#   version:
#   using enviroment:Django 1.13.0
#   python version:python 3.5.2
#   usage:

import os

from pyecharts import Bar

filename = 'bar_test.html'
filepath = 'g:/pyecharts'


bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
bar.render(os.path.join(filepath, filename))