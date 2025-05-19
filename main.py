from getData import Stop, Line, addStopsToLine, orderStops, lines, linesDict, stopsDict
from collections import deque

def bfs_path(start_name, end_name):
    start = stopsDict.get(start_name)
    end = stopsDict.get(end_name)

    if not start or not end:
        return None
    
    queue = deque()
    queue.append((start, [start.name]))
    visited = set()
    visited.add(start)

    while queue:
        current_stop, path = queue.popleft()

        if current_stop == end:
            return path

        # Go through the current line
        for line in current_stop.goesTo:
            stops = line.orderedStops
            if current_stop in stops:
                idx = stops.index(current_stop)
                neighbors = []
                if idx > 0:
                    neighbors.append(stops[idx - 1])
                if idx < len(stops) - 1:
                    neighbors.append(stops[idx + 1])

                for neighbor in neighbors:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor.name]))

        #  Check transfers
        for line in current_stop.goesTo:
            for stop in line.orderedStops:
                if stop.name == current_stop.name and stop != current_stop and stop not in visited:
                    visited.add(stop)
                    queue.append((stop, path + [stop.name]))

    return None

def interact():

    linesStr = ""
    for line in range(len(lines) - 1):
        linesStr += f"{lines[line]}, "
    linesStr += f"{lines[-1]}\n"
    print("\nWelcome to the MTA Subway System! From the list below, which subway line are you starting at?")
    print(linesStr)
    chosenLine = input()

    # Invalid response
    while chosenLine.upper() not in linesDict:
        print("\nInvalid Response. Which subway line are you starting at? (Hint: Choose from the list!)")
        print(linesStr)
        chosenLine = input()

    possibleStarts = ""
    for stop in range(len(linesDict[chosenLine].orderedStops) - 1):
        possibleStarts += f"{linesDict[chosenLine].orderedStops[stop].name}, "
    possibleStarts += f"{linesDict[chosenLine].orderedStops[-1].name}\n"
    print("\nPlease choose a stop from below to start at. \nIt's important that you enter it exactly as it's shown in the list below!")
    print(possibleStarts)

    # Invalid response
    chosenStop = input()
    while chosenStop not in possibleStarts and chosenStop not in ", ":
        print("\nInvalid Response. Which stop are you starting from? (Hint: Choose from the list!)")
        print(possibleStarts)
        chosenStop = input()

    print("\nTo find a destination, choose a subway line again.")
    print(linesStr)
    chosenLine2 = input()

    # Invalid response
    while chosenLine2.upper() not in linesDict:
        print("\nInvalid Response. Which subway line has your destination? (Hint: Choose from the list!)")
        print(linesStr)
        chosenLine2= input()

    possibleEnds = ""
    for stop in range(len(linesDict[chosenLine2].orderedStops) - 1):
        possibleEnds += f"{linesDict[chosenLine2].orderedStops[stop].name}, "
    possibleEnds += f"{linesDict[chosenLine2].orderedStops[-1].name}\n"
    print("\nPlease choose a stop from below to end at. \nIt's important that you enter it exactly as it's shown in the list below!")
    print(possibleEnds)

    # Invalid response
    endStop = input()
    while endStop not in possibleEnds and endStop not in ", ":
        print("\nInvalid Response. Which stop are you starting from? (Hint: Choose from the list!)")
        print(possibleEnds)
        endStop = input()
    
    foundPath = bfs_path(chosenStop, endStop)
    if foundPath == None:
        print("We couldn't find a path between those two stops, sorry! :(")
        return
    
    pathStr = ""
    for stop in range(len(foundPath) - 1):
        pathStr += f"{foundPath[stop]} -> "
    pathStr += f"{foundPath[-1]}"

    print(f"\nYour path from {chosenStop} to {endStop} is:\n{pathStr}\n")
    print("Thank you for using my program and enjoy your trip!\n")

interact()
