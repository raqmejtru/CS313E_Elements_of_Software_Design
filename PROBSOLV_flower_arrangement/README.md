# Flower Arrangement

Jennifer loves making flower arrangements in her free time. 
One day, she bought a blanket of different types of flowers from the shops. 
She has `N` number of vases at home. 
Each flower has to be inserted into one of the vases. 
She wants to arrange the flower so that **no more than two flowers of the same type** 
will be inserted in the same vase. 
She wants to find out **which type of flower will be left after her arrangement**. 

### Input
Input is two lines. 
1. The first line is a list (flower_list) describing which flower types Jennifer has purchased, 
with possible types ranging from 1 through 9. There may be more than one of each type. 
   - For instance, if the input were "`1 1 2 2 2 3`", this would suggest that Jennifer has two 
   flowers of type 1, three flowers of type 2, and one flower of type 3. 
2. The second line is the N number of vases she has. 

### Output
Output is a list of integers representing the flower types left (that is, she bought too many). 

Please sort the output list based on the ascending order of the flower types (For example, `[2,3,6,9]`). 

Output empty list `[]` if no flower is left after the arrangement.


### Example
``` 
# Input
# She bought 7 flowers. There are five flowers of type 1, one flower of type 2, and one flower of type 3.
1 1 1 1 1 2 3 
# She has two vases.
2
``` 
``` 
# Output
[1]
# She bought too many type 1 flowers. 
# Because no matter how to arrange these flowers in two vases, 
# type 1 flower will be more than two flowers in a vase. 
# For example, {1,1,1} and {1,1,2,3} or {1,1} and {1,1,1,2,3}.
```
