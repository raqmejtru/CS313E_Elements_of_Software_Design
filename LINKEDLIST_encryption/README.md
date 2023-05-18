# Generate New Password

John would like to generate a new password based on some modifications of his original password. 
He decided to rotate his original password sequentially based on some specifications. 

1. First, he chooses a singly linked list as the data structure to represent his original password. 
2. Second, he defines a variable called `r_step` to determine how many steps he would like the singly 
linked list to rotate to the left (counter-clockwise) each time. 
3. Third, he also designs a variable called `times` to represent the number of times he wants to 
rotate the singly linked list. 


### Input format:
First line: a line of space-separated nonzero integers representing a linked list (your original password)
Second line: a line of space-separated nonzero integers representing ``r_step’’ and ``times’’, respectively

``` 
6 7 8 9 10
2 2
```

### Output format:  
1. First line:
   - Print the original password
   - The output string represents the original password; the input linked list (the __str__() function; this function has also been provided for you in the template).
2. Second line:
 - The string represents the new rotated linked list (His new password)

``` 
6  7  8  9  10
10  6  7  8  9
```


 

### Explanation:

- The 1st rotation is to rotate the list to the left (counter-clockwise) for 2 steps  (``r_step’’). 
  - John gets  "8  9  10  6  7".   
- The second rotation would yield "10  6  7  8  9".

