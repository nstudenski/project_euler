from statistics import mode
from numpy import unique

# poker.txt from project euler site
games_file = open('/Users/102414/Desktop/euler/e54_supplement.txt','r').read()

def mode_count(array):
    # I needed a new mode function that returns the number of times the mode(s) occur
    # this is very inefficient, but I'm only dealing with arrays of size 5
    if len(array) == 0:
        return 0
    else:
        try:
            return array.count(mode(array))
        except:
            result = 0
            for i in array:
                count = array.count(i)
                if count > result:
                    result = count
            return result
            
class Card():
    def __init__(self,card):
    # jack = 11
    # queen = 12
    # king = 13
    # ace = 14
        self.suit = card[-1:]
        self.num = card[:-1]
        if self.num == 'T':
            self.num = 10
        elif self.num == 'J':
            self.num = 11
        elif self.num == 'Q':
            self.num = 12
        elif self.num == 'K':
            self.num = 13
        elif self.num == 'A':
            self.num = 14
        else:
            self.num = int(self.num)
            
class Hand():
    def __init__(self,cards):
        self.cards = cards
        self.suits = [card.suit for card in self.cards]
        self.nums = [card.num for card in self.cards]
        self.nums.sort(reverse=True)
        
    def isFour(self):
        # if there are only two unique cards in the deck and the mode occurs 4 times
        return (len(unique(self.nums)) == 2) and (mode_count(self.nums) == 4)
        
    def isFull(self):
        # if there are only two unique cards in the deck and the mode occurs 3 times
        return (len(unique(self.nums)) == 2) and (mode_count(self.nums) == 3)
        
    def isFlush(self):
        # if there is only one unique suit
        return len(unique(self.suits)) == 1
        
    def isStraight(self):
        # if there are 5 unique cards that occur in a sequence (the max is 4 away from the min)
        return (len(unique(self.nums)) == 5) and (max(self.nums) - min(self.nums) == 4)

    def isThree(self):
        # if there are three unique cards and the mode occurs 3 times
        return (len(unique(self.nums)) == 3) and (mode_count(self.nums) == 3)
    
    def isTwoPair(self):
        # if there are three unique cards and the mode occurs 2 times
        return (len(unique(self.nums)) == 3) and (mode_count(self.nums) == 2)
        
    def twoPairValues(self):
        nums = self.nums
        pair_cards = [i for i in nums if nums.count(i) == 2]
        result = [i for i in unique(pair_cards)]
        result.sort(reverse=True)
        return result
                
    def isPair(self):
        # if there are four unique cards
        return (len(unique(self.nums)) == 4)

    def score(self):
        score = 0
        if self.isStraight() and self.isFlush():
            score = 800
        elif self.isFour():
            score = 700 + mode(self.nums)
        elif self.isFull():
            score = 600 + mode(self.nums)
        elif self.isFlush():
            score = 500
        elif self.isStraight():
            score = 400
        elif self.isThree():
            score = 300 + mode(self.nums)
        elif self.isTwoPair():
            vals = self.twoPairValues()
            score = 200 + vals[0] + vals[1] / 100
        elif self.isPair():
            score = 100 + mode(self.nums)
        return score


games = [game.split(' ') for game in games_file.split('\n')]


def score_game(game):
    player1 = Hand([Card(a) for a in game[:5]])
    player2 = Hand([Card(a) for a in game[5:]])
    if player1.score() > player2.score():
        return 1
    elif player1.score() < player2.score():
        return 2
    else:
        for i in range(5):
            if player1.nums[i] > player2.nums[i]:
                return 1
            elif player1.nums[i] < player2.nums[i]:
                return 2
        return 'tie'


results = []
for game in games:
    results.append(score_game(game))