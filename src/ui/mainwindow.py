import os

import wx


def organise(src, dest):
    print 'Organising %s into %s' % (src, dest)


class MainWindow(wx.Frame):
    def __init__(self, title="Window"):
        super(MainWindow, self).__init__(None, title=title, size=(700, 100))
        self.panel = wx.Panel(self)

        top_sizer = wx.BoxSizer(wx.VERTICAL)
        dirs_grid = wx.GridSizer(cols=3)

        dir_to_sort_text = wx.StaticText(self.panel, label='Carpeta a ordenar')
        dirs_grid.Add(dir_to_sort_text, flag=wx.EXPAND)

        self.dir_to_sort_input = wx.TextCtrl(self.panel)
        self.dir_to_sort_input.WriteText(os.getcwd())
        dirs_grid.Add(self.dir_to_sort_input, flag=wx.EXPAND)

        self.browse_input_button = wx.Button(self.panel, label='BROWSE')
        dirs_grid.Add(self.browse_input_button)

        dir_destination_text = wx.StaticText(self.panel, label='Nueva carpeta para fotos ordenadas')
        dirs_grid.Add(dir_destination_text, flag=wx.EXPAND)

        self.dir_destination_input = wx.TextCtrl(self.panel)
        self.dir_destination_input.WriteText(os.getcwd())
        dirs_grid.Add(self.dir_destination_input, flag=wx.EXPAND)

        self.browse_output_button = wx.Button(self.panel, label='BROWSE')
        dirs_grid.Add(self.browse_output_button)

        self.organise_button = wx.Button(self.panel, label='Ordenar')
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.organise_button, flag=wx.ALIGN_CENTER)

        top_sizer.Add(dirs_grid, flag=wx.EXPAND|wx.ALIGN_CENTER)
        top_sizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        top_sizer.Add(button_sizer, flag=wx.ALIGN_CENTER)
        self.panel.SetSizer(top_sizer)

        self.setup_handlers()

    def setup_handlers(self):
        self.Bind(wx.EVT_BUTTON, self.on_browse_input_dir, self.browse_input_button)
        self.Bind(wx.EVT_BUTTON, self.on_browse_output_dir, self.browse_output_button)
        self.Bind(wx.EVT_BUTTON, self.on_organise, self.organise_button)

    def on_organise(self, event):
        organise(self.get_source_path(), self.get_dest_path())

    def on_browse_input_dir(self, event):
        print 'on_browse_input_dir()'
        dialog = wx.DirDialog(
            self,
            message='Elige un directorio',
            defaultPath=self.get_source_path(),
            style=wx.OPEN
        )
        status = dialog.ShowModal()
        if status == wx.ID_OK:
            self.update_source_path(dialog.GetPath())
        dialog.Destroy()

    def get_source_path(self):
        return self.dir_to_sort_input.GetValue()

    def get_dest_path(self):
        return self.dir_destination_input.GetValue()

    def update_source_path(self, source_path):
        self.dir_to_sort_input.SetValue(source_path)

    def update_dest_path(self, source_path):
        self.dir_destination_input.SetValue(source_path)

    def on_browse_output_dir(self, event):
        dialog = wx.DirDialog(
            self,
            message='Elige un directorio',
            defaultPath=self.get_dest_path(),
            style=wx.OPEN
        )
        status = dialog.ShowModal()
        if status == wx.ID_OK:
            self.update_dest_path(dialog.GetPath())
        dialog.Destroy()
