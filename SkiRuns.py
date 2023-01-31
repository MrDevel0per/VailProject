import requests
from bs4 import BeautifulSoup
from SkiArea import SkiArea
import csv
import numpy as np
from helpers import *
from Parser import JSONParser
import re
from pathlib import Path
def main():

    downloads_path = str(Path.home() / "Downloads")
    bcUrl = "https://www.beavercreek.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx"
    vailURL = "https://www.vail.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx"
    newUrl = input("Enter the URL of the mountain you want to scrape. Make sure it is in the following format: https://www.RESORTNAME.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx: ")
    if checkUrl(newUrl):
        data = getData(newUrl)
    else:
        bcOrVail = input("The URL did not match. Would you like to see Beaver Creek or Vail? (bc/vail)")
        if bcOrVail == 'bc':
            data = getData(bcUrl)
            newUrl = bcUrl
        else:
            data = getData(vailURL)
            newUrl = vailURL
    # num_runs = input_string("How many runs would you like?")
    fileName = input("What would you like to name the **RUNS** file? Use __name__ for the name of the mountain. Use __num__ for the number of runs.")

    script = parseScript(data)
    skiArea = JSONParser().parseJSON(script, areaName(newUrl))
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
    with open(f'{downloads_path}{fileName}', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'difficulty', 'difficultyNumber', 'isopen', 'isgroomed', 'info', 'length', 'type', 'isTrailWork', 'area'])
        for run in skiArea.runs:
            writer.writerow([run.id, run.name, parseDif(run.difficulty), run.difficulty, run.isopen, run.isgroomed, run.info, run.length, run.type, run.isTrailWork, run.area])
        #Save the file
        csvfile.close()
    with open(f'{downloads_path}{liftName}', 'w', newline='') as csvfile:
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
    # print("Input string: ", input_string)
    return input_string

def areaName(newStr):
    if newStr == "bc":
        return "Beaver Creek"
    elif newStr == "vail":
        return "Vail"

    #Check if it matches the regex
    if checkUrl(newStr):
        #Since it does, get the RESORTNAME and return it here: https://www.RESORTNAME.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx
        regex = r"https://www\.\w+\.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx"
        #Get the name of the resort
        #Get everything after the https://www. before the next /
        resortName = re.search(r"https://www\.(\w+)\.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx", newStr).group(1)


        #Return the name of the resort
        return resortName

    return "Vail"

def checkUrl(url):
    #Using regex, check if it matches this: https://www.RESORTNAME.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx
    #RESORTNAME can be any string
    #If it does, return true
    #If it doesn't, return false
    regex = r"https://www\.\w+\.com/the-mountain/mountain-conditions/terrain-and-lift-status.aspx"
    if re.match(regex, url):
        return True
    else:
        return False
if __name__ == '__main__':
    main()
