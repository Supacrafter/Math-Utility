"""
    A playground for a smaller version of this project
"""

from PeekableStream import PeekableStream
import re

def lex(chars_iter):
    # Key chars
    """
    List of key chars:

    CONSTANTS:
    1
    2
    3
    4
    5
    6
    7
    8
    9
    0

    VARIABLES:
    X --> X var
    Y --> Y var

    WRAPPERS
    () --> Parantheses
    [] --> Square Root
    || --> Absolute Value

    SEPERATORS
    ; --> Statement Seperator (End line)
    , --> Coordinate seperator

    MODIFY OPERATORS
    ^ --> Exponent
    + --> Add
    - --> Subtract
    * --> Multiply
    / --> Divide
    = --> Assignment (Special token for equality)

    EQUALITY OPERATORS
    < --> Less than (Non inclusive)
    > --> Greater than (Non Inclusive)
    <= --> Less than (Inclusive)
    >= --> Greater than (Inclusive)
    != --> Not equal to
    == --> Is equal to

    MINILEXER Only uses modify operators, wrappers, constants and variables
    """

    chars = PeekableStream(chars_iter)
    while chars.next is not None:
        c = chars.move_next()
        if c in " \n": pass
            # ignore white space
        elif c in "1234567890":
            print("Number!")
            # yield (("number", c))
        elif c in "XYxy":
            print("Variable!")
            # yield (("variable", c))
        elif c in "^+-*/":
            print("Operator!")
            # yield (("operator", c))
        elif c == "=":
            print("Assignment!")
            # yield (("assignment", c))
        else:
            raise Exception(
                "Unexpected symbol: " + c
            )

    pass


if __name__ == "__main__":
    userInp = input("Enter an equation: ")
    lex(userInp)
