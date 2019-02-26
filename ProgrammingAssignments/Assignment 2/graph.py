# Data Structures II
# Programming Assignment 2
# Note: code was partially provided by : Dr. Vincent A. Cicirello
# Modified by: Daniel W. Anner
from collections import deque
import math

class Graph :
    """Graph represented with adjacency lists."""

    __slots__ = ['_adj']

    def __init__(self, v=10, edges=[]) :
        """Initializes a graph with a specified number of vertices.

        Keyword arguments:
        v - number of vertices
        edges - any iterable of ordered pairs indicating the edges
        """

        self._adj = [ _AdjacencyList() for i in range(v) ]
        for a, b in edges :
            self.add_edge(a, b)



    def add_edge(self, a, b) :
        """Adds an edge to the graph.

        Keyword arguments:
        a - first end point
        b - second end point
        """

        self._adj[a].add(b)
        self._adj[b].add(a)


    def num_vertices(self) :
        """Gets number of vertices of graph."""

        return len(self._adj)


    def degree(self, vertex) :
        """Gets degree of specified vertex.

        Keyword arguments:
        vertex - integer id of vertex
        """

        return self._adj[vertex]._size

    def bfs(self, s) :
        """Performs a BFS of the graph from a specified starting vertex.
        Returns a list of objects, one per vertex, containing the vertex's distance
        from s in attribute d, and vertex id of its predecessor in attribute pred.

        Keyword arguments:
        s - the integer id of the starting vertex.
        """

        class VertexData :
            __slots__ = [ 'd', 'pred' ]

            def __init__(self) :
                self.d = math.inf
                self.pred = None

        vertices = [VertexData() for i in range(len(self._adj))]
        vertices[s].d = 0
        q = deque([s])
        while len(q) > 0 :
            u = q.popleft()
            for v in self._adj[u] :
                if vertices[v].d == math.inf :
                    vertices[v].d = vertices[u].d + 1
                    vertices[v].pred = u
                    q.append(v)
        return vertices

    def dfs(self) :
        """Performs a DFS of the graph.  Returns a list of objects, one per vertex, containing
        the vertex's discovery time (d), finish time (f), and predecessor in the depth first forest
        produced by the search (pred).
        """

        class VertexData :
            __slots__ = [ 'd', 'f', 'pred' ]

            def __init__(self) :
                self.d = 0
                self.pred = None

        vertices = [VertexData() for i in range(len(self._adj))]
        time = 0

        def dfs_visit(u) :
            nonlocal time
            nonlocal vertices

            time = time + 1
            vertices[u].d = time
            for v in self._adj[u] :
                if vertices[v].d == 0 :
                    vertices[v].pred = u
                    dfs_visit(v)
            time = time + 1
            vertices[u].f = time

        for u in range(len(vertices)) :
            if vertices[u].d == 0 :
                dfs_visit(u)
        return vertices






    def print_graph(self) :
        """Prints the graph."""

        for v, vList in enumerate(self._adj) :
            print(v, end=" -> ")
            for u in vList :
                print(u, end="\t")
            print()

    def print_graph_2(self):
        """Prints the graph of the transpose graph. Copied code from print_graph"""
        for v, vList in enumerate(self._adj2):
            print(v, end=" -> ")
            for u in vList:
                print(u, end="\t")
            print()





class Digraph(Graph) :

    def add_edge(self, a, b) :
        self._adj[a].add(b)

    def topological_sort(self) :
        """Topological Sort of the directed graph (Section 22.4 from textbook).
        Returns the topological sort as a list of vertex indices.
        """
        class VertexData:
            __pos__ = ['d', 'f', 'pre']

            def __init__(self):
                self.d = 0
                self.pre = None

        verts = [VertexData() for i in range(len(self._adj))]
        deque = deque()
        pos = 0

        def visit_dfs(i):
            nonlocal pos
            nonlocal verts

            pos += 1
            verts[i].d = pos
            for j in self._adj[i]:
                if verts[j].d == 0:
                    verts[j].pred = i
                    visit_dfs(j)
            pos += 1
            verts[i].f = pos
            deque.appendleft(i)

        for i in range(len(verts)):
            if verts[i].d == 0:
                visit_dfs(i)
        return deque

    def transpose(self) :
        """Computes the transpose of a directed graph. (See textbook page 616 for description of transpose).
        Does not alter the self object.  Returns a new Digraph that is the transpose of self."""
        self._adj2 = [_AdjacencyList() for i in range(len(self._adj))]
        tList = []

        for j, jList in enumerate(self._adj):
            for k in jList:
                self._adj2[k].add(j)
                tList.insert(k, (k, j))

        return (Digraph(len(self._adj2), tList))

    def strongly_connected_components(self) :
        """Computes the strongly connected components of a digraph.
        Returns a list of lists, containing one list for each strongly connected component,
        which is simply a list of the vertices in that component."""

        pass # Remove this pass statement after you implement this method.  Simply here temporarily.

        #       Homework Hints/Suggestions/Etc: See algorithm on page 617.
        #           1) Take a look at algorithm steps 1 and 2 before you do anything.  Notice that Step 1 computes finishing times with DFS,
        #               and step 3 uses vertices in order of decreasing finishing times.  As in the topological sort, don't actually sort
        #               by finishing time (to avoid O(V lg v) step).  However, this is easier than in the topological sort as you already
        #               have a method that will get you what you need.  For step 1 of algorithm you can simply call your topological sort.
        #               That will give you the vertices in decreasing order by finishing time, which is really the intention of algorithm line 1.
        #           2) Line 2 is just the transpose and you implemented a method to compute this above.
        #           3) The DFS in line 3 can be done in a couple ways.  The simplest is NOT to call DFS, but instead to reimplement it here.
        #               In the outer loop, use the vertex ordering obtained from algorithm line 1 (to implement line 3).
        #               And to do line 4, you'll need to have your code generate the list of lists for the return value.




class _AdjacencyList :

    __slots__ = [ '_first', '_last', '_size']

    def __init__(self) :
        self._first = self._last = None
        self._size = 0

    def add(self, node) :
        if self._first == None :
            self._first = self._last = _AdjListNode(node)
        else :
            self._last._next = _AdjListNode(node)
            self._last = self._last._next
        self._size = self._size + 1

    def __iter__(self):
        return _AdjListIter(self)



class _AdjListNode :

    __slots__ = [ '_next', '_data' ]

    def __init__(self, data) :
        self._next = None
        self._data = data



class _AdjListIter :

    __slots__ = [ '_next', '_num_calls' ]

    def __init__(self, adj_list) :
        self._next = adj_list._first
        self._num_calls = adj_list._size

    def __iter__(self) :
        return self

    def __next__(self) :
        if self._num_calls == 0 :
            raise StopIteration
        self._num_calls = self._num_calls - 1
        data = self._next._data
        self._next = self._next._next
        return data




if __name__ == "__main__" :
    # here is where you will implement any code necessary to confirm that your
    # topological sort, transpose, and strongly connected components methods work correctly.
    # Code in this if block will only run if you run this module, and not if you load this module with
    # an import for use by another module.

    G = Digraph(6, [(1, 2), (1, 5), (2, 1), (2, 5), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 5), (4, 3), (5, 4), (5, 1), (5, 2)])
    # G = Digraph(6, [(1, 2), (1, 5), (2, 1), (2, 5), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 5), (4, 3), (5, 4), (5, 1), (5, 2)])
    # G = Digraph(6, [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)])
    # G = Digraph(5, [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)])
    print("Init Graph")
    G.print_graph()

    print("Transpose Graph")
    G.transpose()
    G.print_graph_2()

    pass
