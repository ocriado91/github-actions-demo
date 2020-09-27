import pytest
import sys

sys.path.append('..')

from calculator import Calculator

def test_add():
    calculator = Calculator(10,4)
    assert calculator.add() == 14

def test_substract():
    calculator = Calculator(10,4)
    assert calculator.substract() == 6

def main():
    ''' Main function '''

    # Testing add function
    test_add()

    # Testing substract function
    test_substract()


if __name__ == '__main__':
    main()

