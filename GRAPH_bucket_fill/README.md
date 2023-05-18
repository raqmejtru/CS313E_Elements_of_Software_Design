# Graph Bucket Fill

## Overview
Task is to:
1. print the adjacency matrix for a graph 
2. implement Breadth-First Search and Depth-First Search to flood fill pixels in images.  

This is also known as "bucket fill" in graphics applications. 
It allows you to select a pixel in an image and fill the selected pixel and all connected pixels of 
the same color with a new color, thereby allowing you to change the color of a large area of an image.  

Implement this feature using Breadth-First Search and Depth-First Search algorithms. 
- treat each pixel of an input image as a node in a graph. 
- start at a given node/pixel and explore the graph from there, changing the color of each pixel as it is visited.

The script reads in a file containing:
- nodes: consist of an x-coordinate, y-coordinate, and a color
- edges between the nodes to build a graph. 
- The code also provides the function `ImageGraph.print_image()` to display the graph of ColorNodes as an image in the console.


# Tasks
1. Print the adjacency matrix of the graph.
2. Complete the Breadth-First Search function of the Graph class.
3. Complete the Depth-First Search function of the Graph class.

#### Rules for the search algorithms
- Only visit nodes that have the same color as the starting node.
- Color visited nodes in the new color.
- Call the `ImageGraph.print_image()` function after coloring a pixel.

Apart from the `ImageGraph` and `ColorNode` classes, you will also find a `Stack` and a `Queue` class. USe these for search algorithm implementations.


## Input
Read input data from the provided `*.in` files. The format of the files will be as follows:
```  
5            # image width and height (square)
5            # number of lines that follow that describe nodes
1, 1, red    # x, y, color
2, 1, red
3, 1, red
2, 2, red
3, 2, red
5            # number of lines that follow that describe edges
0, 1         # from node, to node
1, 2
1, 3
2, 4
3, 4
2, green     # node to start search, color to use for flood fill.
```

1. The first line will be the dimension of the image (width and height). 
   - This number is used to initialize the ImageGraph. 
2. The second line is the number of lines following afterwards describing the nodes. 
   - Each node description has the format x,y,color.
3. After the nodes, there’s another line with a single number telling you how many edge descriptions follow.
   - Each edge description has the format from node index,to node index.
   - The code template connects from node to to node and to node to from node.
4. Finally, there’s a line telling you which node index to start the BFS and DFS algorithms on and which color
   to use for the flood fill.

## Output
There are three parts to the output:
1. The adjacency matrix
   - The adjacency matrix has a `1` at position x,y if there is an edge connecting the node at position x in
the ImageGraph.nodes list and the node at position y in the list; otherwise it is `0` in this position. There are
no spaces or other delimiters between the numbers.
2. The intermediate images produced by the BFS algorithm
3. The intermediate images produced by the DFS algorithm

##### Adjacency matrix

Make sure to call ImageGraph.print image() after each pixel that you color and don’t remove the empty print()
statements that add new lines from the function/add more new lines to the output.
