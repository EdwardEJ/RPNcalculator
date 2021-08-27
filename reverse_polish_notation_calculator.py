import operator
import argparse

def calc():
    ops = { "+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv,
          }
    operators = '+-=*/'
    stack = []
    continue_expr = True

    while continue_expr:
        cmdLineExpr = input('Input: ')
        if cmdLineExpr == 'q':
            print('Exit')
            return
        elif cmdLineExpr == 'n':
            print('New Calculation')
            continue_expr = False
            calc()
        elif len(cmdLineExpr) > 1:
            for num in cmdLineExpr.split():
                if num.isalpha() and num not in operators:
                    print('Cannot add letters')
                    continue
                else:
                    if num.isdigit():
                        stack.append(int(num))
                    elif num not in operators:
                        stack.append(float(num))
                    elif num in operators:
                        expOperator = num
                        firstVal = stack.pop()
                        secVal = stack.pop()
                        result = ops[f'{expOperator}'](secVal, firstVal)
                        stack.append(result)
            print(stack[-1])
        else:
            if cmdLineExpr.isalpha() and cmdLineExpr not in operators:
                print('Cannot add letters')
                continue

            if cmdLineExpr in operators and len(stack) >= 2:
                firstVal = stack.pop()
                secVal = stack.pop()
                result = ops[f'{cmdLineExpr}'](secVal, firstVal)
                print(result)
                stack.append(result)
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
    parser.add_argument('expr', metavar='Expression', type=str, nargs='+', help='Enter an expression to calculate')

if __name__ == '__main__':
    Main()
