import wx
import global_var


class GUI(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self, parent, id, title, size=(800, 380), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.bSizer = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self, size=(500, 75), pos=(0, 0), style=wx.SIMPLE_BORDER)
        self.panel.SetBackgroundColour('#FFFFFF')

        self.Number_Of_Source = wx.StaticText(self.panel, label="Search ", pos=(10, 12))
        self.Number_Of_Source.SetForegroundColour('Black')
        self.font1 = wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.Number_Of_Source.SetFont(self.font1)

        self.txt_search = wx.TextCtrl(self.panel, size=(430, 30), pos=(75, 10))
        self.font = wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.txt_search.SetFont(self.font)

        self.search_limit = wx.StaticText(self.panel, label="Search Limit ", pos=(10, 50))
        self.search_limit.SetForegroundColour('Black')
        self.font1 = wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.search_limit.SetFont(self.font1)

        limit = ['0-100', '101-200', '201-300', '301-400', '401-500','501-1000','1001-2000']
        self.combo = wx.ComboBox(self.panel,size=(110, 30), pos=(130, 50), choices=limit)
        self.combo.Bind(wx.EVT_COMBOBOX, self.combo_value)
        self.font2 = wx.Font(12, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.combo.SetFont(self.font2)

        self.excluded_channel_URL = wx.StaticText(self.panel, label="Excluded Channel URL ", pos=(10, 90))
        self.excluded_channel_URL.SetForegroundColour('Black')
        self.font1 = wx.Font(13, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.excluded_channel_URL.SetFont(self.font1)

        self.txt_area = wx.TextCtrl(self.panel, size=(770, 200), pos=(10, 120), style = wx.TE_MULTILINE|wx.TE_READONLY)
        self.font2 = wx.Font(10, wx.MODERN, wx.NORMAL, wx.NORMAL, False, u'Consolas')
        self.txt_area.SetFont(self.font2)
        textfile_text = open('D:\\Youtube Work\\excluded file.txt', "r")
        textfile_text = textfile_text.read()
        textfile_text_list = textfile_text.split('\n')
        for i in textfile_text_list:
            global_var.channel_link_list.append(i.partition("~")[0].replace(' ',''))
        print('channel_link_list: ', global_var.channel_link_list)
        self.txt_area.AppendText(str(textfile_text))

        self.gobtn = wx.Button(self.panel, label='GO', pos=(530, 12))
        self.gobtn.SetBackgroundColour('#84FF25')
        self.gobtn.Bind(wx.EVT_BUTTON, self.GoBTN_Process)
        self.gobtn.SetForegroundColour('Black')

        self.exitbtn = wx.Button(self.panel, label='EXIT', pos=(650, 12))
        self.exitbtn.SetBackgroundColour('#FF3838')
        self.exitbtn.Bind(wx.EVT_BUTTON, self.Exit)
        self.exitbtn.SetForegroundColour('White')

    def GoBTN_Process(self, event):
        Search_keyword = self.txt_search.GetValue()
        global_var.Search_keyword = str(Search_keyword)

        print('Search Text: ' + global_var.Search_keyword)
        print('Search Limit Selected: '+global_var.dropdown_value)
        from youtube_Work import test
        test()

    def Exit(self, event):
        self.Destroy()

    def combo_value(self,event):
        dropdown_value = self.combo.GetValue()
        global_var.dropdown_value = str(dropdown_value)

app = wx.App()
frame = GUI(parent=None, id=-1, title="All Exe Project")
frame.Show()
app.MainLoop()