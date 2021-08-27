# Reverse Polish Notation Calculator

## Introduction

A python program that calculates expressions using postfix notation also known as reverse polish notation. Expressions are calculated following 2 operands and then an operator (+ - * /)

## How It Works

This program takes in a string argument that can either be numerical or mathematical operation. Numbers (either whole or floating point) are added to a stack and when 2 or more numbers are in a stack, an operation can be executed or more numerical values can be added. To do this, if the next input argument is an operator, and there are at least two numbers in the stack, `stack.pop()` occurs on the last two numbers in the stack and are assigned to their own values which are then executed by the operator. After a calculation occurs, the result gets added to the stack. The calculator can continue to take in new arguments, start a new calculation with an `n` argument, or exit the program with `q`.

Adding one argument will return the value to be calculated. When the argument is an operator, a calculation will occur:
    > 5 
    > returns 5
    > 8
    > returns 8
    > +
    > will add 5 and 8 to return 13

The program can also take an argument with several numbers or operators:
    > 5 5 5 8 + + -
    > returns -13.0
    > 13 +
    > returns 0.0
