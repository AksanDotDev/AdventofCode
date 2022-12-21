import sys

with open(sys.argv[1]) as file:
    raw = file.readlines()


class Exp():
    system = dict()

    def __init__(self, raw_line) -> None:
        tokens = raw_line.split()
        if len(tokens) == 2:
            self.value = int(tokens[1])
        else:
            self.value = None
            self.arg_1 = tokens[1]
            self.arg_2 = tokens[3]
            self.op = tokens[2]
        Exp.system[tokens[0].strip(":")] = self

    def get_value(self):
        if self.value is None:
            arg_1 = Exp.system[self.arg_1].get_value()
            arg_2 = Exp.system[self.arg_2].get_value()
            if self.op == "+":
                value = arg_1 + arg_2
            elif self.op == "*":
                value = arg_1 * arg_2
            elif self.op == "-":
                value = arg_1 - arg_2
            elif self.op == "/":
                value = arg_1 / arg_2
            else:
                raise Exception("Panic!")
            self.value = value
            return value
        else:
            return self.value


for raw_line in raw:
    Exp(raw_line)

print(int(Exp.system["root"].get_value()))
