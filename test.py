import PyCommand
import PyCommandTable

class MyCommand(PyCommand.PyCommand): # we are defining new class on top of the PyCommand

    def __init__(self):
        super().__init__('$') # initing trigger, the $(dolar) sign will be the trigger

    def call(self,args):
        print("This was called!", args)


table = PyCommandTable.PyCommandTable() # we create a new table

command = MyCommand() #creating instance of our command

table.add(command) # we add our command to the table

subCommand = MyCommand()
command.bindSubCommand(subCommand)

#subSubCommand= MyCommand() #third command test
#subCommand.bindSubCommand(subSubCommand)

table.call('$',['$', '$', 1, 2]) # output >> This was called! ['$', 1, 2]