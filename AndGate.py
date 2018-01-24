from Gatter import *

class AndGate(Gatter):
    def __init__(self, inputs, nor=False):
        super().__init__(inputs, nor)
        if not nor:
            self.type = "AND"
        elif nor:
            self.type = "NAND"

    def calc(self):
        for inputstate in self.entrances:
            if not inputstate:
                return False
        return True

    def set_output_value(self):
        self.set_output(self.calc())

    def print(self):
        print(self.entrances)