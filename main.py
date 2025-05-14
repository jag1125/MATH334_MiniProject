COLORS = {
    "RED": ["1", "2", "3"],
    "BLUE": ["A", "C", "E"],
    "YELLOW": ["N", "Q", "R"],
    "GREEN": ["4", "5", "6"],
    "ORANGE": ["B", "D", "F", "M"],
    "BROWN": ["J", "Z"],
    "GRAY": "L",
    "PURPLE": "7",
    "LIME": "G",
    "GRAY": ["L", "S"]
}

# Determining the color for the visual representation later
def determineColor(lineName):
    for color in COLORS:
        if lineName in COLORS[color]:
            return color
    return "GRAY"

class Stop():
    def __init__(self, name):
        self.name = name
        self.goesTo = []

    def __str__(self):
        return self.name

class Line():
    def __init__(self, lineName):
        self.lineName = lineName
        self.stops = []
        self.color = determineColor(lineName)

    def __str__(self):
        return self.lineName

lines = []
linesDict = {}

# Initializing subway information with dataset
with open("MTA_Subway_Stations.csv", "r") as reader:
    added = []
    for line in reader:
        curr = line.split(",")
        tempLines = []
        # Adding lines into lines list
        if len(curr[8]) == 1:
            if curr[8] not in added:
                added.append(curr[8])
                lines.append(Line(curr[8]))
                tempLines.append(lines[-1])
                linesDict[curr[8]] = lines[-1]
            else:
                tempLines.append(linesDict[curr[8]])
        elif " " in curr[8]:
            temp = (curr[8]).split(" ")
            for val in temp:
                if len(val) == 1 and val not in added:
                    added.append(val)
                    lines.append(Line(val))
                    tempLines.append(lines[-1])
                    linesDict[val] = lines[-1]
                elif len(val) == 1:
                    tempLines.append(linesDict[val])
        else:
            continue

        # Adding stop to adjacency lists
        for i in range(len(tempLines)):
            (tempLines[i].stops).append(Stop(curr[5]))
            for x in range(i, len(tempLines)):
                pass

    reader.close()

for line in lines:
    print(line)

print("--------------")

for stopNames in lines[5].stops:
    print(stopNames) 

print("--------------")

for adjacent in lines[5].stops[21].goesTo:
    print(adjacent)
        
        

        


