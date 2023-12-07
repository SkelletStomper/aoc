import util


def dimensions(dimString: str) -> tuple[int, int, int]:
    return tuple([int(num) for num in dimString.split("x")])


def rectaPrism_area(l: int, w: int, h: int) -> int:
    sides = [w*l, w*h, l*h]
    return sides[0]*2 + sides[1]*2 + sides[2]*2 + min(sides)

def ribbons(l: int, w: int, h: int) -> int:
    configs = [2*(l+w), 2*(l+h), 2*(h+w)]
    return min(configs) + w*l*h



def run1():
    s = 0
    for line in util.linewise("elfWrapper.txt"):
        s += rectaPrism_area(*dimensions(line))
    print(s)

def run2():
    s = 0
    for line in util.linewise("elfWrapper.txt"):
        s += ribbons(*dimensions(line))
    print(s)