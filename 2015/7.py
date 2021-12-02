import re

BITSIZE = 2**16


class Signal:
    value = None


class Wire:
    id = None
    signal = None
    dynamic = None

    def __init__(self, **kwargs):
        self.signal = Signal()
        self.dynamic = True
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        return f'{self.id}({self.signal.value})'

    def reset(self):
        if self.dynamic:
            self.signal.value = None


class Gate:
    input = []  # can be multiple wires
    output = None  # a signle wire

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def propagate_signal(self):
        raise NotImplementedError()

    def ready(self) -> bool:
        return all([w.signal.value is not None for w in self.input if isinstance(w, Wire)])


class AndGate(Gate):
    def propagate_signal(self):
        left, right = self.input
        signal = (left.signal.value & right.signal.value) % BITSIZE
        self.output.signal.value = signal
        return all([w.signal.value is not None for w in self.input])

    def __repr__(self):
        return f'{self.input[0].id}({self.input[0].signal.value}) AND {self.input[1].id}({self.input[1].signal.value}) -> {self.output.id}({self.output.signal.value})'


class OrGate(Gate):
    def propagate_signal(self):
        left, right = self.input
        signal = (left.signal.value | right.signal.value) % BITSIZE
        self.output.signal.value = signal

    def __repr__(self):
        return f'{self.input[0].id}({self.input[0].signal.value}) OR {self.input[1].id}({self.input[1].signal.value}) -> {self.output.id}({self.output.signal.value})'


class RightShiftGate(Gate):
    def propagate_signal(self):
        left, n = self.input
        signal = (left.signal.value >> n) % BITSIZE
        self.output.signal.value = signal

    def __repr__(self):
        return f'{self.input[0].id}({self.input[0].signal.value}) RSHIFT {self.input[1]} -> {self.output.id}({self.output.signal.value})'


class LeftShiftGate(Gate):
    def propagate_signal(self):
        left, n = self.input
        signal = (left.signal.value << n) % BITSIZE
        self.output.signal.value = signal

    def __repr__(self):
        return f'{self.input[0].id}({self.input[0].signal.value}) LSHIFT {self.input[1]} -> {self.output.id}({self.output.signal.value})'


class NotGate(Gate):
    def propagate_signal(self):
        wire = self.input[0]
        signal = (~ wire.signal.value) % BITSIZE
        self.output.signal.value = signal

    def __repr__(self):
        return f'NOT {self.input[0].id}({self.input[0].signal.value}) -> {self.output.id}({self.output.signal.value})'


def setup(instructions):
    wires = dict()
    gates = set()

    for instruction in instructions:
        # x AND/OR y -> z
        if (m := re.search(r'^(\w+) (AND|OR) (\w+) -> (\w+)$', instruction)):
            left, op, right, out = m.groups()
            if left not in wires:
                wires[left] = Wire(id=left)
                try:
                    wires[left].signal.value = int(left)
                    wires[left].dynamic = False  # make sure this wire is not cleared on reset
                except ValueError:
                    pass
            if right not in wires:
                wires[right] = Wire(id=right)
                try:
                    wires[right].signal.value = int(right)
                    wires[right].dynamic = False  # make sure this wire is not cleared on reset
                except ValueError:
                    pass
            if out not in wires:
                wires[out] = Wire(id=out)

            if op == 'AND':
                gate = AndGate(input=[wires[left], wires[right]], output=wires[out])
            else:
                gate = OrGate(input=[wires[left], wires[right]], output=wires[out])
            gates.add(gate)

        # x LSHIFT/RSHIFT n -> z
        elif (m := re.search(r'^(\w+) (LSHIFT|RSHIFT) (\d+) -> (\w+)$', instruction)):
            left, op, n, out = m.groups()
            if left not in wires:
                wires[left] = Wire(id=left)
                try:
                    wires[left].signal.value = int(left)
                    wires[left].dynamic = False  # make sure this wire is not cleared on reset
                except ValueError:
                    pass
            if out not in wires:
                wires[out] = Wire(id=out)

            if op == 'LSHIFT':
                gate = LeftShiftGate(input=[wires[left], int(n)], output=wires[out])
            else:
                gate = RightShiftGate(input=[wires[left], int(n)], output=wires[out])
            gates.add(gate)

        # NOT x -> y
        elif (m := re.search(r'^NOT (\w+) -> (\w+)$', instruction)):
            wire, out = m.groups()
            if wire not in wires:
                wires[wire] = Wire(id=wire)
                try:
                    wires[wire].signal.value = int(wire)
                    wires[wire].dynamic = False  # make sure this wire is not cleared on reset
                except ValueError:
                    pass
            if out not in wires:
                wires[out] = Wire(id=out)

            gate = NotGate(input=[wires[wire]], output=wires[out])
            gates.add(gate)

        # x -> y
        elif (m := re.search(r'^(\w+) -> (\w+)$', instruction)):
            left, right = m.groups()
            if left not in wires:
                wires[left] = Wire(id=left)
                try:
                    wires[left].signal.value = int(left)
                    wires[left].dynamic = False  # make sure this wire is not cleared on reset
                    wires[right].dynamic = False  # may throw KeyError, but then it will be set in the next if clause
                except (ValueError, KeyError):
                    pass
            if right not in wires:
                wires[right] = Wire(id=right)
                wires[right].dynamic = wires[left].dynamic

            # make sure that right has the same signal as left
            wires[right].signal = wires[left].signal

    return wires, gates


def propagate_signals(gates):
    remaining = list(gates)
    while len(remaining):
        for gate in remaining:
            if gate.ready():
                gate.propagate_signal()
                remaining.remove(gate)


with open('files/7.txt', 'r') as f:
    instructions = f.readlines()

# instructions = [
#     '123 -> x\n',
#     '456 -> y\n',
#     'x AND y -> d\n',
#     'x OR y -> e\n',
#     'x LSHIFT 2 -> f\n',
#     'y RSHIFT 2 -> g\n',
#     'NOT x -> h\n',
#     'NOT y -> i\n',
# ]

# Exercise 1
wires, gates = setup(instructions)
propagate_signals(gates)
print(wires['a'])

# Exercise 2
value_a = wires['a'].signal.value

for id, wire in wires.items():
    wire.reset()

wires['b'].signal.value = value_a
propagate_signals(gates)
print(wires['a'])
