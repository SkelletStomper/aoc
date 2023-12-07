import util



def vowels(text: str)-> int:
    return len([char for char in text if char in "aeiou"])

def badCombs(text: str) -> bool:
    for comb in ["ab", "cd", "pq", "xy"]:
        if comb in text:
            return True
    return False

def goodCombs(text: str, space = 1) -> bool:
    for a, b in util.one_and_next(text, space):
        if a == b:
            return True
    return False

def pairs_no_overlap(text: str) -> bool:
    dic = dict()
    count = 0
    for a, b in util.one_and_next(text):
        c = a+b
        if not c in dic:
            dic[c] = set()
        dic[c].update({count, count+1})
        count+= 1
    
    return any([len(x) >= 4 for x in dic.values()])
        
        

def nice_or_naughty(text: str) -> bool:
    return vowels(text) >= 3 and goodCombs(text) and not badCombs(text)

def nice_or_naughty2(text: str) -> bool:
    return goodCombs(text, 2) and pairs_no_overlap(text)




def run1():
    s = 0
    for line in util.linewise("niceNaughty.txt"):
        if nice_or_naughty(line):
            s += 1
    print(s)

def run2():
    s = 0
    for line in util.linewise("niceNaughty.txt"):
        if nice_or_naughty2(line):
            s += 1
    print(s)