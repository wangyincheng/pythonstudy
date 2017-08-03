#!/usr/bin/python env

__author__ = 'wangxiaodong'
__filename__ = 'Polar_test2'

# project name:pythonstudy
#   file name:Polar_test2
#   auther:wangxiaodong
#   create date:2017/8/2 21:04
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
for i in range(361):
    t = i / 180 * math.pi
    r = math.sin(2 * t) * math.cos(2 * t)
    data.append([r, i])
polar = Polar("极坐标系示例", width=1200, height=600)
polar.add("Color-Flower", data, start_angle=0, symbol=None, axis_range=[0, None],
          area_color="#f71f24", area_opacity=0.6)
polar.show_config()
polar.render(os.path.join(filepath, filename))