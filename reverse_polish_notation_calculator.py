import operator
import argparse
import sys

def continue_or_exit_calc(expr):
    if expr == 'q':
        print('Exit')
        sys.exit()
    elif expr == 'n':
        print('New Calculation')
        continue_expr = False
        return continue_expr, calc()

def calc():
    ops = { "+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv,
          }
    operators = '+-*/'
    stack = []
    continue_expr = True

    while continue_expr:
        cmdLineExpr = input('Input: ')

        continue_or_exit_calc(cmdLineExpr)

        if len(cmdLineExpr) > 1:
            for num in cmdLineExpr.split():
                if num.isalpha() and num not in operators:
                    print('Cannot add letters')
                    continue
                elif num in operators and len(stack) < 2:
                    print("Need at least 2 values before calculating")
                    break
                else:
                    if num.isdigit():
                        stack.append(int(num))
                    elif num not in operators:
                        stack.append(float(num))
                    elif num in operators:
                        exprOperator = num
                        firstVal = stack.pop()
                        secVal = stack.pop()
                        result = ops[f'{exprOperator}'](secVal, firstVal)
                        stack.append(result)
            print(stack[-1])
        else:
            if cmdLineExpr.isalpha() and cmdLineExpr not in operators:
                print('Cannot add letters')
                continue

            if cmdLineExpr in operators and len(stack) >= 2:
                exprOperator = cmdLineExpr
                firstVal = stack.pop()
                secVal = stack.pop()
                result = ops[f'{exprOperator}'](secVal, firstVal)
                stack.append(result)
                print(result)
            elif cmdLineExpr in operators and len(stack) < 2:
                print('Result of last expression: ',f"{stack[-1]}")
                continue
            elif cmdLineExpr.isdigit():
                print(cmdLineExpr)
                stack.append(int(cmdLineExpr))
            else:
                print(cmdLineExpr)
                stack.append(float(cmdLineExpr))
calc()

def Main():
    parser = argparse.ArgumentParser(description='Performs calculations using Reverse Polish Notation')
    parser.add_argument(dest='rpncalc', action='store_true', help='Enter an expression to calculate')

if __name__ == '__main__':
    Main()
