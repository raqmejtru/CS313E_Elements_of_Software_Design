# Spiral

### Description
Consider the natural numbers laid out in a square spiral, with 1 occupying the center of the spiral. The
central 11 x 11 subset of that spiral is shown below.
``` 
111 112 113 114 115 116 117 118 119 120 121
110 73  74  75  76  77  78  79  80  81  82
109 72  43  44  45  46  47  48  49  50  83
108 71  42  21  22  23  24  25  26  51  84
107 70  41  20  7   8   9   10  27  52  85
106 69  40  19  6   1   2   11  28  53  86
105 68  39  18  5   4   3   12  29  54  87
104 67  38  17  16  15  14  13  30  55  88
103 66  37  36  35  34  33  32  31  56  89
102 65  64  63  62  61  60  59  58  57  90
101 100 99  98  97  96  95  94  93  92  91
```

This spiral has several interesting features. 
- The southeast diagonal has several prime numbers (3, 13, 31, 57, and 91) along it. 
- The southwest diagonal has a weaker concentration of prime numbers (5, 17, 37) along it.  

**Spiral Construction**  
To construct the spiral we start with 1 at the center, with 2 to the right, and 3 below it, 4 to the left, and
so on. Part of the task is to figure out how to fill a spiral of arbitrary size.
Once you construct the spiral, you can complete the rest of the tasks described below.  

### Input
You will read your input data from a file called `spiral.in`. The format of the input file will be as follows:
``` 
11   # dimension of the spiral
1    
42
110
91
```

- The first line will be the dimension of the spiral. 
   - It will always be odd and greater than 1 and less than 100. 
- This will be followed by an arbitrary number of lines. There will be a single number on each line.
  - These numbers will be numbers inside the spiral. 
  - Some of these numbers will be interior numbers, others will be numbers on the edge, and yet others will be numbers 
  at the corners of the spirals. 
- Assume that the input file used to test your program will be valid.

### Output:
For each of the numbers inside the spiral, your output will be the 
**sum of all adjacent numbers to this number, not including this number**. 
For the above input file you will output to the console:
``` 
44
382
477
239
```
