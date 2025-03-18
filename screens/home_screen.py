import wx
from screens.base_screen import BaseScreen
from screens.create_dump_screen import CreateDumpScreen


class HomeScreen(BaseScreen):

    def __init__(self, parent, frame):
        super().__init__(parent, frame)
        # Title
        title = wx.StaticText(self, label="Welcome to PG Backer")
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title.SetFont(font)
        self.main_sizer.Add(title, flag=wx.ALIGN_CENTRE | wx.TOP, border=20)

        # Navigation Buttons
        self.create_dump_button = wx.Button(self, label="Create Database Dump", size=(200, 40))
        self.create_dump_button.Bind(wx.EVT_BUTTON, self.open_create_screen)

        self.main_sizer.Add(self.create_dump_button, flag=wx.ALIGN_CENTRE | wx.ALL, border=20)

        self.SetSizerAndFit(self.main_sizer)

    def open_create_screen(self, event):
        self.frame.add_to_history(lambda parent, frame: CreateDumpScreen(parent, frame))
