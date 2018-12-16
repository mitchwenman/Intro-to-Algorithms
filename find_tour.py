# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]

def find_eulerian_tour(graph):
    # your code here
    return []

def getDegrees(graph):
    degrees = {}
    for edge in graph:
        for node in edge:
            newDegree = degrees.get(node, 0) + 1 # 0 if its the first entry for this node
            degrees[node] = newDegree
    return degrees

def countOdd(elementDict):
    values = elementDict.values()
    numOdd = 0
    for x in values:
        if x % 2 == 1:
            numOdd = numOdd + 1
    return numOdd

def getFirstNode(graph):
    degrees = getDegrees(graph)
    if countOdd(degrees) == 0:
        return graph[0] # start with any node, it doesn't matter
    else:
        # find first odd degree node
        for key in degrees.keys():
            if degrees[key] % 2 == 1:
                return key
    return None

def runTests():
    # simple graph (Graph A)
    graphA = [(1, 2), (2, 3), (3, 1)]
    degreesA = getDegrees(graphA)
    assert len(degreesA) == 3
    assert degreesA[1] == 2 and degreesA[2] == 2 and degreesA[3] == 2
    assert countOdd(degreesA) == 0
    firstNode = getFirstNode(graphA)
    assert firstNode == 1

    # Graph #
    graphB = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),
                (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    degreesB = getDegrees(graphB)
    assert len(degreesB) == 10
    assert degreesB[5] == 4
    assert countOdd(degreesB) == 0


# main
runTests()
