import unittest
try:
    import mock
    import wx
except ImportError:
    from pprint import pprint
    import sys
    pprint(sys.path)

from src import picture
from src.ui import mainwindow


class TestMainWindow(unittest.TestCase):

    def setup_mocks(self):
        self.backups.update({
            'ShowModal': wx.DirDialog.ShowModal,
            '__init__': picture.PicturesCollection.__init__,
            'sort_into_folder': picture.PicturesCollection.sort_into_folder,
        })

        wx.DirDialog.ShowModal = lambda x: wx.ID_OK
        picture.PicturesCollection.__init__ = mock.MagicMock(return_value=None)
        picture.PicturesCollection.sort_into_folder = mock.MagicMock()

    def setUp(self):
        self.backups = {}
        self.setup_mocks()
        self.app = wx.App()
        self.win = mainwindow.MainWindow()

    def tearDown(self):
        PC = picture.PicturesCollection
        PC.__init__ = self.backups.get('__init__', PC.__init__)
        PC.sort_into_folder = self.backups.get('sort_into_folder',
                                               PC.sort_into_folder)
        wx.DirDialog.ShowModal = self.backups.get('ShowModal',
                                                  wx.DirDialog.ShowModal)

    def raise_button_clicked_event(self, button_name):
        button = getattr(self.win, button_name)
        event = wx.PyEvent(
            button.GetId(),
            wx.EVT_BUTTON.evtType[0]
        )
        wx.PostEvent(self.win, event)
        self.app.ProcessPendingEvents()

    def test_organise_existing_dirs(self):
        wx.DirDialog.GetPath = lambda x: 'test_orig'
        self.raise_button_clicked_event('input_path_button')

        wx.DirDialog.GetPath = lambda x: 'test_dest'
        self.raise_button_clicked_event('output_path_button')

        self.raise_button_clicked_event('organise_button')

        PC = picture.PicturesCollection
        PC.__init__.assert_called_once_with('test_orig')
        PC.sort_into_folder.assert_called_once_with('test_dest')
