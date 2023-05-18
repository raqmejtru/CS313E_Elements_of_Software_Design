#  File: hiking.py
#  Description: Determine if it is possible for Mary to find two different hotels so that
#               she can travel to each trail exactly once
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020


import sys


class Stack:
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # return the number of elements in the stack
    def size(self):
        return len(self.stack)


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


class Graph:
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == (self.Vertices[i]).get_label():
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # do a depth first search in a graph
    def dfs(self, v):
        stack = Stack()  # create the Stack
        visited = set()

        # mark the vertex v as visited and push it on the Stack
        visited.add(self.Vertices[v].label)
        self.Vertices[v].visited = True
        stack.push(v)

        # visit all the other vertices according to depth
        while not stack.is_empty():
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(stack.peek())
            if u == -1:
                u = stack.pop()
            else:
                visited.add(self.Vertices[u].label)
                self.Vertices[u].visited = True
                stack.push(u)

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            self.Vertices[i].visited = False

        # Return true if graph is connected
        if len(visited) == len(self.Vertices):
            return True
        # Otherwise return False if graph is not connected
        else:
            return False

    def hiking(self):
        connected = self.dfs(0)    # check if graph is connected
        if not connected:          # exit if unconnected graph
            return False

        odd = 0
        for row in self.adjMat:    # for each hotel,
            row_sum = sum(row)     # count number of trails out of hotel
            if row_sum % 2 != 0:   # if odd num of trails,
                odd += 1           # increment odd

        if odd == 2:               # if only two hotels have odd # of trails,
            return True            # Mary can accomplish her goal.
        else:
            return False


def main():
    theGraph = Graph()
    num = 0
    name = ['a', 'b', 'c', 'd', 'e', 'f']
    matrix = []
    # read in the adjacency matrix
    for line in sys.stdin:
        tmp = line.strip().split()
        matrix.append(tmp)
        # add vertex, create adjMat for the graph
        theGraph.add_vertex(name[num])
        num += 1

    # add undirected edge to update adjMat
    for nei in range(len(matrix)):
        for to in range(len(matrix[nei])):
            if matrix[nei][to] == '1':
                theGraph.add_undirected_edge(nei, to)

    # print result
    print(theGraph.hiking())


if __name__ == "__main__":
    main()
