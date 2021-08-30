import operator
import argparse
import sys

def reverse_polish_notation_calc():
    operators = { "+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv,
          }
    stack = []
    continue_expr = True

    while continue_expr:
        cmd_line_expr = input('Input: ').lstrip(' ')

        new_calc_exit_calc(cmd_line_expr)
 
        for num in cmd_line_expr.split():
            rpn_algo(num, stack, operators)
        print(stack[-1])

def new_calc_exit_calc(expr):
    if expr == 'q':
        print('Exit')
        sys.exit()
    elif expr == 'n':
        print('New Calculation')
        continue_expr = False
        return continue_expr, reverse_polish_notation_calc()

def rpn_algo(expr, stack, operators):
    if not_num_or_operator(expr, operators):
        print('Cannot add letters')
    elif expr.isdigit():
        stack.append(int(expr))
    elif expr.replace('.', '', 1).isdigit():
        stack.append(float(expr))
    elif expr in operators:
        if len(stack) <= 1:
            print("Need at least 2 values before using operator")
        else:
            expr_operator = expr
            first_val = stack.pop()
            second_val = stack.pop()
            result = operators[f'{expr_operator}'](second_val, first_val)
            stack.append(result)

def not_num_or_operator(expr, operators):
    return expr.isalpha() and expr not in operators


def main():
    parser = argparse.ArgumentParser(description='Performs calculations using Reverse Polish Notation')
    parser.add_argument(dest='rpncalc', action='store_true', help='Enter an expression to calculate')
    reverse_polish_notation_calc()

if __name__ == '__main__':
    main()
