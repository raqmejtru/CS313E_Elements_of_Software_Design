# `IntegerInterval`: Object-Oriented Programming

Create the following `IntegerInterval` class.

## Built-in Methods
### 1. `__init__`
`IntegerInterval(beginning, end)` to instantiate the `Interval` object, where `beginning` and `end` are `integers`.

### 2. `__str__`
When printed out, the string should be of the format: 
`Beginning: {beginning}, End: {end}`

### 3. `__eq__`
When determining whether two `IntegerIntervals` are equal, check whether they have the same `beginning` times and the same `end` times.

## Additional Methods
### 4. `def length(self)`
- The length of an interval is given by the difference between its start and end time:
`end - beginning`

### `def overlap(self, other)`
- Method returns `true` if the two intervals overlap
- Given an interval A and B, they overlap if either: 
  1. `A == B`  
  2. `A.beginning` or `A.end` is in the range `(B.beginning, B.end)` exclusive  
  3. `B.beginning` or `B.end` is in the range `(A.beginning, A.end)` exclusive  
     - The exclusive implies that two different intervals that only touch at a boundary are not considered to overlap one another.  

### `def intersection(self, other)`
- Returns the total time in the intersection between two intervals
- Given an interval A and B:
  - If we know they overlap (if `overlap(self, other) returns true`),
    - Then, the intersection’s **start** is `max(A.beginning, B.beginning)` 
    - And the intersection's **end** is **min(A.end, B.end)**
    - Therefore, the intersection time is the length of this intersection interval. 
  - If they don’t overlap, the intersection time is 0.

### `def union(self, other)`
- The total time in the union between the two intervals
- Given an interval A and B, the union between the two is:
  - `length of A + length of B - intersection(A, B)`
