# Tree Balance Factor

Given a binary tree rooted at node n, determine its balance factor.  
In other words, determine the **difference in heights between its two subtrees**.

If the right subtree height is given by `r` and the left subtree height by `l`, the balance factor would be `r - l`.

### Example-1

Suppose you are given a node n which is captured by the tree shown by the below diagram.
```
                    25

            -5            32

       9                 

         25                        
```
 

- Input-1: `Node(25)`
- Output-1: `-2`
 

### Example-2

Suppose you are given a node n which is captured by the tree shown by the below diagram.
``` 
                    1

            1              1   
```

- Input-2: `Node(1)`
- Output-2: `0`