import wx
from screens.home_screen import HomeScreen


class MainFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title="PG Backer", size=(800, 600))

        self.panel = wx.Panel(self)
        self.history = []
        # Track current position in history
        self.current_index = -1

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        # load home screen
        self.add_to_history(HomeScreen)
        self.Center()
        self.Show()

    def go_back(self, event):
        if self.current_index > 0:
            self.current_index -= 1
            self.replace_screen(self.history[self.current_index])

    def go_forward(self, event):
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            self.replace_screen(self.history[self.current_index])

    def add_to_history(self, screen_class):
        self.current_index += 1
        # Clear forward history if moving forward
        self.history = self.history[:self.current_index]
        self.history.append(screen_class)

        self.replace_screen(screen_class)

    def replace_screen(self, screen_class):
        # Replace current UI with the new screen
        self.panel.DestroyChildren()

        # Ensure each screen gets panel & frame references
        new_screen = screen_class(self.panel, self)

        # Check if panel already has a sizer, clear it
        if self.panel.GetSizer():
            self.panel.GetSizer().Clear(True)

        # create a new sizer for the new screen
        new_sizer = wx.BoxSizer(wx.VERTICAL)
        new_sizer.Add(new_screen, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Apply the new sizer to the panel
        self.panel.SetSizerAndFit(new_sizer)
        self.panel.Layout()

        new_screen.update_navigation_buttons()
