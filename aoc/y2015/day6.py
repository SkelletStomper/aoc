import util




class LightField:
    def __init__(self, sizes = (1000, 1000)):
        self.sizes = sizes
        self.field = [0 for _ in range(sizes[0]*sizes[1])]

    def _get_indices(self, start:tuple[int, int], end:tuple[int, int]):
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                yield self.index2Dto1D((x,y))
    
    def index2Dto1D(self, index2D: tuple[int, int]):
        return self.sizes[0]*index2D[1] + index2D[0]
    
    def turn_on(self, start:tuple[int, int], end:tuple[int, int]):
        for index in self._get_indices(start, end):
            self.field[index] = 1


    def turn_off(self, start:tuple[int, int], end:tuple[int, int]):
        for index in self._get_indices(start, end):
            self.field[index] = 0
    
    def toggle(self, start:tuple[int, int], end:tuple[int, int]):
        for index in self._get_indices(start, end):
            self.field[index] = 1 - self.field[index]
    

    def count_lights(self):
        return self.field.count(1)

    def process(self, command: str):
        typRaw, startRaw, endRaw = command.split("|")
        typ = int(typRaw)
        start = tuple([int(num) for num in startRaw.split(",")])
        end = tuple([int(num) for num in endRaw.split(",")])
        if typ == 0:
            self.turn_off(start, end)
        if typ == 1:
            self.turn_on(start, end)
        if typ == 2:
            self.toggle(start, end)


class LightFieldGradient(LightField):
    def turn_on(self, start:tuple[int, int], end:tuple[int, int]):
        for index in self._get_indices(start, end):
            self.field[index] += 1

    def turn_off(self, start:tuple[int, int], end:tuple[int, int]):
        for index in self._get_indices(start, end):
            self.field[index] = max(0, self.field[index] -1)
            
    def toggle(self, start:tuple[int, int], end:tuple[int, int]):
        for index in self._get_indices(start, end):
            self.field[index] += 2

    def count_lights(self):
        return sum(self.field)

def saniText(line: str) -> str:
    dic = {
        "turn off ": "0|",
        "turn on ": "1|",
        "toggle ": "2|",
        " through ": "|"
    }
    return util.replace_dict(line, dic)



def run1():
    lf = LightField((1000,1000))
    for line in util.linewise("lightshow.txt", True):
        line = saniText(line)
        lf.process(line)
    print(lf.count_lights())

def run2():
    lf = LightFieldGradient((1000,1000))
    for line in util.linewise("lightshow.txt", True):
        line = saniText(line)
        lf.process(line)
    print(lf.count_lights())




