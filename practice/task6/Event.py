from Observer import *


class Event:
    def __init__(self, name, old, new, pos):
        self.name = name
        self.old = old
        self.new = new
        self.pos = pos
        self.new_event()

    def new_event(self):
        for i in Observer.static_observers:
            if self.name in i.actions:
                i.actions[self.name](self)

    def __str__(self):
        return " " + str(self.name) + " position ==> " + str(self.pos) + " -> " + ",\t Before:" + \
               str(self.old) + ",\t\t After: " + str(self.new) + " "
