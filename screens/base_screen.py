import wx


class BaseScreen(wx.Panel):

    # Reference to the main frame
    main_sizer: wx.BoxSizer

    def __init__(self, parent, frame):
        super().__init__(parent)
        self.frame = frame

        # Top Bar with Back & Forward Buttons
        self.nav_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.back_button = wx.Button(self, label="←", size=(50, 30))
        self.forward_button = wx.Button(self, label="→", size=(50, 30))

        self.back_button.Bind(wx.EVT_BUTTON, self.frame.go_back)
        self.forward_button.Bind(wx.EVT_BUTTON, self.frame.go_forward)

        self.nav_sizer.Add(self.back_button, flag=wx.ALL, border=5)
        self.nav_sizer.Add(self.forward_button, flag=wx.ALL, border=5)

        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.Add(self.nav_sizer, flag=wx.ALIGN_LEFT | wx.TOP, border=10)

    def update_navigation_buttons(self):
        self.back_button.Enable(self.frame.current_index > 0)
        self.forward_button.Enable(self.frame.current_index < len(self.frame.history) - 1)
