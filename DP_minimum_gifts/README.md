# Reward

ABC's online shopping site has a special reward program for Christmas. 
When the customer spends `T` dollars online, ABC will mail gifts worth `10%` of the `T` dollars 
(**round to integers**). Customers may receive the same types of gifts. 
All kinds of gifts in the warehouse are of a similar size and have enough numbers (supply). 
Each gift has to be packed in a unique box.  
To save the packaging time, ABC staff decides to find the **minimum number** of gifts for each customer.  


### Input
There are two lines of inputs.  
1. The first line is a list of the price for each type of gift (integer). 
2. The second line is an integer T that a customer spends.

Example:
``` 
1 3 4
50
```

### Output
The output is an integer for the minimum number of chosen gifts.  
Return -1 if the staff cannot find the gifts that are worthy of the reward program.

Example:
``` 
2
```


### Explanation:
10% of 50 dollars is 5, which can be made up with a **minimum of two** gifts worth $1 and $4.
