# Work productivity & coffee intake

### Description
Chris has to complete a programming assignment overnight. He has to write `n` lines of code before morning.
He is dead tired, and he tries drinking some black coffee to keep him awake. 
Each time he drinks a cup of coffee, he stays awake for a short amount of time; however, his productivity goes down by a constant factor `k`.  

This is how he plans on finishing the program: 
- He will write the first `v` lines of code, then drink his first cup of coffee.
- Since his productivity has gone down by a factor of `k` he will write `v // k` lines of code.
- He will have another cup of coffee and then write `v // k**2` lines of code.
- He will have another cup of coffee and write `v // k**3` lines of code and so on.
- He will collapse and fall asleep when `v // k ** p` becomes `0`.

Chris **does** want to complete his assignment and maximize his sleep, so he wants to figure out
the **minimum allowable value** of `v` for a given productivity factor `k` that will allow him to write **at least n lines of code** before he falls asleep. 


### Input:
Read your input from standard input as given in the following format file `work.in`:
``` 
2        # num of test cases
300 2    # n k
59 9     # n k
```

The first line is `T`, the number of test cases. 
This will be followed by T lines of input. 
Each line of input will have two numbers: n and k. 
- `n` is the number of lines of code to write (1 ≤ n ≤ 1,000,000)
- `k` is the productivity factor (2 ≤ k ≤ 10)

### Output:
For each test case, write your result to standard out as shown in file `work.out`. 
In your output, there will be `v` lines of code that Chris has to write, as well as the time it took for each function. 

For the above two test cases, the output will be:

``` 
Binary Search: 152
Time: 9.512901306152344e-05

Linear Search: 152
Time: 0.0005910396575927734


Binary Search: 54
Time: 4.696846008300781e-05

Linear Search: 54
Time: 9.012222290039062e-05
```


### Implementation
1. First, write a function that uses a **linear search** to solve the problem. 
2. Then, write a function that uses a modified binary search algorithm to solve it again.  

- Both functions will return the same answer, but the binary search method will usually be faster.
- It is recommended that you write a helper function:
  - Given a value `v` representing the number of lines Chris writes before his first cup of coffee
  - Given a value `k`, the productivity factor
  - Calculate the `n`, the number of lines Chris will write before falling asleep. 
  - This can be called in both the linear and binary functions to make the computations easier.