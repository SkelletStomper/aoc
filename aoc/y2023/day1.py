import util



def replaceWritten(text: str) -> str:
    dic = {
        "one": "o1ne",
        "two": "t2wo",
        "three": "t3hree",
        "four": "f4our",
        "five": "f5ive",
        "six": "s6ix",
        "seven": "s7even",
        "eight": "e8ight",
        "nine": "n9ine",
    }
    return util.replace_dict(text, dic)




def firstLast(text: str) -> int:
    first = None;
    last = None;
    for char in text:
        if char.isdigit():
            num = int(char)
            if first is None:
                first = num
            last = num
    return first*10 + last

def trebuchet_calculations(filename: str, replace = False) -> int:
    s = 0
    for line in util.linewise(filename):
        if replace:
            line = replaceWritten(line)
        calc = firstLast(line)
        s += calc
    return s



def run1():
    print("Sum:", trebuchet_calculations("trebuchet.txt", False))
def run2():
    print("Sum:", trebuchet_calculations("trebuchet.txt", True))
