from Gatter import Gatter


class OrGate(Gatter):
    def __init__(self, inputs, nor=False):
        super().__init__(inputs, nor)
        self.type = "OR"

    def calc(self):
        for inputstate in self.entrances:
            if inputstate:
                return True
        return False

    def set_output_value(self):
        self.set_output(self.calc())
