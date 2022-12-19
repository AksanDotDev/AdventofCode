import sys
from operator import attrgetter


with open(sys.argv[1]) as file:
    raw = map(lambda x: x.split(), file.readlines())


class Resources():

    def __init__(
        self,
        ore: int,
        clay: int,
        obsidian: int,
        geode: int,
    ):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __add__(self, other):
        if not isinstance(other, Resources):
            NotImplemented
        else:
            return Resources(
                self.ore + other.ore,
                self.clay + other.clay,
                self.obsidian + other.obsidian,
                self.geode + other.geode
            )

    def __iadd__(self, other):
        if not isinstance(other, Resources):
            NotImplemented
        else:
            self.ore += other.ore
            self.clay += other.clay
            self.obsidian += other.obsidian
            self.geode += other.geode
            return self

    def __sub__(self, other):
        if not isinstance(other, Resources):
            NotImplemented
        else:
            return Resources(
                self.ore - other.ore,
                self.clay - other.clay,
                self.obsidian - other.obsidian,
                self.geode - other.geode
            )

    def __isub__(self, other):
        if not isinstance(other, Resources):
            NotImplemented
        else:
            self.ore -= other.ore
            self.clay -= other.clay
            self.obsidian -= other.obsidian
            self.geode -= other.geode
            return self

    def __le__(self, other):
        if not isinstance(other, Resources):
            NotImplemented
        else:
            return (
                self.ore <= other.ore and
                self.clay <= other.clay and
                self.obsidian <= other.obsidian and
                self.geode <= other.geode
            )

    def __ge__(self, other):
        if not isinstance(other, Resources):
            NotImplemented
        else:
            return (
                self.ore >= other.ore and
                self.clay >= other.clay and
                self.obsidian >= other.obsidian and
                self.geode >= other.geode
            )

    def copy(self):
        return Resources(
            self.ore,
            self.clay,
            self.obsidian,
            self.geode
        )

    def __repr__(self):
        return f"Resources(Ore:{self.ore}, Clay:{self.clay}," +\
            f" Obsidian:{self.obsidian}, Geode:{self.geode})"


class BluePrint():

    def __init__(
        self,
        ore_bot: Resources,
        clay_bot: Resources,
        obsidian_bot: Resources,
        geode_bot: Resources,
    ):
        self.ore_bot = ore_bot
        self.clay_bot = clay_bot
        self.obsidian_bot = obsidian_bot
        self.geode_bot = geode_bot
        blueprints = [
            self.ore_bot,
            self.clay_bot,
            self.obsidian_bot,
            self.geode_bot
        ]
        self._max_ore = max(map(attrgetter("ore"), blueprints))
        self._max_clay = max(map(attrgetter("clay"), blueprints))
        self._max_obsidian = max(map(attrgetter("obsidian"), blueprints))

    def could_make_ore_bot(self, state):
        return (
            (state.bots.ore < self._max_ore) and
            (self.ore_bot.ore == 0 or state.bots.ore > 0) and
            (self.ore_bot.clay == 0 or state.bots.clay > 0) and
            (self.ore_bot.obsidian == 0 or state.bots.obsidian > 0) and
            (self.ore_bot.geode == 0 or state.bots.geode > 0)
        )

    def could_make_clay_bot(self, state):
        return (
            (state.bots.clay < self._max_clay) and
            (self.clay_bot.ore == 0 or state.bots.ore > 0) and
            (self.clay_bot.clay == 0 or state.bots.clay > 0) and
            (self.clay_bot.obsidian == 0 or state.bots.obsidian > 0) and
            (self.clay_bot.geode == 0 or state.bots.geode > 0)
        )

    def could_make_obsidian_bot(self, state):
        return (
            (state.bots.obsidian < self._max_obsidian) and
            (self.obsidian_bot.ore == 0 or state.bots.ore > 0) and
            (self.obsidian_bot.clay == 0 or state.bots.clay > 0) and
            (self.obsidian_bot.obsidian == 0 or state.bots.obsidian > 0) and
            (self.obsidian_bot.geode == 0 or state.bots.geode > 0)
        )

    def could_make_geode_bot(self, state):
        return (
            (self.geode_bot.ore == 0 or state.bots.ore > 0) and
            (self.geode_bot.clay == 0 or state.bots.clay > 0) and
            (self.geode_bot.obsidian == 0 or state.bots.obsidian > 0) and
            (self.geode_bot.geode == 0 or state.bots.geode > 0)
        )

    def make_ore_bot(self, state):
        while (not state.resources >= self.ore_bot)\
                and state.time > 0:
            state.step()
        if state.time == 0:
            return state
        state.resources -= self.ore_bot
        state.step()
        state.bots.ore += 1
        return state

    def make_clay_bot(self, state):
        while not state.resources >= self.clay_bot\
                and state.time > 0:
            state.step()
        if state.time == 0:
            return state
        state.resources -= self.clay_bot
        state.step()
        state.bots.clay += 1
        return state

    def make_obsidian_bot(self, state):
        while not state.resources >= self.obsidian_bot\
                and state.time > 0:
            state.step()
        if state.time == 0:
            return state
        state.resources -= self.obsidian_bot
        state.step()
        state.bots.obsidian += 1
        return state

    def make_geode_bot(self, state):
        while not state.resources >= self.geode_bot\
                and state.time > 0:
            state.step()
        if state.time == 0:
            return state
        state.resources -= self.geode_bot
        state.step()
        state.bots.geode += 1
        return state

    def get_options(self, state):
        options = []
        if self.could_make_geode_bot(state):
            options.append(self.make_geode_bot)
        if self.could_make_obsidian_bot(state):
            options.append(self.make_obsidian_bot)
        if self.could_make_clay_bot(state):
            options.append(self.make_clay_bot)
        if self.could_make_ore_bot(state):
            options.append(self.make_ore_bot)
        return options

    def __repr__(self):
        return f"BluePrint(OreBot:{self.ore_bot}, ClayBot:{self.clay_bot}," +\
            f" ObsidianBot:{self.obsidian_bot}, GeodeBot:{self.geode_bot})"


class State():

    def __init__(
        self,
        time: int,
        resources: Resources,
        bots: Resources
    ):
        self.time = time
        self.resources = resources
        self.bots = bots

    def step(self):
        self.time -= 1
        self.resources += self.bots
        return self

    def copy(self):
        return State(
            self.time,
            self.resources.copy(),
            self.bots.copy()
        )

    def __repr__(self) -> str:
        return f"State(Time:{self.time}," +\
            f" Resources:{self.resources}, Bots:{self.bots})"

    def best_potential(self):
        potential = self.resources.geode
        potential += self.bots.geode * self.time
        potential += (self.time*(self.time - 1))//2
        return potential


default_state = State(
    32,
    Resources(0, 0, 0, 0),
    Resources(1, 0, 0, 0)
)


def recursive_solve(blueprint: BluePrint, state: State):
    global current_best
    if state.time == 0:
        current_best = max(state.resources.geode, current_best)
    elif current_best > state.best_potential():
        pass
    else:
        for option in blueprint.get_options(state):
            recursive_solve(
                blueprint,
                option(state.copy())
            )


answer = 1
for line in list(raw)[:3]:
    bp = BluePrint(
        Resources(int(line[6]), 0, 0, 0),
        Resources(int(line[12]), 0, 0, 0),
        Resources(int(line[18]), int(line[21]), 0, 0),
        Resources(int(line[27]), 0, int(line[30]), 0),
    )
    current_best = 0
    recursive_solve(bp, default_state.copy())
    answer *= current_best

print(answer)
