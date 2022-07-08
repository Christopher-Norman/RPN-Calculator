import operator


class RPN:
    operations = {'+': operator.add, '-': operator.sub, '%': operator.mod, '*': operator.mul, '/': operator.floordiv}
    result = 0

    def __init__(self, expression: str):
        self.expression = expression

    def evaluate(self):
        stack = []
        #  Iterate through input split by space and check for operators
        for i in self.expression.split():
            if i in self.operations:
                try:
                    b = stack.pop()
                    a = stack.pop()
                    c = self.operations[i](a, b)
                except IndexError:
                    print("Error, too many operators/ out of place operators found in the expression.")
                    return
            else:
                c = i

            try:
                stack.append(int(c))
            except ValueError:
                print("Error, input expression must only contain integers, the operators +,-,*,/,% and spaces.")
                return

        if len(stack) == 1:
            self.result = stack.pop()
        else:
            print("Error, input expression does not contain enough operators.")


if __name__ == '__main__':
    string_expression = input("Input your RPN expression:\n")
    calculation = RPN(string_expression)
    calculation.evaluate()
    print(calculation.result)
