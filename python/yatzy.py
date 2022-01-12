class Yatzy:

    @staticmethod
    def chance(d1: int, d2: int, d3: int, d4: int, d5: int):
        return d1 + d2 + d3 + d4 + d5

    @staticmethod
    def yatzy(dices: list):
        if dices.count(dices[0]) == 5:
            return 50
        return 0
    
    @staticmethod
    def ones(*dices):
        return dices.count(1)
    
    @staticmethod
    def twos(*dices):
        return dices.count(2) * 2
    
    @staticmethod
    def threes(*dices):
        return dices.count(3) * 3
    
    @staticmethod
    def fours(*dices):
        return dices.count(4) * 4
    
    @staticmethod
    def fives(*dices):
        return dices.count(5) * 5
    
    @staticmethod
    def sixes(*dices):
        return dices.count(6) * 6
    
    @staticmethod
    def score_pair(*dices: list):
        for value in reversed(range(1,7)):
            if dices.count(value) == 2:
                return value * 2
        return 0
    
    @staticmethod
    def two_pair(*dices: list):
        result = 0
        pair = 0
        for value in range(1,7):
            if dices.count(value) >= 2:
                result+=value * 2
                pair+=1
        return result if pair > 1 else 0
    
    @staticmethod
    def four_of_a_kind(*dices: list):
        for value in range(1,7):
            if dices.count(value) >= 4:
                return value * 4
        return 0
    

    @staticmethod
    def three_of_a_kind(*dices: list):
        for value in range(1,7):
            if dices.count(value) >= 3:
                return value * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
