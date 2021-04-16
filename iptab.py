#!/usr/bin/env python3
import npyscreen

### BEGIN MAIN FORM
class TableList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(TableList, self).__init__(*args, **keywords)
        self.values = ['FILTER','NAT','MANGLE','RAW','SELINUX']

    def actionHighlighted(self, act_on_this, key_press):
        selected_table = self.values[self.cursor_line]
        if   selected_table == "FILTER" :  self.parent.parentApp.setNextForm("FILTER")
        elif selected_table == "NAT"    :  self.parent.parentApp.setNextForm("NAT")
        elif selected_table == "MANGLE" :  self.parent.parentApp.setNextForm("MANGLE")
        elif selected_table == "RAW"    :  self.parent.parentApp.setNextForm("RAW")
        elif selected_table == "SELINUX":  self.parent.parentApp.setNextForm("SELINUX")
        else                            :  self.parent.parentApp.setNextForm(None)
 
class table_Select_Form(npyscreen.Form):
#    def afterEditing(self):
#        self.parentApp.setNextForm(None)

    def create(self):
        self.Table_Choice = self.add(TableList, max_height = 6, name = "Select a table", scroll_exit = True)

### END MAIN FORM
#################################################
## BEGIN CHAIN SELECT FORM
class Filter_Table(npyscreen.Form):
    def create(self):
        self.MSG = self.add(npyscreen.TitleText, name = "FILTER")

class Nat_Table(npyscreen.Form):
    def create(self):
        self.MSG = self.add(npyscreen.TitleText, name = "NAT")

class Mangle_Table(npyscreen.Form):
    def create(self):
        self.MSG = self.add(npyscreen.TitleText, name = "MANGLE")

class Raw_Table(npyscreen.Form):
    def create(self):
        self.MSG = self.add(npyscreen.TitleText, name = "RAW")

class Selinux_Table(npyscreen.Form):
    def create(self):
        self.MSG = self.add(npyscreen.TitleText, name = "SELINUX")


class iptable_Editor(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', table_Select_Form, name ='Select Table')
        self.addForm('FILTER', Filter_Table, name ='FILTER Chain')
        self.addForm('NAT', Nat_Table, name ='NAT Chain')
        self.addForm('MANGLE', Mangle_Table, name ='MANGLE Chain')
        self.addForm('RAW', Raw_Table, name ='RAW Chain')
        self.addForm('SELINUX', Selinux_Table, name ='SELINUX Chain')

if __name__ == '__main__':
    App = iptable_Editor().run()
