###
# Author: Daniel W. Anner
# Data Structures and Algorithms 2
# Programming Assignment 4
###

import math
# Add any relevant import statements up here.


# Programming Assignment 4:
# Follow the instuctions in comments throughout this file.
# Don't rename any methods, attributes, functions, etc.
# Also don't change order or type of parameters.
# You might consider doing the assignment in this order: 1, 2, 5, 6a, 3, 4, 6b.

class WeightedAdjacencyMatrix :

    # Although technically you do not need to declare variables, including object attributes
    # prior to first use, a consequence of that is that Python must allocate more memory than
    # actually needed because it has no way of knowing how much you will need.
    # __slots__ offers a way of being more memory efficient.  It tells Python exactly what
    # attributes this class will have.  In this case, only a field named _W.  So Python will
    # only allocate enough memory for the attributes specified in __slots__ (just separate by commas
    # if you need more than one).
    # If you try to specify an attribute that is not included in this list you will get a runtime
    # exception.
    __slots__ = ['_W']

    # 1) Implement the initializer, which should create a matrix (i.e., list of lists) with
    # number of rows and columns both equal to size (i.e., number of vertices).
    # Initially there are no edges, which means that the weights should all initially
    # be infinity (inf in Python), other than the diagonal which should have 0s (cost of
    # shortest path from a vertex u to itself is 0).
    #
    # Use the attribute I provided above in __slots__ for your matrix _W (see comment above).
    # Remember to use self for an object attribute (i.e., self._W )
    def __init__(self, size) :
        """Initializes a weighted adjacency matrix for a graph with size nodes.

        Graph is initialized with size nodes and 0 edges.

        Keyword arguments:
        size -- Number of nodes of the graph.
        """
        self._W = [] #create out bare list
        for i in range(size**2): #kwargs for size
            self._W.append(math.inf) #init the weight to infinity

        theMatrix = map(list, zip(*[iter(self._W)] * size)) #use zip to make iterator of tuples, and map to create list of results
        self._W = list(theMatrix) # then convert the tuples to a list again
        for i in range(size):
            self._W[i][i] = 0 # set all the diagonals to 0


    # 2) Implement this method (see the provided docstring)
    def add_edge(self, u, v, weight) :
        """Adds a directed edge from u to v with the specified weight.

        Keyword arguments:
        u -- source vertex id (0-based index)
        v -- target vertex id (0-based index)
        weight -- edge weight
        """
        self._W[u][v] = weight #simply setting the weights


    # 5) Implement this method (see the provided docstring)
    def floyd_warshall(self) :
        """Floyd Warshall algorithm for all pairs shortest paths.

        Returns a matrix D consisting of the weights of the shortest paths between
        all pairs of vertices.  This method does not change the weight matrix of the graph itself.

        Extra Credit version: Returns a tuple (D, P) where D is a matrix consisting of the
        weights of the shortest paths between all pairs of vertices, and P is the predecessors matrix.
        """
        D = [] # init our weight matrix
        P = [] # init our predecessors list
        for i in range(len(self._W)):
            D.append(self._W[i].copy()) # copy our elements to D, so we dont mess with our master list

        # TODO: add the logic to store predecessors for the extra credit
        for i in range(len(D)): # iterate through the list
            for j in range(len(D)): # second loop for our matrix
                for k in range(len(D)): # last loop for our matrix
                    if D[j][i] + D[i][k] < D[j][k]:
                        D[j][k] = D[j][i] + D[i][k]

        return D



# 3) Implement this function.  First note the lack of indentation.  This is not a method of the above class.
# It is a function.
# You can find the relevant equation for haversine distance at this link (and others):
# https://www.movable-type.co.uk/scripts/latlong.html
# That link also includes javascript for computing haversine distance.
# It should be straightforward to translate this to Python.
# Note the constant R in the equation controls the units of measure, and make sure you set it
# appropriately for meters as indicated in the docstring below.
# See documentation of Python's math functions for any needed trig functions as well as degree
# to radian conversion: https://docs.python.org/3/library/math.html
def haversine_distance(lat1, lng1, lat2, lng2) :
    """Computes haversine distance between two points in latitude, longitude.

    Keyword Arguments:
    lat1 -- latitude of point 1
    lng1 -- longitude of point 1
    lat2 -- latitude of point 2
    lng2 -- longitude of point 2

    Returns haversine distance in meters.
    """
    lat1_r = math.radians(lat1) # convert the lat1 to radians
    lat2_r = math.radians(lat2) # convert the lat2 to radians
    lng1_r = math.radians(lng1) # convert the lng1 to radians
    lng2_r = math.radians(lng2) # convert the lng2 to radians

    latdif = lat2_r - lat1_r # get the difference for the distance of latitude
    lngdif = lng2_r - lng1_r # get the difference for the distance of longitude

    i = math.sin(latdif / 2)**2
    j = math.cos(lat1_r)
    k = math.cos(lat2_r)
    l = math.sin(lngdif / 2)**2

    pre = i + j * k * l

    answer = 2 * math.atan2(math.sqrt(pre), math.sqrt(1 - pre))

    return 6378137 * answer


