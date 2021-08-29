import operator
import argparse
import sys
import pylint.lint

pylint_opts = ['basics.py','--load-plugins=pylint.extensions.mccabe','--rcfile=~/.pylintrc']

pylint.lint.Run(pylint_opts)

def new_calc_exit_calc(expr):
    '''
    will either exit or create a new calculation with an exmpty stack
    '''
    if expr == 'q':
        print('Exit')
        sys.exit()
    elif expr == 'n':
        print('New Calculation')
        continue_expr = False
        return continue_expr, new_calc_exit_calc()

def calc_more_than_one_expr(expr, stack, operators, ops):
    '''
    for calculating an argument with more than one expression ex: 4 3 2 + +
    '''
    for num in expr.split():
        if num.isalpha() and num not in operators:
            print('Cannot add letters')
        elif num in operators and len(stack) < 2:
            print("Need at least 2 values before calculating")
            break
        else:
            if num.isdigit():
                stack.append(int(num))
            elif num not in operators:
                stack.append(float(num))
            elif num in operators:
                expr_operator = num
                first_val = stack.pop()
                second_val = stack.pop()
                result = ops[f'{expr_operator}'](second_val, first_val)
                stack.append(result)
    print(stack[-1])


def reverse_polish_notation_calc():
    '''
    calculates using postfix notation
    '''
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

        if len(cmd_line_expr) > 1:
            calc_more_than_one_expr(cmd_line_expr, stack, operators, ops)
        else:
            if cmd_line_expr.isalpha() and cmd_line_expr not in operators:
                print('Cannot add letters')
                continue

            if cmd_line_expr in operators and len(stack) >= 2:
                expr_operator = cmd_line_expr
                first_val = stack.pop()
                second_val = stack.pop()
                result = ops[f'{expr_operator}'](second_val, first_val)
                stack.append(result)
                print(result)
            elif cmd_line_expr in operators and len(stack) < 2:
                print('Result of last expression: ',f"{stack[-1]}")
                continue
            elif cmd_line_expr.isdigit():
                print(cmd_line_expr)
                stack.append(int(cmd_line_expr))
            else:
                print(cmd_line_expr)
                stack.append(float(cmd_line_expr))
reverse_polish_notation_calc()

def main():
    parser = argparse.ArgumentParser(description='Performs calculations using Reverse Polish Notation')
    parser.add_argument(dest='rpncalc', action='store_true', help='Enter an expression to calculate')

if __name__ == '__main__':
    main()
