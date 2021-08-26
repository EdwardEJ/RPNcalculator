from collections import deque
import operator
import argparse

def calc(expr):
    '''
    Take in string
    each char is iterable, seperate numbers and operands into own indexes
    remove spaces while maintaining floating numbers
    while queue is not empty, add numbers to stack
    if string is an operator, execute operand and last two digits
    if next string is operator and number in stack, execute operator and next number in stack with previously generated number
    continue until queue is empty
    '''

    ops = { "+": operator.add,
           "-": operator.sub,
           "*": operator.mul,
           "/": operator.truediv,
          }
    operators = '+-=*/'
    stack = []
    exprNoSpaces = []
    for str in expr:
        if str.isalpha() and str not in operators:
            return "Cannot add letters"
        if str in operators:
            exprNoSpaces.append(str)
            continue
        if str.isdigit():
            exprNoSpaces.append(int(str))
        else:
            exprNoSpaces.append(float(str))
            
    queue = deque(exprNoSpaces)
    ans = 0

    if len(queue) == 1:
        return queue[0]
    
    while queue:
        next = queue[0]
        if type(next) == int or type(next) == float:
            stack.append(queue.popleft())          
        else:
            firstVal = stack.pop()
            secVal = stack.pop()
            queueOp = queue.popleft()
            ans = ops[f'{queueOp}'](secVal, firstVal)
            stack.append(ans)
    return ans

def Main():
    parser = argparse.ArgumentParser(description='Performs calculations using Reverse Polish Notation')
    parser.add_argument('expr', metavar='Expression', type=str, nargs='+', help='Enter an expression to calculate')

    args = parser.parse_args()
    result = calc(args.expr)
    print(result)

if __name__ == '__main__':
  Main()