# 4) Implement this function.  First note the lack of indentation.  This is not a method of the above class.
# It is a function.
#
# Specifically, it should be able to parse a file of the format from this set of graphs: http://tm.teresco.org/graphs/
# Details of the format itself can be found here: http://courses.teresco.org/metal/graph-formats.shtml
# Only worry about the "simple" format (and NOT the "collapsed" format).
# You might start by looking at one of the smaller graphs to see what the format looks like, such as Andora.
# First line of all files is: TMG 1.0 simple
# Second line tells you number of vertices and number of edges: V E
# The next V lines provide one vertex per line of the form: StringID  latitude  longitude
# You only really need the latitude and longitude values, and simply use 0 to V-1 as the vertex ids instead of the given
# strings.
# The next E lines provide the edges, one per line, of the form: from to aValueYouDontNeedForThisAssignment.
# You only need the from and to values, and not the 3rd value on the line.
# The from and to tell you the endpoints of an edge (0 based indices into the list of vertices).
# For each edge in this list add two directed edges to the WeightedAdjacencyMatrix (one in each direction).
# The weight for the edge should be the so-called haversine distance (which you implemented a function to
# compute in Step 3.
#
# HINTS (for parsing input file):
# You can find Python file IO examples here: https://docs.python.org/3/tutorial/inputoutput.html
# Scroll to 7.2 and look at examples of open. Specifically, see example that uses "with" which
# has the advantage that Python will automatically close the file for you at the end of the with block.
#
# The call to read() in that example, however, reads the entire file at once as a String.
# You will find it useful, to instead iterate over the lines of the file.  You can either use the readline
# method directly for this.  Or, see the example on that same page that uses a loop of the form:
# for line in f (each iteration of this loop will automatically call readline to get the next line of
# the file and loop will iterate over entire file).
#
# Useful methods for parsing the input graph file:
# The split method for Strings: https://docs.python.org/3/library/stdtypes.html#string-methods
#
# Converting String that is a number to a number type:
# float(s) will convert a string s that contains a floating-point number to a floating point number.
# For example,
# s = "101.25"  # s is a string that happens to look like a floating-point number.
# v = float(s)  # v will now have the floating-point value 101.25
# Likewise, int(s) will do the same but for integer values.
#
def parse_highway_graph_data(filename) :
    """Parses a highway graph file and returns a WeightedAdjacencyMatrix.

    Keyword arguments:
    filename -- name of the file.

    Returns a WeightedAdjacencyMatrix object.
    """

    with open(filename) as file:
        list = []
        list = file.readlines()

        for word in list:
            print("test", type(word))
            list.append(word.split(',')) # split the words by the ,
        for num in list[0]:
            edgeList = num.split() # grab the vertices and edges from the file

        # main for loops done, lets init our values for lat/lng
        vertices = edgeList[0] # init the first vert to the edge vertifices list
        vertices = int(vertices) # cast the vertices to int type
        coordinates = [] # init lsit for coordinates
        coordinateValues = [] # init list for coordinate values
        edges = edgeList[1] # create edges list
        edges = int(edges) # cast edges to int type
        latitudeList = [] # init list for lat values
        longitudeList = [] # init list for lng values

        for val in list[1:vertices + 1]:
            coordinates.append(val) # get the lat/lng coordinates from our file data

        for index in range(len(coordinates)):
            for val in coordinates[index]:
                coordinateValues.append(val.split())  # get the lat/lng coordinate values from our file data

        for val in coordinateValues: # add values to the list
            x = val[1]
            float(x) # cast to float  type
            latitudeList.append(x) # cast to the latitue list
            y = val[2]
            float(y) # cast to float type
            longitudeList.append(y) # append to the longitude list

        # lat/lng done, init values to assign edges
        edgeValues = []
        actualEdges = []
        splitEdges = []
        edgeList1 = []
        edgeList2 = []
        for val in list[edges + 2:]:
            edgeValues.append(val) # append the edge values
        for val in edgeValues:
            actualEdges.append(val) # append the actual values - this is a shim to get the proper Data
            #TODO: condense this into one loop

        for index in range(len(actualEdges)): # we need index locations
            for val in actualEdges[index]: # for each value at this location
                splitEdges.append(val.split()) # add the edges in the split format
        for val in splitEdges: # add our data to the actual lists
            x = val[0]
            int(x)
            edgeList1.append(x)
            y = val[1]
            int(y)
            edgeList2.append(y)

        matrix = WeightedAdjacencyMatrix(vertices) # add the values into a new matrix
        for i in range(len(edgeList1)): # iterate through the edges - we only need to use one list to create the range, since they should be the same length
            eStart = int(edgeList1[i]) # cast to int, create start
            eEnd = int(edgeList2[i]) # cast to int, create end

            latStart = float(latitudeList[eStart]) # cast to float, create start for latitude
            latEnd = float(latitudeList[eEnd]) # cast to float, create end for latitue
            lngStart = float(longitudeList[eStart]) # cast to float, create start for longitude
            lngEnd = float(longitudeList[eEnd]) # cast to float, create end for longitude

            dist = haversine_distance(latStart, lngStart, latEnd, lngEnd) # get the distance with our haversine distance method
            matrix.add_edge(eStart, eEnd, dist) # add the edge
            matrix.add_edge(eEnd, eStart, dist)

        return matrix


