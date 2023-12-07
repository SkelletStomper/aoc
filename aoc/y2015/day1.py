from util import linewise


def evaluate_line(line: str) -> int:
    sum = 0
    for char in line:
        if char == "(":
            sum += 1
        if char == ")":
            sum -= 1
    return sum

def basementer(str)-> int:
    sum = 0
    for i, char in enumerate(str):
        if char == "(":
            sum += 1
        if char == ")":
            sum -= 1
        if sum == -1:
            return i+1

def run1():
    sum = 0
    for line in linewise("santaFloor.txt"):
        sum += evaluate_line(line)
    print(sum)

def run2():
    text = "".join([line for line in linewise("santaFloor.txt")])
    print(basementer(text))