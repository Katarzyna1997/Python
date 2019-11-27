from zad15 import Complex


class Calculator:
    operations = ['+', '-', '*', '/']

    def __init__(self):
        self.result = None

    def calculate(self, num1, num2, operation):
        if operation not in Calculator.operations: 
            raise NotImplementedError('An operation is not implemented.')
        src = 'self.result = num1 {} num2'.format(operation)
        exec(src, locals())
        

if __name__ == '__main__':

    calculator = Calculator()
    while True:
        try:
            print('\n---------- CALCULATOR ----------')
            r, i = input("Enter first number (e.g.: '1+i3', '2-i5'): ").split('i')
            num1 = Complex(float(r[:-1]), float(r[-1] + i))
            r, i = input("Enter first number (e.g.: '1+i3', '2-i5'): ").split('i')
            num2 = Complex(float(r[:-1]), float(r[-1] + i))
            action = input("Select an action {0}: ".format(Calculator.operations))
            calculator.calculate(num1, num2, action)
            print('{0} {1} {2} = {3}'.format(num1,
                                             action,
                                             num2,
                                             calculator.result))
        except ValueError:
            print('Wrong format!')
