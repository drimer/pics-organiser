import os

import wx


def organise(src, dest):
    print 'Organising %s into %s' % (src, dest)


class MainWindow(wx.Frame):
    def __init__(self, title="Window"):
        super(MainWindow, self).__init__(None, title=title, size=(700, 100))
        self.panel = wx.Panel(self)

        self.input_path_label = wx.StaticText(self.panel, label='Carpeta a ordenar')
        self.input_path_text = wx.TextCtrl(self.panel)
        self.input_path_text.WriteText(os.getcwd())
        self.input_path_button = wx.Button(self.panel, label='BROWSE')
        self.output_path_label = wx.StaticText(self.panel, label='Nueva carpeta para fotos ordenadas')
        self.output_path_text = wx.TextCtrl(self.panel)
        self.output_path_text.WriteText(os.getcwd())
        self.output_path_button = wx.Button(self.panel, label='BROWSE')
        self.organise_button = wx.Button(self.panel, label='Ordenar')

        top_sizer = wx.BoxSizer(wx.VERTICAL)
        paths_grid = wx.GridSizer(cols=3)
        paths_grid.Add(self.input_path_label, flag=wx.EXPAND)
        paths_grid.Add(self.input_path_text, flag=wx.EXPAND)
        paths_grid.Add(self.input_path_button)
        paths_grid.Add(self.output_path_label, flag=wx.EXPAND)
        paths_grid.Add(self.output_path_text, flag=wx.EXPAND)
        paths_grid.Add(self.output_path_button)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(self.organise_button, flag=wx.ALIGN_CENTER)

        top_sizer.Add(paths_grid, flag=wx.EXPAND|wx.ALIGN_CENTER)
        top_sizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
        top_sizer.Add(button_sizer, flag=wx.ALIGN_CENTER)
        self.panel.SetSizer(top_sizer)

        self.setup_handlers()

    def setup_handlers(self):
        self.Bind(wx.EVT_BUTTON, self.on_browse_input_dir, self.input_path_button)
        self.Bind(wx.EVT_BUTTON, self.on_browse_output_dir, self.output_path_button)
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
        return self.input_path_text.GetValue()

    def get_dest_path(self):
        return self.output_path_text.GetValue()

    def update_source_path(self, source_path):
        self.input_path_text.SetValue(source_path)

    def update_dest_path(self, source_path):
        self.output_path_text.SetValue(source_path)

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
