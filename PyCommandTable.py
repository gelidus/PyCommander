from PyCommand import PyCommand

class PyCommandTable(object):

    _commands = { }

    def __init__(self, commands = []):
        if commands is None:
            self._commands = []
        else:
            for com in commands:
                self._commands[com.trigger] = com

    def call(self, trigger, args = []):
        if trigger in self._commands:
        	self._commands[trigger].call(args)

    def add(self, command):
        if isinstance(command, PyCommand):
            self._commands[command.trigger] = command

    def remove(self, trigger):
        if trigger in self._commands:
            del self._commands[trigger]