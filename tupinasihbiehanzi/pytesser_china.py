import sys
print sys.path
#sys.path.append('C:\\Python27\\Lib\\site-packages\\pytesser_v0.0.1')

from pytesser import *
import Image

import os
os.chdir(r'D:\pycharmworkspace\image')
print os.getcwd()
im = Image.open('fnord.tif')
text = image_to_string(im)
print text
# try:
# 	text = image_file_to_string('fnord.tif', graceful_errors=False)
# except errors.Tesser_General_Exception, value:
# 	print "fnord.tif is incompatible filetype.  Try graceful_errors=True"
# 	print value
# text = image_file_to_string('fnord.tif', graceful_errors=True)
# print "fnord.tif contents:", text
# text = image_file_to_string('fonts_test.png', graceful_errors=True)
# print text
