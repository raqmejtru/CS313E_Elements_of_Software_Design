# Adjacency Matrix

Suppose you are given a **weighted directed graph** provided as an **edge list**, 
where each element of the list contains the string node label of the source node, 
followed by the string node label of the destination node, followed by the integer weight of the edge.  

Generate an adjacency matrix representing the equivalent graph, where the rows/columns are ordered 
in ascending order of the labels.

### Example-1

Sample Input-1:
``` 
[['A', 'D', 3], ['D', 'A', -5], ['F', 'A', 16], ['Z', 'F', 3], ['A', 'Z', 12]]
```

Output-1:
``` 
0   3  0  12
-5  0  0  0
16  0  0  0
0   0  3  0
```


### Example-2

Sample Input-2: 
``` 
[['4', '6", 3], ['4', '5', 2], ['5', '6', 9]]
```

Output-2:
``` 
0 2 3
0 0 9
0 0 0
```
