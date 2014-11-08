import os

import wx


class MainWindow(wx.Frame):
    def __init__(self, title="Window"):
        super(MainWindow, self).__init__(None, title=title, size=(400, 100))
        self.panel = wx.Panel(self)

        top_sizer = wx.BoxSizer(wx.VERTICAL)
        dirs_grid = wx.GridSizer(cols=2)

        dir_to_sort_text = wx.StaticText(self.panel, label='Carpeta a ordenar')
        dirs_grid.Add(dir_to_sort_text, flag=wx.EXPAND)

        self.dir_to_sort_input = wx.TextCtrl(self.panel)
        dirs_grid.Add(self.dir_to_sort_input, flag=wx.EXPAND)

        dir_destination_text = wx.StaticText(self.panel, label='Nueva carpeta para fotos ordenadas')
        dirs_grid.Add(dir_destination_text, flag=wx.EXPAND)

        self.dir_destination_input = wx.TextCtrl(self.panel)
        dirs_grid.Add(self.dir_destination_input, flag=wx.EXPAND)

#        self.SetSizeHints(250, 150, 250, 150)
#        self.SetSizeHints(100, 100, 100, 100)

        self.organise_button = wx.Button(self.panel, label='Ordenar')
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.organise_button, flag=wx.ALIGN_CENTER)

        top_sizer.Add(dirs_grid, flag=wx.EXPAND)
        top_sizer.Add(button_sizer, flag=wx.ALIGN_CENTER)
        self.panel.SetSizer(top_sizer)

        self.setup_handlers()

    def setup_handlers(self):
        self.Bind(wx.EVT_BUTTON, self.on_organise, self.organise_button)

    def on_organise(self, event):
        print 'Organise'
