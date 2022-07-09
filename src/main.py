import operator


class RPN:
    operations = {'+': operator.add, '-': operator.sub, '%': operator.mod, '*': operator.mul, '/': operator.floordiv}
    result = None
    stack = []
    expression = None

    def evaluate(self, expression: str):
        self.expression = expression
        self.stack = []
        self.result = None

        #  Iterate through input split by space and check for operators
        for value in self.expression.split():
            if value in self.operations:
                try:
                    b = self.stack.pop()
                    a = self.stack.pop()
                    # Call operation from dictionary on operands taken from top of the stack
                    c = self.operations[value](a, b)
                except IndexError:
                    print("Error, too many operators/ out of place operators found in the expression.")
                    return
                except ZeroDivisionError:
                    print("Error, division by zero, the expression cannot be evaluated.")
                    return
            else:
                c = value

            try:
                self.stack.append(int(c))
            except ValueError:
                print("Error, '",c,"' is not a valid input. Input expression must only contain integers, the operators +,-,*,/,% and spaces.")
                return

        if len(self.stack) == 1:
            self.result = self.stack.pop()
        else:
            print("Error, input expression does not contain enough operators.")


class TooManyOperatorsError(Exception):
    def __str__(self):
        return 'Error, too many operators/ out of place operators found in the expression.'


class InvalidCharError(Exception):
    def __init__(self, invalid_char, *args):
        super().__init__(args)
        self.invalid_char = invalid_char

    def __str__(self):
        return f'Error, "{self.invalid_char}" is not a valid input. Input expression must only contain integers, ' \
               'the operators +,-,*,/,% and spaces.'


class TooFewOperatorsError(Exception):
    def __str__(self):
        return 'Error, input expression does not contain enough operators.'


if __name__ == '__main__':
    string_expression = input("Input your RPN expression:\n")
    calculation = RPN()
    calculation.evaluate(string_expression)
    print(calculation.result)


