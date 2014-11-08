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

    def test_organise_exsiting_dirs(self):
        wx.DirDialog.GetPath = lambda x: 'test_orig'
        event = wx.PyEvent(
            self.win.browse_input_button.GetId(),
            wx.EVT_BUTTON.evtType[0]
        )
        wx.PostEvent(self.win, event)
        self.app.ProcessPendingEvents()

        wx.DirDialog.GetPath = lambda x: 'test_dest'
        event = wx.PyEvent(
            self.win.browse_output_button.GetId(),
            wx.EVT_BUTTON.evtType[0]
        )
        wx.PostEvent(self.win, event)
        self.app.ProcessPendingEvents()

        event = wx.PyEvent(
            self.win.organise_button.GetId(),
            wx.EVT_BUTTON.evtType[0]
        )
        wx.PostEvent(self.win, event)
        self.app.ProcessPendingEvents()

        mainwindow.organise.assert_called_once_with('test_orig', 'test_dest')
