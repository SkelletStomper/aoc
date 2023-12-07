import util




class Scratchcard:
    def __init__(self, raw: str):
        self.times_drawn = 1
        card, numbers  = raw.split(":")
        self.ID = int(card.split(" ")[-1])
        target, have = [number.strip() for number in numbers.split("|")]
        self.target = {int(num) for num in target.split(" ") if num != ""}
        self.have = {int(num) for num in have.split(" ") if num != ""}
    
    def winning_amount(self):
        both = self.target.intersection(self.have)
        if len(both) == 0:
            return 0
        return 2**(len(both)-1)
    def same(self):
        both = self.target.intersection(self.have)
        return len(both)

    def copy_IDs(self) -> list[int]:
        return list[range(self.ID+1, self.ID+1+self.winning_amount())]




def propagate_cards(cards:list[Scratchcard]):
    for ID in range(len(cards)):
        won = cards[ID].same()
        for i in range(ID+1, min([ID+won+1, len(cards)])):
            cards[i].times_drawn += cards[ID].times_drawn


def run1():
    cards = [Scratchcard(line) for line in util.linewise("scratchcards.txt", strip_newlines=True)]
    print(sum([card.winning_amount() for card in cards]))
    
    
def run2():
    cards = [Scratchcard(line) for line in util.linewise("scratchcards.txt", strip_newlines=True)]
    
    propagate_cards(cards)
    print(sum([card.times_drawn for card in cards]))

