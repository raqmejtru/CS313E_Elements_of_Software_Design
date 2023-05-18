# String Anagram Families

Given a list of words `lst`, return the **number of anagram families** of the elements in lst.

### Description
- An anagram of word w is a word formed by using **each of the letters** in word w **exactly once**. 
  - For example, 'ate' is an anagram of 'eat', but would not be an anagram of 'tear'. 
- Any word is an anagram of itself. 
- An anagram family is a list of strings that are all anagrams of each other.

### Input
- The first line of input will be an integer `n`, the number of words in `lst`. 
- The next `n lines` will each contain a single word w which is a word in `lst`. 
- 1 <= n <= 30 and each word will consist of **lowercase letters only**.

**Example Input:**
```
7
ate
bat
cat
eat
rat
tab
tea
```

### Output
- Output a single integer that is the **number of anagram families** formed by `lst`.

**Example Output:**
```
4
```


### Anagram family example
The anagram families in the example input would be: 
```
cat
rat
bat, tab
ate, eat, tea
```
