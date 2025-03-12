import wx

from screens import (
    HomeScreen,
)


class PGBacker(wx.App):

    def OnInit(self):
        self.frame = HomeScreen()
        self.frame.Show()
        return True
