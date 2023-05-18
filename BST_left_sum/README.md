# Left Sum of BST

Imagine you are looking at the left side of a binary search tree.  
The left-side-view nodes are nodes that are of the left-most node at each level.  
Return the sum of all the left-side-view nodes.

### Input
A sequence of integers representing the BST, for example:
``` 
15 10 20 9 30
```

### Output
An integer that represents the sum of the left-side-view nodes of the BST, for example:
``` 
34
```


### Explanation:
Visualization of example input tree:
``` 
           15 

       10     20

   9               30
```

The left-most nodes at each level are `15`, `10`, and `9`.  
Therefore, the sum of these nodes are `15+10+9 = 34`.