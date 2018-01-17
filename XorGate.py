from Gatter import *


class XorGate(Gatter):
    def __init__(self, inputs, nor=False):
        super().__init__(inputs, nor)
        self.type = "XOR"

    def calc(self):
        check = 0
        for inputstate in self.entrances:
            if inputstate:
                check += 1
        return check == 1

    def set_output_value(self):
        self.set_output(self.calc())
