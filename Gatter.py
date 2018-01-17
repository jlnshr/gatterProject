class Gatter:
    def __init__(self, inputs, nor=False):
        self.inputs = inputs
        self.output = False
        self.type = ""
        self.entrances = []
        self.nor = nor

        for i in range(0, self.inputs):
            self.entrances.append(False)

    def report(self):
        print("Das Gatter hat {0} Eingänge und ist vom Typ {1}. Der Ausgangswert ist aktuell {2}"
              .format(self.inputs, self.type, self.output))

    def get_entrances(self):
        return self.entrances

    def get_output(self):
        return self.output

    def set_output(self, value):
        if self.nor:
            self.output = not value
        elif not self.nor:
            self.output = value

    def set_inputstate(self, index, value):
        self.entrances[index] = value

    def get_inputstate(self, index):
        return self.entrances[index]
