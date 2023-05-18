#  File: Adjacency.py
#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Raquel Mejia-Trujillo
#  Course Name: CS 313E
#  Unique Number: 52020

import ast


def edge_to_adjacency(edge_list):
    adj_dict = dict()
    to_nodes_set = set()

    # Convert input into dictionary, where key = from_node, val = [(to_node, weight), ...]
    for edge in edge_list:
        from_node = edge.pop(0)
        to_node = edge.pop(0)
        to_nodes_set.add(to_node)
        weight = edge.pop(0)
        try:
            adj_dict[from_node].append((to_node, weight))
        except KeyError:
            adj_dict[from_node] = [(to_node, weight)]

    # Double check that all to_nodes are included as keys in dict:
    for to_node in to_nodes_set:
        if to_node not in adj_dict.keys():
            adj_dict[to_node] = []

    # Initialize n x n matrix with 0's
    num_nodes = len(adj_dict)
    adj = [[0 for col in range(num_nodes)] for row in range(num_nodes)]

    # Construct adjacency matrix:
    adj_dict = dict(sorted(adj_dict.items()))                  # Sort in increasing order of keys
    for from_node, edges in adj_dict.items():                  # For each from_node,
        for edge_tuple in edges:                               # For each to_node, weight tuple in the from_node,
            to_node, weight = edge_tuple
            from_idx = list(adj_dict.keys()).index(from_node)  # Get the index of the from_node
            to_idx = list(adj_dict.keys()).index(to_node)      # Get the index of the to_node
            adj[from_idx][to_idx] = weight                     # Assign weight to correct location

    # Return adjacency matrix
    return adj


def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))


if __name__ == "__main__":
    main()
