import util


def race_times(totalTime: int):
    times = []
    for i in range(totalTime+1):
        to_add = i * (totalTime-i)
        times.append(to_add)
    return times
    
def bigger_in(times: list[int], target: int):
    return len([time for time in times if time > target])

def get_races(filename):
    lines = list(util.linewise(filename, True))
    times = [int(time) for time in lines[0].split(" ") if time.isdecimal()]
    dists = [int(dist) for dist in lines[1].split(" ") if dist.isdecimal()]

    for time, dist in zip(times, dists):
        yield time, dist

def get_bigrace(filename):
    lines = list(util.linewise(filename, True))
    time = int(lines[0].split(":")[1].replace(" ", ""))
    dist= int(lines[1].split(":")[1].replace(" ", ""))
    return time, dist

def run1():
    mul = 1
    for time, dist in get_races("races.txt"):
        mul *= bigger_in(race_times(time), dist)
    print(mul)

def run2():
    time, dist = get_bigrace("races.txt")
    print(bigger_in(race_times(time), dist))