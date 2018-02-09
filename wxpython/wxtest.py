# coding=utf-8
#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# see also:  https://wxpython.org/Phoenix/docs/html/wx.lib.agw.persist.html#persistent-overview
import sys
if __name__ == '__main__':
    import wx , os
    import wx.lib.agw.persist as PM

    class xf(wx.Frame):
        def __init__(self, parent):
            wx.Frame.__init__(self, parent, -1, " window maintains size and position after restart ")

            self.Bind(wx.EVT_CLOSE, self.OnClose)

            self._persistMgr = PM.PersistenceManager.Get()
            _configFile = os.path.join(os.getcwd(), "persist-saved-cfg")    # getname()
            self._persistMgr.SetPersistenceFile(_configFile)
            if not self._persistMgr.RegisterAndRestoreAll(self): print (" no workie  ")

        def OnClose(self, event):
            self._persistMgr.SaveAndUnregister()
            event.Skip()

    a = wx.App()
    f = xf(None)
    selff  =f
    parenta=a

    p=a.Traits.StandardPaths.Get()
    print  (str(                         wx.GetUserHome()                  )) #  /home/...
    print  (str(                         wx.StandardPaths.GetDataDir(p)    )) #  /usr/share/main
    uh=  wx.GetUserHome()
    dd=  wx.StandardPaths.GetDataDir(p)  # this .py src works with python3 as well as python2

    f.Show    ()
    a.MainLoop()
