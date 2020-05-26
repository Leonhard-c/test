# !usr/bin/python
# Filename:elsword_crit_max_gui.py

import wx
import validator
import sys
import critAndmax

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(650,460))

        self.Center()

        self.InitSetMenu()
        self.InitUI()

    def InitSetMenu(self):

        # Set icon
        self.icon = wx.Icon()

        # Bottom status
        self.CreateStatusBar()

        # Setting up the menu
        filemenu = wx.Menu()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")

        # Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)

        # Events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

    def InitUI(self):
        # Creating Panel
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        # 第一组暴击网格
        grid_c = wx.GridBagSizer(hgap=10,vgap=10)
        # 暴击网格第一列
        label_crit = wx.StaticText(panel,label="暴击计算")
        grid_c.Add(label_crit, pos=(1,0), flag=wx.LEFT, border=5)
        # 暴击网格第二列
        crit_panel = wx.StaticText(panel, label="面板暴击")
        grid_c.Add(crit_panel, pos=(0,1), flag=wx.LEFT, border=5)
        crit_plus = wx.StaticText(panel, label="加算BUFF")
        grid_c.Add(crit_plus, pos=(1,1), flag=wx.LEFT, border=5)
        crit_multiply = wx.StaticText(panel, label="乘算BUFF")
        grid_c.Add(crit_multiply, pos=(2,1), flag=wx.LEFT, border=5)
        # 暴击网格第三列
        self.crit_panel_input = wx.TextCtrl(panel,-1, validator=validator.MyNumberValidator())
        grid_c.Add(self.crit_panel_input, pos=(0,2), flag=wx.LEFT, border=5)
        self.crit_plus_input = wx.TextCtrl(panel,-1, validator=validator.MyNumberValidator())
        grid_c.Add(self.crit_plus_input, pos=(1,2), flag=wx.LEFT, border=5)
        self.crit_multiply_input = wx.TextCtrl(panel,-1, validator=validator.MyNumberValidator())
        grid_c.Add(self.crit_multiply_input, pos=(2,2), flag=wx.LEFT, border=5)
        # 暴击网格第四列
        button_c = wx.Button(panel,wx.ID_ANY,"计算暴击")
        grid_c.Add(button_c, pos=(0,3), flag=wx.LEFT, border=5)
        button_c_c = wx.Button(panel,wx.ID_ANY,"清空暴击")
        grid_c.Add(button_c_c, pos=(1,3), flag=wx.LEFT, border=5)
        # 暴击网格第五列
        crit_panel_b = wx.StaticText(panel, label="递减前暴击")
        grid_c.Add(crit_panel_b, pos=(0,4), flag=wx.LEFT, border=5)
        crit_plus_a = wx.StaticText(panel, label="递减后暴击")
        grid_c.Add(crit_plus_a, pos=(1,4), flag=wx.LEFT, border=5)
        crit_multiply_f = wx.StaticText(panel, label="最终暴击")
        grid_c.Add(crit_multiply_f, pos=(2,4), flag=wx.LEFT, border=5)
        # 暴击网格第六列
        self.crit_panel_result = wx.TextCtrl(panel,-1, style=wx.TE_READONLY)
        grid_c.Add(self.crit_panel_result, pos=(0,5), flag=wx.LEFT, border=5)
        self.crit_plus_result = wx.TextCtrl(panel,-1, style=wx.TE_READONLY)
        grid_c.Add(self.crit_plus_result, pos=(1,5), flag=wx.LEFT, border=5)
        self.crit_multiply_result = wx.TextCtrl(panel,-1, style=wx.TE_READONLY)
        grid_c.Add(self.crit_multiply_result, pos=(2,5), flag=wx.LEFT, border=5)

        # ----------------------------------------------------------------------------

        # 第二组极大网格
        grid_m = wx.GridBagSizer(hgap=10,vgap=10)
        # 极大网格第一列
        label_max = wx.StaticText(panel,label="极大计算")
        grid_m.Add(label_max, pos=(1,0), flag=wx.LEFT, border=5)
        # 极大网格第二列
        max_panel = wx.StaticText(panel, label="面板极大")
        grid_m.Add(max_panel, pos=(0,1), flag=wx.LEFT, border=5)
        max_plus = wx.StaticText(panel, label="加算BUFF")
        grid_m.Add(max_plus, pos=(1,1), flag=wx.LEFT, border=5)
        max_multiply = wx.StaticText(panel, label="乘算BUFF")
        grid_m.Add(max_multiply, pos=(2,1), flag=wx.LEFT, border=5)
        # 极大网格第三列
        self.max_panel_input = wx.TextCtrl(panel,-1, validator=validator.MyNumberValidator())
        grid_m.Add(self.max_panel_input, pos=(0,2), flag=wx.LEFT, border=5)
        self.max_plus_input = wx.TextCtrl(panel,-1, validator=validator.MyNumberValidator())
        grid_m.Add(self.max_plus_input, pos=(1,2), flag=wx.LEFT, border=5)
        self.max_multiply_input = wx.TextCtrl(panel,-1, validator=validator.MyNumberValidator())
        grid_m.Add(self.max_multiply_input, pos=(2,2), flag=wx.LEFT, border=5)
        # 极大网格第四列
        button_m = wx.Button(panel,wx.ID_ANY,"计算极大")
        grid_m.Add(button_m, pos=(0,3), flag=wx.LEFT, border=5)
        button_m_c = wx.Button(panel, wx.ID_ANY, "清空极大")
        grid_m.Add(button_m_c, pos=(1, 3), flag=wx.LEFT, border=5)
        # 极大网格第四列
        max_panel_b = wx.StaticText(panel, label="递减前极大")
        grid_m.Add(max_panel_b, pos=(0,4), flag=wx.LEFT, border=5)
        max_plus_a = wx.StaticText(panel, label="递减后极大")
        grid_m.Add(max_plus_a, pos=(1,4), flag=wx.LEFT, border=5)
        max_multiply_f = wx.StaticText(panel, label="最终极大")
        grid_m.Add(max_multiply_f, pos=(2,4), flag=wx.LEFT, border=5)
        # 极大网格第五列
        self.max_panel_result = wx.TextCtrl(panel,-1, style=wx.TE_READONLY)
        grid_m.Add(self.max_panel_result, pos=(0,5), flag=wx.LEFT, border=5)
        self.max_plus_result = wx.TextCtrl(panel,-1, style=wx.TE_READONLY)
        grid_m.Add(self.max_plus_result, pos=(1,5), flag=wx.LEFT, border=5)
        self.max_multiply_result = wx.TextCtrl(panel,-1, style=wx.TE_READONLY)
        grid_m.Add(self.max_multiply_result, pos=(2,5), flag=wx.LEFT, border=5)

        vbox.Add((-1, 50))
        vbox.Add(grid_c, flag=wx.ALIGN_CENTER)
        vbox.Add((-1, 50))
        vbox.Add(grid_m, flag=wx.ALIGN_CENTER)
        panel.SetSizer(vbox)


        # 绑定按键
        self.Bind(wx.EVT_BUTTON, self.OnCalculateCrit, button_c)
        self.Bind(wx.EVT_BUTTON, self.OnCalculateMax, button_m)
        self.Bind(wx.EVT_BUTTON, self.OnClearCrit, button_c_c)
        self.Bind(wx.EVT_BUTTON, self.OnClearMax, button_m_c)

    def OnAbout(self, event):
        text = """
例1：CU面板暴击为74.9%，13c裤子强化等级8，在自身buff上齐后是否满暴\n
CU被动有觉醒时20%加算递减buff，以及5%的乘算buff，13c的buff为乘算（8+2）%
面板74.9%代入f(y)换算成递减前暴击为86.5%，加上20%结果为106.5%代入f(x)得此时面板暴击为86.6%，最后乘算86.6*（1+0.05+0.1）=99.59即为最终面板。
99.59＜100，所以没有满暴。\n
例2：CU面板极大为84%，13c鞋子强化等级10，在自身buff上齐后是否满极大\n
CU关于极大的buff只有自己的歼灭纹章加算递减提供15%，点了特性之后提升17.25%，这里取15%。13c提供（10+2）%乘算
84代入f(y)得递减前极大化为108%，加上15%为123%，代入f(x)递减后为90.8%，最后乘算90.8*（1+0.12）=101.696
101.696＞100，所以满极大
"""
        dig = wx.MessageDialog(self, text, "Information for use", wx.OK)
        dig.ShowModal()
        dig.Destroy()

    def OnExit(self, event):
        self.Close(True)

    def OnCalculateCrit(self, event):
        if  (self.crit_panel_input.GetValue() == '' or self.crit_plus_input.GetValue() == '' or self.crit_multiply_input.GetValue() == ''):
            self.DialogBlankError()
        else:
            try:
                crit_panel_value = float(self.crit_panel_input.GetValue())
                crit_plus_value = float(self.crit_plus_input.GetValue())
                crit_multiply_value = float(self.crit_multiply_input.GetValue())
            except:
                self.DialogInputError()
            else:
                try:
                    crit_object = critAndmax.Crit(crit_panel_value)
                    crit_object.beforeCrit()
                    crit_object.plusBuff(crit_plus_value)
                    crit_object.afterCrit()
                    crit_object.multiplyBuff(crit_multiply_value)
                except Exception as e:
                    # print(e.args)
                    self.DialogError(e.args)
                else:
                    self.crit_panel_result.SetValue(str(crit_object.beCrit))
                    self.crit_plus_result.SetValue(str(crit_object.afCrit))
                    self.crit_multiply_result.SetValue(str(crit_object.finalCrit))


    def OnCalculateMax(self, event):
        if (self.max_panel_input.GetValue() == '' or self.max_plus_input.GetValue() == '' or self.max_multiply_input.GetValue() == ''):
            self.DialogBlankError()
        else:

            try:
                max_panel_value = float(self.max_panel_input.GetValue())
                max_plus_value = float(self.max_plus_input.GetValue())
                max_multiply_value = float(self.max_multiply_input.GetValue())
            except:
                self.DialogInputError()
            else:

                try:
                    max_object = critAndmax.Max(max_panel_value)
                    max_object.beforeMax()
                    max_object.plusBuff(max_plus_value)
                    max_object.afterMax()
                    max_object.multiplyBuff(max_multiply_value)
                except Exception as e:
                    # print(e.args)
                    self.DialogError(e.args)
                else:
                    self.max_panel_result.SetValue(str(max_object.beMax))
                    self.max_plus_result.SetValue(str(max_object.afMax))
                    self.max_multiply_result.SetValue(str(max_object.finalMax))

    def DialogError(self, message):
        text1 = ""
        text2 = ""
        if message[0] == 'critvalue':
            text1 = "输入面板暴击不在取值范围内，必须大于0小于100\n"
            text2 = "目前输入值为：" + str(message[1])
        elif message[0] == 'finalCrit':
            text1 = "输入加算暴击值，经计算后不在取值范围内，必须大于0小于140\n"
            text2 = "目前取得值为：" + str(message[1])
        elif message[0] == 'Maxvalue':
            text1 = "输入面板极大不在取值范围内，必须大于0小于100\n"
            text2 = "目前输入值为：" + str(message[1])
        elif message[0] == 'finalMax':
            text1 = "输入加算极大值，经计算后不在取值范围内，必须大于0小于160\n"
            text2 = "目前取得值为：" + str(message[1])

        text = text1 + text2

        dig = wx.MessageDialog(self, text, "Error Information", wx.OK)
        dig.ShowModal()
        dig.Destroy()

    def DialogBlankError(self):
        text = "输入框内容不能为空"
        dig = wx.MessageDialog(self, text, "Error Information", wx.OK)
        dig.ShowModal()
        dig.Destroy()

    def DialogInputError(self):
        text = "输入内容不规范"
        dig = wx.MessageDialog(self, text, "Error Information", wx.OK)
        dig.ShowModal()
        dig.Destroy()

    def OnClearCrit(self, event):
        self.crit_panel_input.Clear()
        self.crit_plus_input.Clear()
        self.crit_multiply_input.Clear()

        self.crit_panel_result.Clear()
        self.crit_plus_result.Clear()
        self.crit_multiply_result.Clear()

    def OnClearMax(self, event):
        self.max_panel_input.Clear()
        self.max_plus_input.Clear()
        self.max_multiply_input.Clear()

        self.max_panel_result.Clear()
        self.max_plus_result.Clear()
        self.max_multiply_result.Clear()


app = wx.App(False)
frame = MainWindow(None, "Elsword Calculator (crit and max)")
frame.Show()
app.MainLoop()
