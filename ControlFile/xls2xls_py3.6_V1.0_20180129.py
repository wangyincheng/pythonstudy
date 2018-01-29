# coding=utf-8
__doc__ = """
输入的excel:包含一个sheet页，列名分别为：'姓名''出生日期''身份证号''地址''电话''性别''单位信息'
输出的excel:包含一个sheet页，列名分别为：'姓名''出生日期''地址''电话(隐藏中间四位)'
"""

import os
import re
import xlrd
import xlwt
from datetime import date

def fromatinputvalue(value):
    """格式化变量"""
    if value == '':
        value = '-'
    elif isinstance(value, unicode):
        value = value.encode('utf-8')
    elif isinstance(value, float):
        value = str(value)
        value = value.decode('gb2312').encode('utf-8')
    elif isinstance(value, int):
        value = str(value)
        value = value.decode('gb2312').encode('utf-8')
    return value

def readXlsx(filename):
    #读取excel文件
    data = xlrd.open_workbook(filename)
    print("read excel %s" % filename)
    #获取工作表
    #table = data.sheets()[0] #通过索引顺序获取
    #table = data.sheet_by_index(0) #通过索引顺序获取
    table = data.sheet_by_name(u'Sheet1')#通过名称获取

    #获取整行和整列的值（数组）
    #table.row_values(i)
    #table.col_values(i)
    #获取行数和列数
    nrows = table.nrows
    ncols = table.ncols
    #循环行列表数据
    outputdata = []
    for i in range(nrows ):
        if i == 0:
            pass
        else:
            outputdata.append([fromatinputvalue(table.row_values(i)[0]),fromatinputvalue(table.row_values(i)[1]),fromatinputvalue(table.row_values(i)[3]),fromatinputvalue(table.row_values(i)[4]).replace('.0','')[:3]+'****'+fromatinputvalue(table.row_values(i)[4]).replace('.0','')[-4:]])
    return outputdata
    #单元格
    #table.cell(rowx,colx)
    #cell_A1 = table.cell(0,0).value
    #cell_C4 = table.cell(3,2).value
    #使用行列索引
    #cell_A1 = table.row(0)[0].value
    #cell_A2 = table.col(1)[0].value
    #简单的写入
    #row = 0
    #col = 0
    # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    #ctype = 1value = '单元格的值'
    #xf = 0# 扩展的格式化
    #table.put_cell(row, col, ctype, value, xf)
    #table.cell(0,0) #单元格的值'
    #table.cell(0,0).value #单元格的值'

def writeExcel(outputpath,filename,outputdata):
    # type: (object, object, object) -> object
    #写入到新文件
    #创建workbook（其实就是excel，后来保存一下就行）
    workbook = xlwt.Workbook(encoding = 'gb2312')
    #创建表
    worksheet = workbook.add_sheet('Sheet1')
    #定义列名
    listName = [u'姓名',u'年龄',u'地址',u'电话(隐藏中间四位)']
    style_date = xlwt.XFStyle()
    style_date.num_format_str = 'YYYY/MM/DD'
    #向第一行写入列名
    j = 0
    for Name in listName:
        worksheet.write(0,j,Name.encode('gb2312'))
        j = j + 1
    #往单元格内写入内容
    j = 1
    for values in outputdata:
        i = 0
        for value in values:
            if i == 1:
                worksheet.write(j, i,value.decode('utf-8').encode('gb2312'),style_date)
            else:
                worksheet.write(j,i,value.decode('utf-8').encode('gb2312'))
            i = i + 1
        j = j + 1
    #保存
    print('保存文件')
    workbook.save(os.path.join(outputpath,filename))
    return True

if __name__ == "__main__":
    # 输入文件路径
    inputfilepath = 'D:/pycharmWorkspace/testspace/inputexcelfile'
    # 修改工作路径到文件路径
    os.chdir(inputfilepath)
    filename = u'人员信息清单1.xls'
    outputdata = readXlsx(filename)
    outputpath = 'D:/pycharmWorkspace/testspace/outputexcelfile'
    result = writeExcel(outputpath,u'输出人员清单1.xls'.encode('gb2312'),outputdata)