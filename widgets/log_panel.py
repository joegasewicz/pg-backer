import wx


class LogPanel(wx.TextCtrl):

    def __init__(self, parent):
        super().__init__(parent, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        self.SetBackgroundColour("#1e1e1e")
        self.SetForegroundColour("#ffffff")
        self.SetFont(wx.Font(10, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))

    def log(self, message: str):
        self.AppendText(f"{message}\n")
