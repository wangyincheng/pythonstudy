# -*- coding: UTF-8 -*-
import wx
import getexcel
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class MianWindow(getexcel.GetExcelFile):
    # 首先，咱们从刚刚源文件中将主窗体继承下来.就是修改过name属性的主窗体咯。
    def init_main_window(self):
        self.mian_text.SetValue(u'D:/pycharmWorkspace/testspace/inputexcelfile/人员信息清单1.xls')

    def clearmaintext_button(self, event):
        self.mian_text.Clear()


if __name__ == '__main__':
    app = wx.App()

    main_win = MianWindow(None)
    main_win.init_main_window()
    main_win.Show()
    app.MainLoop()