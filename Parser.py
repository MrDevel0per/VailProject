import json

from SkiArea import SkiArea
from SkiRun import SkiRun, Chairlift
from helpers import *


class JSONParser:
    def parseJSON(self, jsonString, name):
        data = json.loads(jsonString)
        returnable = []
        lifts = []
        data['GroomingAreas'].pop(0)
        for area in data['GroomingAreas']:
            returnable.append(self.parseGroomingArea(area, area['Name']))
        for lift in data['Lifts']:
            lifts.append(self.parseLifts(lift))
        skiArea = makeSkiRun(returnable, lifts, name)
        return skiArea

    def parseGroomingArea(self, data, area):
        runs = []
        for run in data['Trails']:
            # print(run)
            newRun = self.parseRun(run, area)
            runs.append(newRun)
            print(newRun.name)
            if newRun.name == 'Golden Peak Terrain Park - Middle':
                print(newRun.difficulty)
        return runs

    def parseRun(self, run, area):
        return SkiRun(run['Id'], run['Name'], run['Difficulty'], run['IsOpen'], run['IsGroomed'], run['TrailInfo'],
                      run['TrailLength'], run['TrailType'], run['IsTrailWork'], area)

    def parseLifts(self, lift):
        return Chairlift(lift['Name'], lift['Status'], lift['Type'], lift['Mountain'], lift['WaitTimeInMinutes'],
                         lift['Capacity'], lift['OpenTime'], lift['CloseTime'])
