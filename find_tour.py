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


def runTests():
    graphA = [(1, 2), (2, 3), (3, 1)]
    degrees = getDegrees(graphA)
    assert len(degrees) == 3
    assert degrees[1] == 2 and degrees[2] == 2 and degrees[3] == 2

runTests()
