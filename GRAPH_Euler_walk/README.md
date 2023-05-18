# Mountain Hiking

Mary is a photographer. She decided to take pictures of all the trails in the well-known 
mountains on Saturday. The unique part of the mountain is that there are several garden hotels. 
Each garden hotel connects with some other garden hotels with trails. Mary estimates she can walk 
through each trail to take pictures exactly once in one day.   
To make sure she has enough energy for hiking and enjoys services from different garden hotels, 
she wants to book two hotels. Mary will live in the first hotel on Friday night so that she can 
get up early and start hiking. She wants to visit all trails exactly once, and then at night, 
she wants to stay in another hotel.
Is it possible for her to find two different hotels so that she can travel to each trail exactly once?   
Return a boolean.


### Input
* The input is an adjacency matrix representing an undirected graph.  
* Each vertex represents a hotel. 
* The edge represents a trail between two hotels.

Example:
``` 
0 0 1 0 1
0 0 1 1 0
1 1 0 1 0
0 1 1 0 0
1 0 0 0 0
```
    
### Output: `Boolean`
`True` means Mary can find the two different 
hotels so that she can travel to each trial exactly once; `False` otherwise.

Example:
``` 
True
```
 

### Explanation
To help better understand this problem, we label the vertices (hotels) as `a`, `b`, `c`, `d`, `e`:
``` 
   a b c d e
a 0 0 1 0 1
b 0 0 1 1 0
c 1 1 0 1 0
d 0 1 1 0 0
e 1 0 0 0 0  
```

Then we have an undirected edges: 
``` 
a-c, a-e
b-c, b-d, 
c-d
```

And we can have a path: `e – a – c - b - d - c`

She can therefore stay at hotel `e` the first night, and 
hotel `c` the second night, while being able to visit all trails (`True`). 
