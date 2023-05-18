# Fully Automatic Beverage Vending Machine  

Implement the controller software of this machine.
The software should be able to control the brewing process of fresh coffee and tea beverages.

## Overview
The machine should be able to:
- Brew Coffee sorts of Espresso, Americano, Latte Macchiato
- Make Tea sorts of Black Tea, Green Tea, and Yellow Tea
- Add condiments like milk and sugar to the hot beverage

## Requirements
1. When the machine starts up and is initiated, it shows a request question and asks users about their beverage wishes.
2. After each brewing process, the state of the beverage machine should return to the same initial state and display the request question to ask users again.
3. As an additional requirement, the coffee machine should be able to add condiments like milk and sugar to the hot beverage. 
   - Users of this machine should be able to select between 0 to 3 units of milk or sugar to add.
   - The vending machine should only allow up to 3 units of condiments. 

## Implementation Details
1. Define parent class `Beverage`
  - attributes `price`, `caffeine`, `calories`
  - Create `__str__(self)` method:
    - prints the name of the drink, calories, and price.
2. Child class `Latte(Beverage)` has attribute `lactose`
3. Child class `Tea(Beverage)` has attribute `color`
4. Define parent class `Condiments`
   - attributes `milk` and `sugar`
5. Define organizational class `UserInterface` for the vending machine's main controller function that runs up the user interface and communicates with the user. 
6. Define the `main` function that gets the input from the user and prints it out to the standard output.  
