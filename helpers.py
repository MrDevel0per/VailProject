from SkiArea import SkiArea


def makeSkiRun(parsed, lifts, name):
    # Print parsed as a JSON string
    percentages = []
    numRuns = 0
    allRuns = []
    for area in parsed:
        miniArray = CalculatePercentages(area)
        # Add the last value to the number of runs
        numRuns += miniArray[4]
        percentages.append(miniArray[:-1])
        for run in area:
            allRuns.append(run)
    # We now have a list of percentages for each area
    # Calculate the overall percentages for each difficulty
    green = 0
    blue = 0
    black = 0
    doubleBlack = 0

    for area in percentages:
        green += area[0]
        blue += area[1]
        black += area[2]
        doubleBlack += area[3]
    green = green / len(percentages)
    blue = blue / len(percentages)
    black = black / len(percentages)
    doubleBlack = doubleBlack / len(percentages)
    # We make a skiArea
    skiArea = SkiArea(allRuns, green, blue, black, doubleBlack, lifts, name)
    return skiArea

def cleanString(string):
    string = string.replace('FR.TerrainStatusFeed = ', '')
    #Remove all characters starting from FR.LiftStatusFilters and after
    string = string.replace(string[string.find('FR.LiftStatusFilters'):], '')
    #Remove all empty lines
    string = string.replace("""
    """, '')
    #Remove all semicolons
    string = string.replace(';', '')
    return string

def CalculatePercentages(runs):
    #Calculate the percentage of runs that are difficulties 1-4
    #Return a list of percentages
    percentages = []
    #First, scan through runs for each difficulty
    green = 0
    blue = 0
    black = 0
    doubleBlack = 0
    for run in runs:
        # print("SkiRun: " + run.name + " Difficulty: " + newStr(run.difficulty))
        if run.difficulty == 1:
            green += 1
        elif run.difficulty == 2:
            blue += 1
        elif run.difficulty == 3:
            black += 1
        elif run.difficulty == 4:
            doubleBlack += 1
    #Calculate the percentages
    percentages.append(green / len(runs))
    percentages.append(blue / len(runs))
    percentages.append(black / len(runs))
    percentages.append(doubleBlack / len(runs))
    percentages.append(len(runs))
    return percentages