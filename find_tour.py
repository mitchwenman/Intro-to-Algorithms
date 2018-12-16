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
    tour = []
    workingGraph = list(graph) # so we can remove elements
    # your code here
    currNode = getFirstNode(workingGraph)
    tour.append(currNode)
    while len(workingGraph) != 0:
        # find the next edge for the currentNode
        nextEdge = getNextEdge(currNode, workingGraph)
        print "Next Edge: " + str(nextEdge)
        # update currNode
        x, y = nextEdge
        if currNode == x:
            currNode = y
        else:
            currNode = x
        # mark edge as traversed
        tour.append(currNode)
        workingGraph.remove(nextEdge)

    return tour

def getNextEdge(node, graph):
    graphLength = len(graph)
    if graphLength == 1:
        return graph[0] # there's only one edge left
    # find next edge containing node (not sure about this!!)
    for edge in graph:
        if node in edge:
            # check if we're heading down a dead end
            x, y = edge
            if node == x:
                nextNode = y
            else:
                nextNode = x
            followingGraph = list(graph)
            followingGraph.remove(edge)
            if getNextEdge(nextNode, followingGraph):
                return edge
    return None

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
        return graph[0][0] # start with any node, it doesn't matter
    else:
        # find first odd degree node
        for key in degrees.keys():
            if degrees[key] % 2 == 1:
                return key
    return -1

def graphA_Tests():
    # simple graph (Graph A)
    graph = [(1, 2), (2, 3), (3, 1)]
    degrees = getDegrees(graph)
    assert len(degrees) == 3
    assert degrees[1] == 2 and degrees[2] == 2 and degrees[3] == 2
    assert countOdd(degrees) == 0
    firstEdge = getFirstNode(graph)
    assert firstEdge == 1
    tour = find_eulerian_tour(graph)
    print str(tour)

def graphB_Tests():
    # Graph #
    # http://graphonline.ru/en/?graph=CwOwDenRQtayhfcd
    graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),
                (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    degrees = getDegrees(graph)
    assert len(degrees) == 10
    assert degrees[5] == 4
    assert countOdd(degrees) == 0
    assert getFirstNode(graph) == 0
    tour = find_eulerian_tour(graph)
    print tour

def graphC_Tests():
    graph = [(1, 13), (1, 6), (6, 11), (3, 13),
                (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
                (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
                (7, 14),  (10, 13)]
    degrees = getDegrees(graph)
    assert len(degrees) == 15
    assert getFirstNode(graph) == 1
    tour = find_eulerian_tour(graph)
    print tour

def graphD_Tests():
    graph = [ (4, 5), (2, 1), (2, 5), (1, 4),  (5, 6), (6, 3), (3, 2)]
    tour = find_eulerian_tour(graph)
    print tour

def runTests():
    #graphA_Tests()
    #graphB_Tests()
    #graphC_Tests()
    graphD_Tests()


# main
runTests()
