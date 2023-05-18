#  File: GraphFill.py
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020
#  Date Created: 04/03/2023
#  Date Last Modified: 04/03/2023

import os
import sys

# ----------------------- PRINTING LOGIC ----------------------------

# enables printing colors on Windows
os.system("")

# code to reset the terminal color
RESET_CHAR = "\u001b[0m"
# color codes for the terminal
COLOR_DICT = {
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m"
}
# character code for a block
BLOCK_CHAR = "\u2588"


# Input: text is some string we want to write in a specific color,
#        color is the name of a color that is looked up in COLOR_DICT
# Output: returns the string wrapped with the color code
def colored(text, color):
    color = color.strip().lower()
    if color not in COLOR_DICT:
        raise Exception(color + " is not a valid color!")
    return COLOR_DICT[color] + text


# Input: color is the name of a color that is looked up in COLOR_DICT
# prints a block (two characters) in the specified color
def print_block(color):
    print(colored(BLOCK_CHAR, color) * 2, end='')


# ------------------------------------------------------------

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

    # checks the item at the top of the Queue
    def peek(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


# class for a graph node; contains x and y coordinates, a color, a list of edges and
# a flag signaling if the node has been visited (useful for search algorithms)
# it also contains a "previous color" attribute. This might be useful for your flood fill implementation.
class ColorNode:
    # Input: x, y are the location of this pixel in the image
    #   color is the name of a color
    def __init__(self, index, x, y, color):
        self.index = index
        self.color = color
        self.prev_color = color
        self.x = x
        self.y = y
        self.edges = []
        self.visited = False

    # Input: node_index is the index of the node we want to create an edge to in the node list
    # adds an edge and sorts the list of edges
    def add_edge(self, node_index):
        self.edges.append(node_index)

    # Input: color is the name of the color the node should be colored in;
    # the function also saves the previous color (might be useful for your flood fill implementation)
    def visit_and_set_color(self, color):
        self.visited = True
        self.prev_color = self.color
        self.color = color

        print("Visited node " + str(self.index))


# class that contains the graph
class ImageGraph:
    def __init__(self, image_size):
        self.nodes = []
        self.image_size = image_size

    # prints the image formed by the nodes on the command line
    def print_image(self):
        img = [["black" for i in range(self.image_size)] for j in range(self.image_size)]

        # fill img array
        for node in self.nodes:
            img[node.y][node.x] = node.color

        for line in img:
            for pixel in line:
                print_block(pixel)
            print()
        # print new line/reset color
        print(RESET_CHAR)

    # sets the visited flag to False for all nodes
    def reset_visited(self):
        for i in range(len(self.nodes)):
            self.nodes[i].visited = False

    # Construct adjacency matrix: --------------------------------------------------------------------------------------
    def get_adjacency_matrix(self):
        num_nodes = len(self.nodes)
        adj = [[0 for j in range(num_nodes)] for i in range(num_nodes)]  # initialize n x n matrix with 0's

        # Construct adjacency matrix:
        for from_node in self.nodes:               # for each from node
            for to_node in from_node.edges:        # for each to node
                adj[from_node.index][to_node] = 1  # change 0 to 1, since an edge exists.

        return adj

    # Print adjacency matrix: ------------------------------------------------------------------------------------------
    def print_adjacency_matrix(self):
        num_nodes = len(self.nodes)
        adj = self.get_adjacency_matrix()

        print("Adjacency matrix:")
        for i in range(num_nodes):
            for j in range(num_nodes):
                print(adj[i][j], end='')
            print()  # start new line each row
        print()  # empty line afterwards

    # Return the index of a node, given its x and y coordinates --------------------------------------------------------
    def get_index(self, x, y):
        # Given an x and y position in adjacency matrix, return the index of node in self.nodes.
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node.index

    # Breadth-first search: --------------------------------------------------------------------------------------------
    # Input: `graph`       is the graph containing the nodes
    #        `start_index` is the index of the currently visited node
    #        `color`       is the color to fill the area containing the current node with
    def bfs(self, start_index, color):

        self.reset_visited()                   # reset visited status
        print("Starting BFS; initial state:")  # print initial state
        self.print_image()

        visited_nodes = set()              # keep track of node indexes that have been visited
        px = self.nodes[start_index]       # convert start_index to node object called px (pixel)
        q = Queue()                        # FIFO
        q.enqueue((px.index, px.x, px.y))  # enqueue the starting pixel to bucket fill
        matching_color = px.color          # pixels to be filled with new color must match start pixel's old color

        # bfs bucket fill algorithm:
        while not q.is_empty():            # while queue is not empty
            next, _, _ = q.peek()          # peek index of the next pixel
            if next in visited_nodes:      # if next has already been visited
                q.dequeue()                # remove pixel from queue
                continue                   # restart while loop

            i, x, y = q.dequeue()          # dequeue current pixel (index, x-coord, y-coord)
            visited_nodes.add(i)           # add current index to visited_nodes
            px = self.nodes[i]             # convert to node object called px (pixel)
            px.visit_and_set_color(color)  # mark pixel as visited, change to new color
            self.print_image()             # print updated image

            # create indexes of l, r, u, d pixels in relation to current pixel:
            left = self.get_index(x - 1, y)
            right = self.get_index(x + 1, y)
            up = self.get_index(x, y - 1)
            down = self.get_index(x, y + 1)

            neighbors = [left, right, up, down]  # list that will be iterated through
            neighbors = [x for x in neighbors if x is not None]  # remove non-existent indexes
            for index in neighbors:              # for each existing neighboring pixel,
                neighbor_px = self.nodes[index]  # convert to node object called neighbor_px

                # if neighbor color is the old color and the neighbor hasn't been visited,
                if neighbor_px.color == matching_color and neighbor_px.index not in visited_nodes:
                    # then enqueue the neighbor pixel (index, x-coord, y-coord)
                    q.enqueue((neighbor_px.index, neighbor_px.x, neighbor_px.y))

    # Depth-first search: ----------------------------------------------------------------------------------------------
    # Input: graph       is the graph containing the nodes
    #        start_index is the index of the currently visited node
    #        color       is the color to fill the area containing the current node with
    def dfs(self, start_index, color):

        self.reset_visited()  # reset visited status
        print("Starting DFS; initial state:")  # print initial state
        self.print_image()

        visited_nodes = set()           # keep track of node indexes that have been visited
        px = self.nodes[start_index]    # convert start_index to node object called px (pixel)
        s = Stack()  # LIFO
        s.push((px.index, px.x, px.y))  # push the starting pixel to bucket fill
        matching_color = px.color       # pixels to be filled with new color must match start pixel's old color

        # dfs bucket fill algorithm:
        while not s.is_empty():
            next, _, _ = s.peek()       # peek index of the next pixel
            if next in visited_nodes:   # if next has already been visited
                s.pop()                 # remove pixel from stack
                continue                # restart while loop

            i, x, y = s.pop()           # pop current pixel (index, x-coord, y-coord)
            visited_nodes.add(i)        # add current index to visited_nodes
            px = self.nodes[i]          # convert to node object called px (pixel)
            px.visit_and_set_color(color)  # mark pixel as visited, change to new color
            self.print_image()          # print updated image

            # create indexes of l, r, u, d pixels in relation to current pixel:
            left = self.get_index(x - 1, y)
            right = self.get_index(x + 1, y)
            up = self.get_index(x, y - 1)
            down = self.get_index(x, y + 1)

            neighbors = [left, right, up, down]  # list that will be iterated through
            neighbors = [x for x in neighbors if x is not None]  # remove non-existent indexes
            for index in neighbors:              # for each existing neighboring pixel,
                neighbor_px = self.nodes[index]  # convert to node object called neighbor_px

                # if neighbor color is the old color and the neighbor hasn't been visited,
                if neighbor_px.color == matching_color and neighbor_px.index not in visited_nodes:
                    # then push the neighbor pixel (index, x-coord, y-coord)
                    s.push((neighbor_px.index, neighbor_px.x, neighbor_px.y))


# Create graph, connections structured as adjacency list: --------------------------------------------------------------
def create_graph(data):
    # creates graph from read in data
    data_list = data.split("\n")

    # get size of image, number of nodes
    image_size = int(data_list[0])
    node_count = int(data_list[1])

    graph = ImageGraph(image_size)

    index = 2

    # create nodes
    for i in range(node_count):
        # node info has the format "x,y,color"
        node_info = data_list[index].split(",")
        new_node = ColorNode(len(graph.nodes), int(node_info[0]), int(node_info[1]), node_info[2])
        graph.nodes.append(new_node)
        index += 1

    # read edge count
    edge_count = int(data_list[index])
    index += 1

    # create edges between nodes
    for i in range(edge_count):
        # edge info has the format "fromIndex,toIndex"
        edge_info = data_list[index].split(",")
        # connect node 1 to node 2 and the other way around
        graph.nodes[int(edge_info[0])].add_edge(int(edge_info[1]))
        graph.nodes[int(edge_info[1])].add_edge(int(edge_info[0]))
        index += 1

    # read search info
    search_info = data_list[index].split(",")
    search_start = int(search_info[0])
    search_color = search_info[1]

    return graph, search_start, search_color


# Print from_node, x, y, to_node: --------------------------------------------------------------------------------------
def print_node_info(node_list):
    print(f'i x y edges')
    for node in node_list:
        print(node.index, node.x, node.y, node.edges)


def main():
    # read input
    data = sys.stdin.read()

    graph, search_start, search_color = create_graph(data)

    # print matrix
    graph.print_adjacency_matrix()

    # run bfs
    graph.bfs(search_start, search_color)

    # reset by creating graph again
    graph, search_start, search_color = create_graph(data)

    # run dfs
    graph.dfs(search_start, search_color)


if __name__ == "__main__":
    main()
