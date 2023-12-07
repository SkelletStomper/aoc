import util




def houseChecker(directions: str, santas = 1):
    loc = [[0,0] for _ in range(santas)]
    visited = {(0,0): 1}
    santa = 0
    for char in directions:
        if char == "^":
            loc[santa][1] += 1
        elif char == "v":
            loc[santa][1] -= 1
        elif char == "<":
            loc[santa][0] -= 1
        elif char == ">":
            loc[santa][0] += 1
        tloc = tuple(loc[santa])
        if not tloc in visited:
            visited[tloc] = 0
        visited[tloc] += 1
        santa += 1
        santa %= santas
    return visited


def run1():
    visited = houseChecker(util.file_string("eggnogDriver.txt"))
    print(len(visited))

def run2():
    visited = houseChecker(util.file_string("eggnogDriver.txt"), 2)
    print(len(visited))


