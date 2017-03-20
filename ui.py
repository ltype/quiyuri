import wx

import config


class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, wx.ID_ANY, title=title, pos=(150, 150), size=(400, 300))
        panel = wx.Panel(self, wx.ID_ANY)

        self.combo = wx.ComboBox(panel, choices=[])
        self.combo.SetSelection(0)
        self.btn_add = wx.Button(panel, label=config.add)
        self.btn_remove = wx.Button(panel, label=config.remove)
        self.tips = wx.StaticText(panel, label=config.tips)
        self.lst = wx.ListBox(panel, size=(50, 150), style=wx.LB_SINGLE)
        self.lst.AlwaysShowScrollbars(hflag=False, vflag=True)
        self.cb = wx.CheckBox(panel, label=config.checkbox, style=wx.TEXT_ALIGNMENT_RIGHT)
        self.cb.SetValue(True)

        bsizer_header = wx.BoxSizer(wx.HORIZONTAL)
        bsizer_tips = wx.BoxSizer(wx.HORIZONTAL)
        bsizer_lst = wx.BoxSizer(wx.HORIZONTAL)
        bsizer_footer = wx.BoxSizer(wx.HORIZONTAL)
        bsizer_header.Add(self.combo, proportion=2, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)
        bsizer_header.Add(self.btn_add, proportion=1, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)
        bsizer_header.Add(self.btn_remove, proportion=1, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)
        bsizer_tips.Add(self.tips, proportion=2, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)
        bsizer_lst.Add(self.lst, proportion=2, flag=wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_LEFT, border=5)
        bsizer_footer.Add(self.cb, proportion=2, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT, border=5)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(bsizer_header, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        box.Add(bsizer_tips, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        box.Add(bsizer_lst, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
        box.Add(bsizer_footer, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

        self.Bind(wx.EVT_BUTTON, self.on_btn_add, self.btn_add)
        self.Bind(wx.EVT_BUTTON, self.on_btn_remove, self.btn_remove)

        panel.SetSizer(box)

    def refresh_cb(self, sessions):
        self.combo.Clear()
        for k, v in sessions.items():
            self.combo.Append(v.Process.name(), v)

    def on_btn_add(self, event):
        items = self.lst.GetItems()
        selected = self.combo.GetClientData(self.combo.GetSelection())
        if not selected.Process.name() in items:
            self.lst.Append(selected.Process.name())

    def on_btn_remove(self, event):
        if self.lst.GetSelection() >= 0:
            self.lst.Delete(self.lst.GetSelection())