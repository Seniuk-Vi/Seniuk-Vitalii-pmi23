

class Observer:
    static_observers = []

    def __init__(self):
        self.static_observers.append(self)
        self.actions = {}

    @property
    def actions(self):
        return self._actions

    @actions.setter
    def actions(self, value):
        self._actions = value

    def add_event(self, event, callback):
        self.actions[event] = callback
