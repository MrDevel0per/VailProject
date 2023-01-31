import requests
from bs4 import BeautifulSoup
from SkiArea import SkiArea
import csv
import numpy as np
from helpers import *
from Parser import JSONParser
import json
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}

def main():
    bcUrl = "https://www.beavercreek.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx"
    vailURL = "https://www.vail.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx"

    bcOrVail = input("Would you like to see Beaver Creek or Vail? (bc/vail)")
    if bcOrVail == 'bc':
        data = getData(bcUrl)
    else:
        data = getData(vailURL)
    # num_runs = input_string("How many runs would you like?")
    fileName = input("What would you like to name the RUNS file? Use __name__ for the name of the mountain. Use __num__ for the number of runs.")

    script = parseScript(data)
    skiArea = JSONParser().parseJSON(script, areaName(bcOrVail))
    liftName = parseFileName(input(
        "What would you like to name the **LIFTS** file? Use __name__ for the name of the mountain. Use __num__ for the number of lifts."),
                             skiArea.name, len(skiArea.lifts))
    difficulties = input("Do you want to see the percentages of each difficulty? (y/n)")
    fileName = parseFileName(fileName, skiArea.name, len(skiArea.runs))
    if difficulties == 'y':
        difficulties = True
    else:
        difficulties = False
    if difficulties:
        print("Percentage of green runs: ", skiArea.percentageGreen)
        print("Percentage of blue runs: ", skiArea.percentageBlue)
        print("Percentage of black runs: ", skiArea.percentageBlack)
        print("Percentage of double black runs: ", skiArea.percentageDoubleBlack)
    #We now write the skiArea.runs to a file
    with open(f'/Users/owen/Downloads/{fileName}', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'difficulty', 'difficultyNumber', 'isopen', 'isgroomed', 'info', 'length', 'type', 'isTrailWork', 'area'])
        for run in skiArea.runs:
            writer.writerow([run.id, run.name, parseDif(run.difficulty), run.difficulty, run.isopen, run.isgroomed, run.info, run.length, run.type, run.isTrailWork, run.area])
        #Save the file
        csvfile.close()
    with open(f'/Users/owen/Downloads/{liftName}', 'w', newline='') as csvfile:
       writer = csv.writer(csvfile)
       #Do the chairlifts that were in the JSOn
       writer.writerow(['name', 'status', 'type', 'WaitTimeInMinutes', 'Capacity', 'OpenTime', 'CloseTime', 'Mountain'])
       for lift in skiArea.lifts:
           writer.writerow(
               [lift.name, makeStatus(lift.status), lift.type, lift.WaitTimeInMinutes, lift.Capacity, lift.OpenTime, lift.CloseTime,
                lift.Mountain])


def getData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def makeStatus(stat):
    if stat == 1:
        return "Open"
    elif stat == 2:
        return "Closed"
    elif stat == 3:
        return "Scheduled"
def parseScript(data):
    # Scan for the scripts
    scripts = data.find_all('script')
    # Find the script with the data
    newScripts = []
    for script in scripts:
        if script.has_attr('type'):
            if script['type'] == 'module':
                # Check if the script text contains "FR.TerrainStatusFeed"
                if "FR.TerrainStatusFeed" in script.text:
                    newScripts.append(script)
    finalScript = cleanString(newScripts[0].text)
    return finalScript

def parseDif(num):
    if num == 1:
        return "Green"
    elif num == 2:
        return "Blue"
    elif num == 3:
        return "Black"
    elif num == 4:
        return "Double Black"
    else:
        return "Green"


def parseFileName(input_string, name, run_number):
    # Replace __name__ with the name of the mountain
    # Replace __num__ with the number of runs
    input_string = input_string.replace("__name__", name)
    input_string = input_string.replace("__num__", str(run_number))
    if not input_string.endswith(".csv"):
        input_string += ".csv"
    print("Input string: ", input_string)
    return input_string

def areaName(newStr):
    if newStr == "bc":
        return "Beaver Creek"
    elif newStr == "vail":
        return "Vail"
    else:
        return "Vail"
if __name__ == '__main__':
    main()