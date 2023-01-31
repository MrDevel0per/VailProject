class SkiRun:
    def __init__(self, id, name, difficulty, isopen, isgroomed, info, length, type, isTrailWork, area):
        self.id = id
        self.name = name
        self.difficulty = difficulty
        self.isopen = isopen
        self.isgroomed = isgroomed
        self.info = info
        self.length = length
        self.type = type
        self.isTrailWork = isTrailWork
        self.area = area

class Chairlift:
    def __init__(self, name, status, type, Mountain, WaitTimeInMinutes, Capacity, OpenTime, CloseTime):
        self.name = name
        self.status = status
        self.type = type
        self.Mountain = Mountain
        self.WaitTimeInMinutes = WaitTimeInMinutes
        self.Capacity = Capacity
        self.OpenTime = OpenTime
        self.CloseTime = CloseTime