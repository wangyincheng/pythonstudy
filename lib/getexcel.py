# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class GetExcelFile
###########################################################################

class GetExcelFile(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"获取excel文件", pos=wx.DefaultPosition,
                          size=wx.Size(554, 148), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        getexcelsize = wx.GridSizer(0, 3, 0, 0)

        self.main_text_note = wx.StaticText(self, wx.ID_ANY, u"请选择要转换的文件：", wx.DefaultPosition, wx.DefaultSize,
                                            0 | wx.ALWAYS_SHOW_SB | wx.TRANSPARENT_WINDOW)
        self.main_text_note.Wrap(-1)
        getexcelsize.Add(self.main_text_note, 0, wx.ALL, 5)

        self.mian_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        getexcelsize.Add(self.mian_text, 0, wx.ALL, 5)

        self.browser_button = wx.Button(self, wx.ID_ANY, u"浏览", wx.DefaultPosition, wx.DefaultSize, 0)
        getexcelsize.Add(self.browser_button, 0, wx.ALL, 5)

        self.clearmaintext = wx.Button(self, wx.ID_ANY, u"清除", wx.DefaultPosition, wx.DefaultSize, 0)
        getexcelsize.Add(self.clearmaintext, 0, wx.ALL, 5)

        self.next_button_getexcel = wx.Button(self, wx.ID_ANY, u"下一步", wx.DefaultPosition, wx.DefaultSize, 0)
        getexcelsize.Add(self.next_button_getexcel, 0, wx.ALL, 5)

        self.exit_button = wx.Button(self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0)
        getexcelsize.Add(self.exit_button, 0, wx.ALL, 5)

        self.SetSizer(getexcelsize)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.browser_button.Bind(wx.EVT_BUTTON, self.getpath)
        self.clearmaintext.Bind(wx.EVT_BUTTON, self.clearmaintext_button)
        self.exit_button.Bind(wx.EVT_BUTTON, self.exit_program)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def getpath(self, event):
        event.Skip()

    def clearmaintext_button(self, event):
        event.Skip()

    def exit_program(self, event):
        event.Skip()


