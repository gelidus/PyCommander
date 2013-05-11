PyCommander
===========

PyCommander is a simple system for organizing commands. This example shows how it work: 

```python
from PyCommandTable import PyCommandTable
from PyCommand import PyCommand

class MyCommand(PyCommand): # we are defining new class on top of the PyCommand
    def __init__(self):
        super(MyCommand, self).__init__('$') # initing trigger, the $(dolar) sign will be the trigger

    def call(self,args):
        print("This was called!", args)


table = PyCommandTable() # we create a new table

command = MyCommand() #creating instance of our command

table.add(command) # we add our command to the table

table.call('$') # output >> This was called! []

table.call('$', [1,2,3]) # output >> This was called! [1,2,3]

```
