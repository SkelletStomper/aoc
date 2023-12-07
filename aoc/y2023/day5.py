import util



class Mapping:
    class Map:
        def __init__(self, srcStart: int, dstStart: int, covering: int):
            self.srcStart = srcStart
            self.dstStart = dstStart
            self.covering = covering

        def __contains__(self, number: int) -> bool:
            return number >= self.srcStart and number < self.srcStart + self.covering

        def map(self, number: int) -> int:
            if number not in self:
                raise(Exception("Why?"))
            delta = self.dstStart - self.srcStart
            return number + delta

        def __str__(self):
            return f"Map starting from {self.srcStart}, mapping to {self.dstStart} and mapping {self.covering} values (delta: {self.dstStart-self.srcStart})"

        def reverse(self):
            tmp = self.srcStart
            self.srcStart = self.dstStart
            self.dstStart = tmp


    def __init__(self, src: str, dst: str):
        self.src = src
        self.dst = dst
        self.maps: list[Mapping.Map] = list()
    def add_map(self, srcStart, dstStart, covering):
        self.maps.append(self.Map(srcStart, dstStart, covering))
    
    def map(self, number: int) -> tuple[str, int]:
        retNum = number
        #print(self)
        for map in self.maps:
            if number in map:
                retNum = map.map(number)
                #print(f"mapped {number} to {retNum} via {map}")
                break
        else:
            #print(f"Kept {number} the same")
            pass
        
        return (self.dst, retNum)

    def reverse(self):
        tmp = self.src
        self.src = self.dst
        self.dst = tmp

        for map in self.maps:
            map.reverse()
        return self

    def __str__(self):
        return f"Mapping from {self.src} to {self.dst}"

    

class Almanach():
    def __init__(self, filename):
        lines = list(util.linewise(filename, True))
        lines.append("")
        
        self.get_seeds_from_line(lines[0])

        self.mappings: dict[str, Mapping] = dict()
        mappingStart = False
        buildingMapping: Mapping|None = None
        for i, line in enumerate(lines[1:]):
            if line == "":
                if buildingMapping is not None:
                    self.mappings[buildingMapping.src] = buildingMapping
                    buildingMapping = None
                mappingStart = True
            elif mappingStart:
                tmp = line.split(" ")[0].split("-to-")
                src, dst = tmp[0], tmp[1]
                buildingMapping = Mapping(src, dst)
                mappingStart = False
            else:
                dstStart, srcStart, covering = [int(num) for num in line.split(" ")]
                buildingMapping.add_map(srcStart, dstStart, covering)
    
    def get_seeds_from_line(self, line):
        sanitized = line[7:]
        self._seeds = list([int(seed) for seed in sanitized.split(" ")])


    @property
    def seeds(self):
        for seed in self._seeds:
            yield "seed", seed
    def in_seeds(self, num):
        return num in self._seeds

    def process(self, start: tuple[str, int], target: str) -> int:
        typ, num = start
        while typ != target:
            typ, num = self.mappings[typ].map(num)
        return num

    def processed(self):
        for seed in self.seeds:
            yield self.process(seed, "location")
    
    def search_for_lowest(self) -> int:
        minLocation= util.inf()
        for location in self.processed():
            minLocation = min(minLocation, location)
        return minLocation

    def reverse(self):
        revMaps = [mapping.reverse() for mapping in self.mappings.values()]
        self.mappings = {mapping.src: mapping for mapping in revMaps}
    def search_for_lowest_reverse(self) -> int:
        c = 51000000
        self.reverse()
        while True:
            if c%50000 == 0:
                print(c)
            if self.in_seeds(self.process(("location", c), "seed")):
                self.reverse()
                return c
            c += 1

class AlmaMass(Almanach):
    def get_seeds_from_line(self, line):
        from itertools import pairwise
        sanitized = line[7:]
        seeds = [int(num) for num in sanitized.split(" ")]
        self.seed_ranges = [pair for i, pair in enumerate(pairwise(seeds)) if i%2 == 0]
        print(self.seed_ranges)
    @property
    def seeds(self):
        for pair in self.seed_ranges:
            start, much = pair
            print(f"range with {much} locations")
            for i in range(start, start+much):
                if i%50000 == 0:
                    print((i-start) /much)
                yield ("seed", i)
    def in_seeds(self, num):
        for pair in self.seed_ranges:
            start, much = pair
            if start <= num < start+much:
                return True
        return False
    


def run1():
    a = Almanach("almanach.txt")
    print(a.search_for_lowest())
    

def run2():
    a = AlmaMass("almanach.txt")
    print(a.search_for_lowest_reverse())
   