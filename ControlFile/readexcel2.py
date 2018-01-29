# coding=utf-8
import os
import xlrd



#decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode(‘gb2312’)，表示将gb2312编码的字符串转换成unicode编码。
#encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode(‘gb2312’)，表示将unicode编码的字符串转换成gb2312编码。
# 输入文件路径
inputfilepath = 'D:/pycharmWorkspace/testspace/inputexcelfile'
# 修改工作路径到文件路径
os.chdir(inputfilepath)
# 读取excel文件
data = xlrd.open_workbook(u"D:/pycharmWorkspace/testspace/inputexcelfile/人员信息清单1.xlsx")

table = data.sheet_by_name(u'Sheet1')

nrows_num = table.nrows

ncols_num = table.ncols

res = []

for nrows in range(nrows_num):
    for ncols in range(ncols_num):

        cell_value = table.cell(nrows, ncols).value

        if cell_value == '':
            cell_value = '__'
            res.append(cell_value)
        elif isinstance(cell_value, unicode):
            cell_value = cell_value.encode('utf-8')
            res.append(cell_value)
        elif isinstance(cell_value, float):
            cell_value = str(cell_value)
            cell_value = cell_value.decode('gb2312').encode('utf-8')
            res.append(cell_value)
        elif isinstance(cell_value, int):
            cell_value = str(cell_value)
            cell_value = cell_value.decode('gb2312').encode('utf-8')
            res.append(cell_value)
    res.append('|')

res = ','.join(res)
res = res.split('|')

for i in range(len(res) - 1):
    print '第', i + 1, '行数据：', res[i].strip(',')
