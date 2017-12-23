"""--- Day 23: Coprocessor Conflagration ---"""
from collections import defaultdict


class ExperimentalCoprocessor:
    """A tablet represenatation able to run the assembly code Duet."""

    def __init__(self, puzzle_input):
        """ctor, nothing more exiting."""
        self.instructions = puzzle_input
        self.registers = defaultdict(int)
        self.pc = 0
        self.mul_counter = 0

    def step(self):
        """
        Execute the next instruction and move the pc counter to the next instruction.

        Throws:
            Exception: If the instruction is unknown and cannot be handled or if
                        self.pc points to an invalid index of self.instructions.

        """
        if self.pc < 0 or self.pc >= len(self.instructions):
            raise Exception('Index out of bounds for pc.')
        ins, x, *optionals = self.instructions[self.pc].split()
        y = optionals[0] if len(optionals) > 0 else None
        if ins == 'set':
            self.registers[x] = self._get_value(y)
        elif ins == 'sub':
            self.registers[x] -= self._get_value(y)
        elif ins == 'mul':
            self.registers[x] *= self._get_value(y)
            self.mul_counter += 1
        elif ins == 'jnz':
            if self._get_value(x) != 0:
                # -1 since we always add 1 to self.pc later in the method.
                self.pc += self._get_value(y) - 1
        else:
            raise Exception('Unable to parse instruction: ' + self.instructions[self.pc])
        self.pc += 1

    def _get_value(self, value):
        """Convert the value into an int or return value of self.registers[value]."""
        try:
            return int(value)
        except ValueError:
            return self.registers[value]


def part_a(puzzle_input):
    """
    Calculate the answer for part_a.

    Args:
        puzzle_input (list): Formatted as the provided input from the website.
    Returns:
        string: The answer for part_a.

    """
    ec = ExperimentalCoprocessor(puzzle_input)
    try:
        while True:
            ec.step()
    except Exception:
        pass
    return str(ec.mul_counter)


def part_b(puzzle_input):
    """
    Calculate the answer for part_b.

    Solving this part for the general case takes "forever", so instead of
    running the code in the ExperimentalCoprocessor, we translate the code
    into Python code instead.

    Original input to the left. A jnz with a negative value indicates a loop and
    a jnz with a positive value will be translated into an if-statement.
    set b 81                        set b 81
    set c b                         set c b
    jnz a 2                         jnz a 2
    jnz 1 5                         jnz 1 5
    mul b 100                       mul b 100
    sub b -100000                   sub b -100000
    set c b                         set c b
    sub c -17000                    sub c -17000
    set f 1                             set f 1
    set d 2                             set d 2
    set e 2                                 set e 2
    set g d                                     set g d
    mul g e                                     mul g e
    sub g b                                     sub g b
    jnz g 2                                     jnz g 2
    set f 0                                     set f 0
    sub e -1                                    sub e -1
    set g e                                     set g e
    sub g b                                     sub g b
    jnz g -8                                    jnz g -8  # repeat if g != 0
    sub d -1                                sub d -1
    set g d                                 set g d
    sub g b                                 sub g b
    jnz g -13                               jnz g -13  # repeat if g != 0
    jnz f 2                             jnz f 2
    sub h -1                            sub h -1
    set g b                             set g b
    sub g c                             sub g c
    jnz g 2                             jnz g 2
    jnz 1 3                             jnz 1 3  # if g == 0 above, jump out of the instructions and finish!
    sub b -17                           sub b -17
    jnz 1 -23                           jnz 1 -23

    A rough translation to Python code would then be...
    set b 81                            b = 81
    set c b                             c = b
    jnz a 2                             if a != 0:
    jnz 1 5
    mul b 100                               b *= 100
    sub b -100000                           b -= -100000
    set c b                                 c = b
    sub c -17000                            c -= -17000
                                            while True:
        set f 1                                 f = 1
        set d 2                                 d = 2
                                                while True:
            set e 2                                 e = 2
                                                    while True:
                set g d                                 g = d
                mul g e                                 g *= e
                sub g b                                 g -= b
                jnz g 2                                 if g == 0:
                set f 0                                     f = 0
                sub e -1                                e -= -1
                set g e                                 g = e
                sub g b                                 g -= b
                jnz g -8                                if g == 0:
                                                            break
            sub d -1                                d -= -1
            set g d                                 g = d
            sub g b                                 g -= b
            jnz g -13                               if g == 0:
                                                        break
        jnz f 2                                 if f == 0:
        sub h -1                                    h -= -1
        set g b                                 g = b
        sub g c                                 g -= c
        jnz g 2                                 if g == 0:
        jnz 1 3                                     break
        sub b -17                               b -= -17
        jnz 1 -23                               # repeat again!

    And then we compress the Python code a bit. Part b states that a should start
    with value 1, therefore we can remove the first if-statement.
    a, b, c, d, e, f, g, h = 0, 0, 0, 0, 0, 0, 0, 0
    a = 1
    b = 81 * 100 + 100000
    c = b + 17000
    while True:
        f = 1
        d = 2
        while True:
            e = 2               # We recogonize this pattern, set a vaiable to a
            while True:         # constant, then increase it by 1 later on and
                g = d * e - b   # then check if it has reached a value and break
                if g == 0:      # if that is true => for i in range(a, b)
                    f = 0
                e += 1
                g = e - b
                if g == 0:
                    break
            d += 1
            g = d - b
            if g == 0:
                break
        if f == 0:
            h += 1
        g = b - c
        if g == 0:
            break
        b += 17

    A more compact version is listed below. The code still runs really slow...
    h = 0
    for b in range(108100, 125100 + 1, 17):
        f = 1
        for d in range(2, b + 1):
            for e in range(2, b + 1):
                if d * e == b:
                    f = 0
        if f == 0:
            h += 1

    The two inner loops check if b is a composite number in an inefficient way.
    It will continue to check multiplications even if d * e == b. It does also
    check if e * d == b even if multiplication has the associative property,
    https://en.wikipedia.org/wiki/Associative_property

    Moving the two inner loops to a method with faster return will speed up
    the code a bit :)

    Args:
        puzzle_input (list): Actually not used...
    Returns:
        string: The answer for part_b.

    """
    def is_composite(number):
        if number % 2 == 0:
            return True
        for i in range(3, int(number ** 0.5) - 1, 2):  # to need to check even numbers
            if number % i == 0:
                return True
        return False
    h = 0
    for b in range(108100, 125100 + 1, 17):
        if is_composite(b):
            h += 1
    return str(h)


def solve(puzzle_input):
    """Returs the answer for both parts."""
    return {'a': part_a(puzzle_input), 'b': part_b(puzzle_input)}
