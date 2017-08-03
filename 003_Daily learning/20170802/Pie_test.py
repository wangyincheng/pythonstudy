#!/usr/bin/python env

__author__ = 'wangxiaodong'
__filename__ = 'Pie_test'

# project name:pythonstudy
#   file name:Pie_test
#   auther:wangxiaodong
#   create date:2017/8/2 21:08
#   change auther:
#   change date:
#   version:
#   using enviroment:Django 1.13.0
#   python version:python 3.5.2
#   usage:

import os


filename = __filename__+'.html'
filepath = 'g:/pyecharts'

from pyecharts import Pie

pie = Pie("饼图示例", title_pos='center', width=1000, height=600)
pie.add("", ['A', 'B', 'C', 'D', 'E', 'F'], [335, 321, 234, 135, 251, 148], radius=[40, 55],is_label_show=True)
pie.add("", ['H', 'I', 'J'], [335, 679, 204], radius=[0, 30], legend_orient='vertical', legend_pos='left')
pie.show_config()
pie.render(os.path.join(filepath, filename))