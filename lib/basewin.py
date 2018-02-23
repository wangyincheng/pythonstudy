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
## Class excel_Trancate
###########################################################################

class excel_Trancate(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"excel转换器", pos=wx.DefaultPosition, size=wx.Size(716, 662),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"主测试窗口", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.text_main = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.text_main, 0, wx.ALL, 5)

        self.button_main = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.button_main, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_main.Bind(wx.EVT_BUTTON, self.main_button_click)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def main_button_click(self, event):
        event.Skip()


