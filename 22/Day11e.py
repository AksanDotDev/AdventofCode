import sys
from collections import deque
from math import lcm

with open(sys.argv[1]) as file:
    raw = file.readlines()


class Monkey():
    monkeys = []
    mod = None

    def __init__(
                self,
                starting_items,
                operation,
                test,
                outcomes
            ):
        self.items = deque(starting_items)
        self.operation = operation
        self.test = test
        self.outcomes = outcomes
        self.inspections = 0
        Monkey.monkeys.append(self)
        if mod := Monkey.mod:
            Monkey.mod = lcm(mod, self.test.value)
        else:
            Monkey.mod = self.test.value

    @classmethod
    def round(cls):
        for monkey in cls.monkeys:
            monkey.turn()

    def turn(self):
        while self.items:
            item = self.items.popleft()
            item = self.operation(item)
            self.inspections += 1
            target = self.outcomes[self.test(item)]
            item %= Monkey.mod
            Monkey.monkeys[target].throw(item)

    def throw(self, item):
        self.items.append(item)

    def __repr__(self):
        return f"Monkey: Holding{self.items}, Operation: {self.operation}, " +\
               f"Test: {self.test}, Outcomes: {self.outcomes}, " +\
               f"Inspections: {self.inspections}"


class Operation():

    def __init__(self, op, arg):
        if arg == "old":
            if op == "*":
                self._func = lambda x: x**2
                self._str = "x**2"
            else:
                self._func = lambda x: x * 2
                self._str = "x * 2"
        else:
            if op == "*":
                self._func = lambda x: x * int(arg)
                self._str = f"x * {int(arg)}"
            else:
                self._func = lambda x: x + int(arg)
                self._str = f"x + {int(arg)}"

    def __call__(self, x):
        return self._func(x)

    def __repr__(self) -> str:
        return self._str


class Test():

    def __init__(self, div):
        self.value = int(div)
        self._func = lambda x: (x % self.value) == 0
        self._str = f"x % {self.value} == 0"

    def __call__(self, x):
        return self._func(x)

    def __repr__(self) -> str:
        return self._str


for i in range(0, len(raw), 7):
    Monkey(
        starting_items=map(lambda x: int(x.strip(",")), raw[i+1].split()[2:]),
        operation=Operation(*raw[i+2].split()[4:]),
        test=Test(raw[i+3].split()[3]),
        outcomes=(int(raw[i+5].split()[5]), int(raw[i+4].split()[5])),
    )

for _ in range(10000):
    Monkey.round()

inspections = sorted(
    map(lambda x: x.inspections, Monkey.monkeys),
    reverse=True
)

print(inspections[0]*inspections[1])
