# Expression Tree

### Description

Read the file `expression.in` from stdin and create an expression tree. 
The expression will be a valid infix expression with the all the necessary parentheses so that there 
is no ambiguity in the order of the expression. 
Evaluate the expression and print the result. 
Write the prefix and postfix versions of the same expression without any parentheses.

In an expression tree the nodes are either 1) operators or 2) operands.
1. The operators will be in the set [`+`, `-`, `*`, `/`, `//`, `%`, `**`].
   - All the operator nodes will have exactly two children.
2. The operands will be either integers or floating point numbers.
   - All the operand nodes will be leaves of the expression tree.


The function `create_tree()` will:
1. Take an infix expression with parentheses as a `str` as an input parameter
   - Assume that the expression string is valid and there are **spaces between** the operators, operands, and the parentheses.
2. Create an Expression Tree using the infix expression

Take the expression string and break it into four types of tokens. 
- left parenthesis: _starting a new expression_
- right parenthesis: _ending an expression_
- operator
- operand

### Algorithm
1. Start with an `empty node` that will be the `root` node. 
   - Call it the `current` node. 
2. Then start parsing the expression:  
   - If the current token is a left parenthesis:
     - Add a new node as the left child of the current node. 
     - Push current node on the stack 
     - Make the current node equal to the left child.
   - If the current token is an operator:
     - Set the current node's data value to the operator. 
     - Push current node on the stack. 
     - Add a new node as the right child of the current node 
     - Make the current node equal to the right child.
   - If the current token is an operand:
     - Set the current node's data value to the operand 
     - Make the current node equal to the parent by popping the stack.
   - If the current token is a right parenthesis:
     - Make the current node equal to the parent node by popping the stack (if it is not empty).


### Input:
``` 
( ( 8 + 3 ) * ( 7 - 2 ) )
```

### Output:
``` 
( ( 8 + 3 ) * ( 7 - 2 ) ) = 55.0

Prefix Expression: * + 8 3 - 7 2

Postfix Expression: 8 3 + 7 2 - *
```

### References
Binary Expression Tree https://en.wikipedia.org/wiki/Binary_expression_tree
