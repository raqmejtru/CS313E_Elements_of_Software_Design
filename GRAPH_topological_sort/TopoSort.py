#  File: TopoSort.py
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 04/07/2023
#  Date Last Modified: 04/07/2023

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

    def clear(self):
        self.stack = []

    def __str__(self):
        return self.stack


class Queue:
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    def current(self):
        return self.queue[0]

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
        self.Vertices = []  # a list of vertex objects
        self.adjMat = []  # adjacency matrix of edges

    # return number of vertices
    def num_vertices(self):
        return len(self.Vertices)

    # check if a vertex is already in the graph
    def has_vertex(self, label) -> bool:
        for i in range(self.num_vertices()):
            if label == self.Vertices[i].get_label():
                return True
        return False

    # given a label get the index of a vertex
    def get_index(self, label) -> int:
        for i in range(self.num_vertices()):
            if label == self.Vertices[i].get_label():
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        for i in range(self.num_vertices() - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(self.num_vertices()):
            new_row.append(0)
        self.adjMat.append(new_row)

    # print `index: label` for all vertices
    def print_vertices(self):
        for i in range(self.num_vertices()):
            print(f'{i}: {self.Vertices[i]}')

    # get adjacency list from adjacency matrix
    def get_adj_list(self) -> dict:
        adj_list = {}
        for from_v in range(self.num_vertices()):
            adj_list[from_v] = []
            for to_v in range(0, len(self.adjMat[from_v])):
                if self.adjMat[from_v][to_v] != 0:
                    adj_list[from_v].append(to_v)
        return adj_list

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # return the first unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited(self, v: int) -> int:
        for i in range(self.num_vertices()):
            if self.adjMat[v][i] > 0 and not self.Vertices[i].was_visited():
                return i
        return -1

    # return list of vert(ex/ices) that are adjacent to vertex v (index)
    def get_adj_directed(self, v: int) -> list:
        verts = []
        for i in range(self.num_vertices()):
            if self.adjMat[v][i] > 0:
                verts.append(i)
        return verts

    # return list of vert(ex/ices) that point to v or that v points to
    def get_adj_mutual(self, v: int) -> list:
        verts = []
        for i in range(self.num_vertices()):
            if self.adjMat[v][i] > 0 or self.adjMat[i][v] > 0:
                verts.append(i)
        return verts

    # do the depth first search in a graph from vertex v (index)
    # returns True if cycle detected from given start node `v`
    def dfs(self, v: int) -> bool:
        stack = Stack()                               # create empty stack
        cyclic = False                                # cycle check

        self.Vertices[v].visited = True               # mark input vertex v as visited
        stack.push(v)                                 # push input vertex onto stack

        # depth first search
        while not stack.is_empty() and not cyclic:
            u = self.get_adj_unvisited(stack.peek())  # peek adjacent unvisited vertex

            if v in self.get_adj_directed(u):         # if v is adjacent to u,
                if u in self.get_adj_mutual(v):       # and if u and v point to each other,
                    cyclic = True                     # then a cycle was detected.

            if u == -1:                               # if u has already been visited,
                stack.pop()                           # remove from stack.

            else:
                self.Vertices[u].visited = True       # otherwise mark u as visited
                stack.push(u)                         # and push u to stack.

        # stack is empty or cycle exists, reset all vertices to unvisited.
        for i in range(self.num_vertices()):
            self.Vertices[i].visited = False

        return cyclic

    # determine if a directed graph has a cycle
    def has_cycle(self) -> bool:
        for v in range(self.num_vertices()):  # perform dfs on all vertices,
            if self.dfs(v):                   # if not cyclic,
                return True                   # return true

    # determine the number of parents that each node has, used for topological sort.
    def get_num_parents(self) -> dict:
        # key = index of the current vertex: value = number of parents
        num_parents = {v: 0 for v in range(self.num_vertices())}
        adj_list = self.get_adj_list()

        # Iterate through the maximum number of edges possible in graph
        for from_v in range(self.num_vertices()):
            for to_v in adj_list[from_v]:
                num_parents[to_v] += 1

        return num_parents

    # return a list of vertex labels after a topological sort
    def toposort(self) -> list:

        # only perform topological sort if graph is acyclic
        if self.has_cycle():
            return

        q = Queue()                            # queue to hold vertices without parents
        adj_list = self.get_adj_list()         # get adjacency list from adjacency matrix
        num_parents = self.get_num_parents()   # get number of parents for each vertex (dict)

        for to_v, num in num_parents.items():  # for all vertices in graph,
            if num == 0:                       # if vertex does not have parents,
                q.enqueue(to_v)                # add vertex to queue.

        topo_order = []                        # list to hold topological order (of vertex labels)
        while not q.is_empty():                # while queue is not empty (i.e., haven't visited all vertices),
            from_v = q.dequeue()               # dequeue the current parent vertex
            label = self.Vertices[from_v].get_label()  # get label rather than index of vertex
            topo_order.append(label)           # append label to topo_order list

            children = adj_list[from_v]        # get list of children of the current parent vertex
            for to_v in children:              # for each child vertex,
                num_parents[to_v] -= 1         # decrement num_parents to simulate deleting parent from graph
                if num_parents[to_v] == 0:     # if the child no longer has parents,
                    q.enqueue(to_v)            # add child to queue

        return topo_order


def main():
    # create a Graph object
    theGraph = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices and insert them into the graph
    for i in range(num_vertices):
        line = sys.stdin.readline()
        vertex = line.strip()
        theGraph.add_vertex(vertex)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read the edges and insert them into the graph
    for i in range(num_edges):
        line = sys.stdin.readline()
        line = line.strip()
        edge = line.split()
        start = theGraph.get_index(edge[0])
        finish = theGraph.get_index(edge[1])

        theGraph.add_directed_edge(start, finish, 1)

    # test if a directed graph has a cycle
    if theGraph.has_cycle():
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # test topological sort
    if not theGraph.has_cycle():
        vertex_list = theGraph.toposort()
        print("\nList of vertices after toposort")
        print(vertex_list)


if __name__ == '__main__':
    main()
