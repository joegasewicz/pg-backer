import wx

from screens import (
    HomeScreen,
)
from frames.main_frame import MainFrame
from utils.database import engine
from utils.logger import logger
from models import (
    Model,
)


class PGBacker(wx.App):

    def OnInit(self):
        # Create tables
        logger.info("Creating sqlite tables")
        Model.metadata.create_all(engine)
        # Display screens
        self.frame = MainFrame()
        self.frame.Show()
        return True
