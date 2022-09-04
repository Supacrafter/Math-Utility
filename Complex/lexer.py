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
    """

    chars = PeekableStream(chars_iter)
    while chars.next is not None:
        c = chars.move_next()
        if c in " \n": pass
            # ignore white space
        elif c in "()[]||":
            print("Wrapper! (" + c + ")")
            #yield (c, "")
        elif c in "XYxy":
            print("Variable! (" + c + ")")
            #yield ("variable", c)
        elif c in ";,":
            print("Seperator! (" + c + ")")
            #yield ("seperator", c)
        elif c in "^+-*/":
            print("Operator! (" + c + ")")
            #yield ("operation", c)
        elif c == "=":
            print("Assignment! (" + c + ")")
            #yield ("assignment", c)
        elif c in "><!":
            print("Comparison! (" + c + ")")
            #yield ("comparison", c)
        elif c in "1234567890":
            print("Number! (" + c + ")")
            #yield ("number", c)
        elif c in "\t": raise Exception(
            "Tabs are not valid"
        )
        else: raise Exception(
            "Unexpected character: '" + c + "'."
        )
    pass


def _scan_wrapper(delim, chars:PeekableStream):
    ret = ""
    while chars.next != delim:
        c = chars.move_next()
        if c is None:
            raise Exception (
                "Missing Wrapper."
            )
    ret += c
    chars.move_next()
    return ret

def _scan(first_char, chars, allowed):
    ret = first_char
    p = chars.next
    while p is not None and re.match(allowed, p):
        ret += chars.move_next()
        p = chars.next
    return ret

if __name__ == "__main__":
    userInp = input("Enter an equation: ")
    lex(userInp)