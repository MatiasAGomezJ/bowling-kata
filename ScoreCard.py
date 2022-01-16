from re import I
import string

class ScoreCard:

    def __init__(self, pins):
        self.pins = pins
        self.totalScore = self.calculatePins(pins)

    def setTotal(self, totalScore):
        self.totalScore = totalScore

    def getTotal(self):
        return self.totalScore

    def calculatePins(self, pins):
        totalScore = 0
        
        pins = pins.replace("-", "0")
        pins = pins.replace(" ", "")

        lengthPins = len(pins)

        InsideSpare = False

        TriesLeftInStrike = 0

        InsideDoubleStrike = False

        for index in range(lengthPins):

            frameScore = 0
        
            if pins[index] not in string.digits:
                if pins[index] == "/":
                    frameScore = 10 - int(pins[index-1])
                if pins[index] == "X":
                    frameScore = 10
            else:
                frameScore = int(pins[index])


            if InsideSpare:
                frameScore *= 2
                InsideSpare = False

            if TriesLeftInStrike > 0:

                if InsideDoubleStrike:
                    frameScore *=3
                    InsideDoubleStrike = False
                else:
                    frameScore *=2
                    
                TriesLeftInStrike -= 1

            totalScore += frameScore

            if pins[index] == "/":
                if lengthPins - index == 2:
                    continue
                InsideSpare = True

            if pins[index] == "X":
                if lengthPins - index <= 3:
                    continue
                if TriesLeftInStrike == 1:
                    InsideDoubleStrike = True
                TriesLeftInStrike = 2


        return totalScore

if __name__ == '__main__':

    def test():
        #      "-- -- -- -- -- -- -- -- -- ---"
        pins = "-- -- -- -- -- -- -- -- -- XXX"
        total = 30
        scoreCard = ScoreCard(pins)
        assert scoreCard.getTotal() == total

    test()