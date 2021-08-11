#!/usr/bin/env python3
import npyscreen
import iptc

# pointless comment

class OptionsList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(OptionsList, self).__init__(*args, **keywords)
        self.values = ['--- Select A Table ---','filter','nat','mangle','raw','selinux']
        self.tables = self.values

    def actionHighlighted(self, act_on_this, key_press):
        if self.values == self.tables:
            selected_table = self.values[self.cursor_line]
            self.values=['--- Select A Chain ---']
            chains = iptc.easy.dump_table(selected_table, ipv6=False)

            for key in chains: self.values.append(key)
            self.display()

        else:
            self.values = self.tables
            self.name = "--- Select Table ---"
            self.display()

class table_Select_Form(npyscreen.Form):
    def create(self):
        self.Table_Choice = self.add(OptionsList, max_height = 15,scroll_exit = True)

class iptable_Editor(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', table_Select_Form, name ='IP Tables Editor')
if __name__ == '__main__':
    App = iptable_Editor().run()
