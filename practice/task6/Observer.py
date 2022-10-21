from Logger import *


class Observer:
    observers = []

    def __init__(self):
        self.observers.append(self)
        self.actions = {}

    def add_event(self, event, callback):
        self.actions[event] = callback
