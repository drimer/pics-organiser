import unittest

import mock
import wx

from src.ui import mainwindow


class TestMainWindow(unittest.TestCase):

    def setup_mocks(self):
        self.backups = {
            'wx.DirDialog.ShowModal': wx.DirDialog.ShowModal,
            'mainwindow.organise': mainwindow.organise,
        }

        wx.DirDialog.ShowModal = lambda x: wx.ID_OK
        mainwindow.organise = mock.MagicMock(wraps=mainwindow.organise)

    def setUp(self):
        self.setup_mocks()
        self.app = wx.App()
        self.win = mainwindow.MainWindow()

    def tearDown(self):
        mainwindow.organise = self.backups['mainwindow.organise']
        wx.DirDialog.ShowModal = self.backups['wx.DirDialog.ShowModal']

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

        mainwindow.organise.assert_called_once_with('test_orig', 'test_dest')
