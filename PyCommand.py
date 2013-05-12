import PyCommandTable

class PyCommand(object):

    def __init__(self, trigger):
        self.trigger = trigger
        self._subCommands = { }

    def invoke(self, args):
        if len(self._subCommands) > 0 and len(args) > 0 and args[0] in self._subCommands:
            self._subCommands[args[0]].invoke(args[1:])
        else:
            self.call(args)


    def call(self, args = []):
        print("Debug >> PyCommand call to lower class with args", args)

    def bindSubCommand(self, command):
        if command not in self._subCommands:
            self._subCommands[command.trigger] = command