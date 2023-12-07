import util
from collections import Counter




class Hand:
    labels = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    labelDic = {c: i for i, c in enumerate(labels)}

    def __init__(self, ipStr:str):
        handStr, bidStr = ipStr.split(" ")
        self.string = handStr
        self.bid = int(bidStr)
        cardDic = dict(Counter(dict(Counter(handStr)).values()))

        self.rank = -1
        if 5 in cardDic:
            self.rank = 7
        elif 4 in cardDic:
            self.rank = 6
        elif 3 in cardDic and 2 in cardDic:
            self.rank = 5
        elif 3 in cardDic:
            self.rank = 4
        elif 2 in cardDic and cardDic[2] == 2:
            self.rank = 3
        elif 2 in cardDic:
            self.rank = 2
        else:
            self.rank = 1
        
        



class HandJokerfied:
    labels = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    labelDic = {c: i for i, c in enumerate(labels)}

    def __init__(self, ipStr:str):
        handStr, bidStr = ipStr.split(" ")
        self.string = handStr
        self.bid = int(bidStr)
        cardDic = dict(Counter(handStr))
        jokers = 0
        if "J" in cardDic:
            jokers = cardDic.pop("J")
        print(jokers)
        
        cardDic = dict(Counter(cardDic.values()))

        print(jokers)

        self.rank = -1
        highest = 0
        if len(cardDic) != 0:
            highest = max(cardDic.keys())

        if jokers + highest == 5:
            self.rank = 7
        elif jokers+highest == 4:
            self.rank = 6
        elif (3 in cardDic and 2 in cardDic) or (2 in cardDic and cardDic[2] == 2 and jokers == 1):
            self.rank = 5
        elif highest + jokers == 3:
            self.rank = 4
        elif 2 in cardDic and (cardDic[2] == 2 or jokers == 1):
            self.rank = 3
        elif highest + jokers == 2:
            self.rank = 2
        else:
            self.rank = 1
        

def keyHand(hand: Hand):
    key = 0
    for i, char in enumerate(reversed(hand.string)):
        key += hand.labelDic[char]*100**i
    key += hand.rank*100**5
    return key
    


        




def run1():
    hands = [Hand(line) for line in util.linewise("poker.txt", True)]
    hands.sort(key = keyHand)

    s = 0
    for i, hand in enumerate(hands):
        s += hand.bid * (i+1)
    print(s)

def run2():
    hands = [HandJokerfied(line) for line in util.linewise("poker.txt", True)]
    hands.sort(key = keyHand)

    s = 0
    for i, hand in enumerate(hands):
        s += hand.bid * (i+1)
    print(s)


    