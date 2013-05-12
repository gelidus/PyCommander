import PyCommand

class PyCommandTable(object):

    def __init__(self, commands = []):
        self._commands = { }
        if commands is not None:
            for com in commands:
                self._commands[com.trigger] = com

    def call(self, trigger, args = []):
        if trigger in self._commands:
        	self._commands[trigger].invoke(args)

    def add(self, command):
        if isinstance(command, PyCommand.PyCommand):
            self._commands[command.trigger] = command

    def remove(self, trigger):
        if trigger in self._commands:
            del self._commands[trigger]
