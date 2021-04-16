#!/usr/bin/env python3
import npyscreen


class TableList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(TableList, self).__init__(*args, **keywords)
        self.values = ['FILTER','NAT','MANGLE','RAW','SELINUX']

    def actionHighlighted(self, act_on_this, key_press):
        self.parent.T.name = "CHANGED"
        self.parent.T.display()

class table_Select_Form(npyscreen.Form):
    def afterEditing(self):
        self.T.name = "CHANGED"
        self.T.display()
        #self.parentApp.setNextForm(None)

    def create(self):
        self.T = self.add(npyscreen.TitleFixedText, name = "Change Me!",)
        self.L = self.add(TableList, max_height = 6, name = "Select a table", scroll_exit = True)

class iptable_Editor(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', table_Select_Form, name ='Select Table')

if __name__ == '__main__':
    App = iptable_Editor().run()
