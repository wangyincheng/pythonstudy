#!/usr/bin/python env

__author__ = 'wangxiaodong'
__filename__='Polar_test'
# project name:pythonstudy
#   file name:Polar_test
#   auther:wangxiaodong
#   create date:2017/8/2 20:56
#   change auther:
#   change date:
#   version:
#   using enviroment:Django 1.13.0
#   python version:python 3.5.2
#   usage:

import os

import math

from pyecharts import Polar

filename = __filename__+'.html'
filepath = 'g:/pyecharts'

data = []
for i in range(101):
    theta = i / 100 * 360
    r = 5 * (1 + math.sin(theta / 180 * math.pi))
    data.append([r, theta])
hour = [i for i in range(1, 25)]
polar = Polar("极坐标系示例", width=1200, height=600)
polar.add("Love", data, angle_data=hour, boundary_gap=False,start_angle=0)
polar.show_config()
polar.render(os.path.join(filepath, filename))