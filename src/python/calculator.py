#!/usr/bin/env python3


class Calculator:
    ''' Calculator class '''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def substract(self):
        return self.a - self.b


def main():
    ''' Main function '''

    a = 10
    b = 4
    calculator = Calculator(a,b)

    add_result = calculator.add()
    print("A + B = " + str(add_result))
    
    substract_result = calculator.substract()
    print("A - B = " + str(substract_result))
            
if __name__ == '__main__':
    main()
