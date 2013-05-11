class PyCommand(object):

    def __init__(self, trigger):
        self.trigger = trigger

    def call(self, args = []):
        print("Debug >> PyCommand call to lower class with args", args)