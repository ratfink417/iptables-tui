#!/usr/bin/env python3
import npyscreen
import iptc

# chains = iptc.easy.dump_table('filter', ipv6=False)
# for key in chains:
#     print(key)
# rules  = iptc.easy.dump_chain('filter', 'OUTPUT', ipv6=False)

## BEGIN MAIN FORM
class TableList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(TableList, self).__init__(*args, **keywords)
        self.values = ['filter','nat','mangle','raw','selinux']

    def actionHighlighted(self, act_on_this, key_press):
        selected_table = self.values[self.cursor_line]
        self.values=[]
        chains = iptc.easy.dump_table(selected_table, ipv6=False)

        for key in chains:
            self.values.append(key)

        self.display()

class table_Select_Form(npyscreen.Form):
    def create(self):
        self.Table_Choice = self.add(TableList, max_height = 15, name = "Select a table", scroll_exit = True)


class iptable_Editor(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', table_Select_Form, name ='Select Table')
if __name__ == '__main__':
    App = iptable_Editor().run()
