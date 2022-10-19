from Memento import *

class Originator:

    def __init__(self):
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):        self._state = state

    @property
    def memento(self):
        return Memento(self.state.mas, self.state.file_name)

    @memento.setter
    def memento(self, memento):
        self._state = memento.state

