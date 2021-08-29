import operator
import argparse
import sys
# import pylint.lint

# pylint_opts = ['basics.py','--load-plugins=pylint.extensions.mccabe','--rcfile=~/.pylintrc']

# pylint.lint.Run(pylint_opts)

def new_calc_exit_calc(expr):
    if expr == 'q':
        print('Exit')
        sys.exit()
    elif expr == 'n':
        print('New Calculation')
        continue_expr = False
        return continue_expr, reverse_polish_notation_calc()

def rpn_algo(expr, operators, stack, ops):
    if not_num_or_operator(expr, operators):
        print('Cannot add letters')
    elif expr.isdigit():
        stack.append(int(expr))
    elif expr not in operators:
        stack.append(float(expr))
    elif expr in operators:
        if len(stack) <= 1:
            print("Need at least 2 values before using operator")
        else:
            expr_operator = expr
            first_val = stack.pop()
            second_val = stack.pop()
            result = ops[f'{expr_operator}'](second_val, first_val)
            stack.append(result)
            print(result)

def calc_one_or_more_expr(expr, stack, operators, ops):
    for num in expr.split():
        rpn_algo(num, operators, stack, ops)

def not_num_or_operator(expr, operators):
    return expr.isalpha() and expr not in operators

def reverse_polish_notation_calc():
    ops = { "+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv,
          }
    operators = '+-*/'
    stack = []
    continue_expr = True

    while continue_expr:
        cmd_line_expr = input('Input: ').lstrip(' ')

        new_calc_exit_calc(cmd_line_expr)
        if cmd_line_expr not in operators:
            print(cmd_line_expr)
        calc_one_or_more_expr(cmd_line_expr, stack, operators, ops)

reverse_polish_notation_calc()

def main():
    parser = argparse.ArgumentParser(description='Performs calculations using Reverse Polish Notation')
    parser.add_argument(dest='rpncalc', action='store_true', help='Enter an expression to calculate')

if __name__ == '__main__':
    main()
