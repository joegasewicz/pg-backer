import wx

from widgets import LogPanel
from screens.base_screen import BaseScreen


class CreateDumpScreen(BaseScreen):
    grid_sizer: wx.FlexGridSizer
    button_sizer: wx.BoxSizer

    def __init__(self, parent, frame):
        super().__init__(parent, frame)

        self.grid_sizer = wx.FlexGridSizer(rows=6, cols=2, vgap=15, hgap=15)
        self.button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Make inputs stretch horizontally
        self.grid_sizer.AddGrowableCol(1, proportion=1)
        self.main_sizer.Add(self.grid_sizer, flag=wx.ALL | wx.EXPAND, border=30)

        # Fields
        self.input_host = self.label_and_text_field(text="Database Host")
        self.input_username = self.label_and_text_field(text="Database Username")
        self.input_password = self.label_and_text_field(text="Database Password")
        self.input_port = self.label_and_text_field(text="Database Port")
        self.input_name = self.label_and_text_field(text="Database Name")

        # File Picker Field
        label_file = wx.StaticText(self, label="Dump File")
        self.file_sizer = wx.BoxSizer(wx.HORIZONTAL)  # Horizontal sizer for input button
        self.input_file = wx.TextCtrl(self, style=wx.TE_READONLY)
        self.browser_button = wx.Button(self, label="Browse")

        # Bind Picker event
        self.browser_button.Bind(wx.EVT_BUTTON, self.on_browse)

        self.file_sizer.Add(self.input_file, proportion=1,  flag=wx.EXPAND | wx.RIGHT, border=5)
        self.file_sizer.Add(self.browser_button, flag=wx.EXPAND)

        self.grid_sizer.Add(label_file, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        self.grid_sizer.Add(self.file_sizer, flag=wx.EXPAND)

        # Log Panel
        self.log_output = LogPanel(self)
        self.main_sizer.Add(self.log_output, flag=wx.ALL | wx.EXPAND, border=10, proportion=1)

        # Buttons
        self.dump_button = wx.Button(self, label="Dump", size=(120, 40))
        self.cancel_button = wx.Button(self, label="Cancel", size=(120, 40))

        self.button_sizer.Add(self.cancel_button, flag=wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, border=10)
        self.button_sizer.AddStretchSpacer(1)  # Push the dump button to the right
        self.button_sizer.Add(self.dump_button, flag=wx.ALIGN_CENTER_VERTICAL)
        self.dump_button.Bind(wx.EVT_BUTTON, self.start_dump)

        self.main_sizer.Add(self.button_sizer, flag=wx.ALL | wx.EXPAND, border=30)

        # self.SetSizer(self.main_sizer)
        # self.main_sizer.Fit(self)
        # self.Center()
        self.SetSizerAndFit(self.main_sizer)

    def label_and_text_field(self, *, text: str):
        label = wx.StaticText(self, label=text)
        _input = wx.TextCtrl(self)

        self.grid_sizer.Add(label, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        self.grid_sizer.Add(_input, flag=wx.EXPAND)

        return _input

    def on_browse(self, event):
        # open file dialog
        dialog = wx.FileDialog(
            self,
            "Select dump file",
            wildcard="All files (*.*)|*.*",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        )
        if dialog.ShowModal() == wx.ID_OK:
            # Set selected file path
            self.input_file.SetValue(dialog.GetPath())
        dialog.Destroy()

    def start_dump(self, event):
        self.log_output.log("Starting PostgreSQL backup...")
        wx.CallLater(1000, lambda: self.log_output.log("Connecting to database..."))
