import random
from SkiRun import SkiRun

class SkiArea:
    def __init__(self, runs, percentageGreen, percentageBlue, percentageBlack, percentageDoubleBlack, lifts, name):
        self.runs = runs
        self.percentageGreen = percentageGreen
        self.percentageBlue = percentageBlue
        self.percentageBlack = percentageBlack
        self.percentageDoubleBlack = percentageDoubleBlack
        self.lifts = lifts
        self.name = name

    def getRandomRuns(self, count):
        #We want to return a list of runs
        #We will get a number of runs from each difficulty, based on percentages of runs of that difficulty
        #We will then return a list of runs
        returnable = []
        greens = []
        blues = []
        blacks = []
        doubleBlacks = []
        for run in self.runs:
            if run.difficulty == 1:
                greens.append(run)
            elif run.difficulty == 2:
                blues.append(run)
            elif run.difficulty == 3:
                blacks.append(run)
            elif run.difficulty == 4:
                doubleBlacks.append(run)
        #Now, calculate how many runs we need to get from each difficulty
        #We do this by taking the percentages and getting that percent as an integer from the count
        #We then get that many runs from each difficulty
        #We then add them to the returnable list
        #We then return the list
        greenCount = int(self.percentageGreen * count)
        blueCount = int(self.percentageBlue * count)
        blackCount = int(self.percentageBlack * count)
        doubleBlackCount = int(self.percentageDoubleBlack * count)
        for i in range(greenCount):
            #Get a random green run
            run = greens[random.randint(0, len(greens) - 1)]
            returnable.append(run)
            greens.remove(run)
        for i in range(blueCount):
            #Get a random blue run
            run = blues[random.randint(0, len(blues) - 1)]
            returnable.append(run)
            blues.remove(run)
        for i in range(blackCount):
            # Get a random blue run
            run = blacks[random.randint(0, len(blues) - 1)]
            returnable.append(run)
            blacks.remove(run)
        for i in range(doubleBlackCount):
            # Get a random blue run
            run = doubleBlacks[random.randint(0, len(blues) - 1)]
            returnable.append(run)
            doubleBlacks.remove(run)
        return returnable