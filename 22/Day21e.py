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
            if tokens[0].strip(":") == "root":
                self.op = "=="
            else:
                self.op = tokens[2]
        Exp.system[tokens[0].strip(":")] = self

    def get_value(self):
        if self.value is None:
            arg_1 = Exp.system[self.arg_1].get_value()
            arg_2 = Exp.system[self.arg_2].get_value()
            if self.op == "==":
                value = abs(arg_1 - arg_2)
            elif self.op == "+":
                value = arg_1 + arg_2
            elif self.op == "*":
                value = arg_1 * arg_2
            elif self.op == "-":
                value = arg_1 - arg_2
            elif self.op == "/":
                value = arg_1 / arg_2
            else:
                raise Exception("Panic!")
            return value
        else:
            return self.value


for raw_line in raw:
    Exp(raw_line)


searching = True

lr = 0.1

while searching:
    baseline_diff = Exp.system["root"].get_value()
    if baseline_diff == 0.0:
        searching = False
        break
    baseline = Exp.system["humn"].get_value()
    Exp.system["humn"].value = baseline + 1
    pos_test_diff = Exp.system["root"].get_value()
    if pos_test_diff < baseline_diff:
        Exp.system["humn"].value = int(baseline + max(1, lr*baseline_diff))
    else:
        Exp.system["humn"].value = int(baseline - max(1, lr*baseline_diff))
    lr *= 0.95

print(Exp.system["humn"].get_value())
