#!/usr/bin/python

from src.ui.mainwindow import MainWindow

import wx


def main():
    app = wx.App()
    window = MainWindow()
    window.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
