class CareTaker:

    def __init__(self, originator, max_size, collection):
        self.max_size = max_size
        self._originator = originator
        self.undos = []
        self.redos = []
        self.current_collection = collection

    def create(self):
        memento = self._originator.memento
        if self.max_size > 0:
            if len(self.undos) == self.max_size:
                self.undos.pop(0)
            self.undos.append(memento)
            self.redos = []

    def undo(self):
        if len(self.undos) < 2:
            raise AttributeError("Save first")
        redo = self.undos.pop()
        self.redos.append(redo)
        ret_mem = self.undos.pop()
        self.current_collection.copy(ret_mem)
        self.undos.append(ret_mem)

    """
    Can't redo
    """

    def redo(self):
        if len(self.redos) < 1:
            raise AttributeError("No redo options")
        redo = self.redos.pop()
        self.undos.append(redo)
        self.current_collection.copy(redo)
