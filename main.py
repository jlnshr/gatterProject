from AndGate import *
from OrGate import *
from XorGate import *

or_gate = OrGate(2)
or_gate.report()
or_gate.set_inputstate(0, True)
or_gate.set_output_value()
or_gate.report()

and_gate = AndGate(3, True)
and_gate.report()
for i in range(0, 3):
    and_gate.set_inputstate(i, True)
and_gate.set_output_value()
and_gate.report()
xor_gate = XorGate(4)
xor_gate.report()
xor_gate.set_inputstate(0, True)
xor_gate.set_inputstate(3, True)
xor_gate.set_output_value()
xor_gate.report()
