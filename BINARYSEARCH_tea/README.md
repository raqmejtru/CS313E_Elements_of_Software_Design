# Tea Options


### Description
- Tim loves to try black tea from different shops each day. 
- He collects a `list` of `prices` of black tea **from each store**, and the prices remain the same for each day. 
- He allocates a given amount of money for black tea for each day (can be spent at different stores) on consecutive days. 

### Problem
Now, Tim wants to compute the **number of different shops** that he can order black tea from
in order to buy **one cup of black tea each day**. 

### `find_purchase_options(prices, money)`
Implement the "`find_purchase_options()`" function, given:
- `prices`: a list of integers that contains the price of black tea in **each** store 
- `money`: and a list of integers that includes the amount of money that Tim will spend in a given day (element) 

- Return a list of integers representing the **number of different shops** that 
Tim can select from to buy a cup of black tea for **each** given day.
  - i.e., `len(money) == len(output_list)`
 

**Example Input:**
```
prices = [3, 10, 8, 6, 11]
money = [1, 10, 3, 11, 12]
```

**Example Output:**
``` 
[0, 4, 1, 5, 5]
```

### Explanation:
On each day, the maximum number of different shops that Tim can choose to have a cup of black is  [0,4,1,5,5]
1. On the 1st day, Tim won't be able to buy a drink from any of the shops.
   - `(money[0] == 1)` < all in `prices`
   - `num_shops = 0`
2. On the 2nd day, Tim can buy a drink in shops 1, 2, 3, and 4.
   - `(money[1] == 10)` >= `prices[0]`, `prices[1]`, `prices[2]`, `prices[3]`
   - `num_shops = 4`
3. On the 3rd day, Tim can buy a drink only in shop number 1.
   - `(money[2] == 3)` >= `prices[0]`
   - `num_shops = 1`
4. On the 4th day, Tim can buy a drink in any shop, that is 5 different shops.
   - `(money[3] == 11)` >= all in `prices`
   - `num_shops = 5`
5. On the 5th day, Tim can also buy a drink in any shop, that is 5 different shops.
   - `(money[4] == 12)` >= all in `prices`
   - `num_shops = 5`

    
### Notes:
- There may be duplicates in both lists.
- The money list will become much larger than the prices list, which drastically increases
the number of times that you have to search `prices`
- **A linear search each time will not work.** 
  - So, try to come up with an efficient search algorithm 
  - (hint: binary search) 
- Also, you can modify the prices list.
