from calculator import Calculator

def main():
    ''' Calculator main function '''

    a = 10
    b = 4
    calculator = Calculator(a,b)

    print("A + B = " + str(calculator.add()))
    print("A - B = " + str(calculator.substract()))


if __name__ == '__main__':
    main()