# 6a) This function should construct a WeightedAdjacencyMatrix object with the vertices and edges of your choice
# (small enough that you can verify that your Floyd Warshall implementation is correct).
# After constructing the WeightedAdjacencyMatrix object, call your floyd_warshall method, and then
# output the D matrix it returns using print statements (one row of matrix per line, columns separated by tabs).
# If you also computed the predecessor matrix, then output that as well (print a blank line between the matrices).
def test_with_your_own_graphs() :
    m = WeightedAdjacencyMatrix(5)

    m.add_edge(0, 1, 8)
    m.add_edge(1, 0, 8)
    m.add_edge(2, 1, 3)
    m.add_edge(1, 2, 3)
    m.add_edge(2, 3, 7)
    m.add_edge(3, 2, 7)
    m.add_edge(3, 0, 14)
    m.add_edge(4, 1, 9)
    m.add_edge(1, 4, 9)
    m.add_edge(0, 4, 12)
    m.add_edge(4, 0, 12)

    print("Floyd Warshall Graph")
    g = m.floyd_warshall()
    for i in g:
        print(*i, sep='\t')


# 6b) This function should use your parseHighwayGraphData to get a WeightedAdjacencyMatrix object corresponding
# to the graph of your choice from http://tm.teresco.org/graphs/ (I recommend starting with one of the small graphs).
# Then use your floyd_warshall method to compute all pairs shortest paths.
# Don't output the entire matrix since that would be a bit large (even for the smaller graphs).
# Instead, the parameter to the function below is a list of 2-tuples.  For each 2-tuple, of the form (from, to)
# in this list, print on one line (in this order): from to distance
# If you implemented the extra credit part (the predecessors), then each line of output should be of the form:
# from to distance pathTaken
# You should do this with at least one graph from the linked site, but I recommend trying it with multiple.
# In what you submit, have this function work with one graph (of your choice).
# Upload that graph when you submit your assignment (in case the page updates the data, this way I'll have the exact
# graph that you used).
def test_with_highway_graph(L) :
    b = parse_highway_graph_data('inputs/IND-GJ-region.txt')
    g = b.floyd_warshall()

    for i in g:
        print(i)
    for i in L:
        print(i[0], i[1], g[i[0]][i[1]])

if __name__ == "__main__":
    print("IND-GJ-region Graph Data")
    test_with_highway_graph([(1, 0), (2, 3)])
    print("Test with own Graphs example")
    test_with_your_own_graphs()
