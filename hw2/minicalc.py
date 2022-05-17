""" ECE 508 Spring 2022
    Dr. Schubert
    Steve Braich sbraich@pdx.edu
    PSU ID: 953378420

    Your solutions should include the code to solve each problem and a transcript (e.g. screenshots) of your
    programs working. The assessment of your code will consider comment quality, clarity/readability,
    maintainability, algorithm and code efficiency.

    1) Calculator: Write a function (‘minicalc’) that when executed provides an interactive calculator
       application with the following functions:

          a. help
          b. add for any number of arguments (e.g. “add 3 5 6 7 8 999 -2 555”)
          c. modulus operator (e.g. “% 8 3”)
          d. your choice of two functions from the math module (e.g. “sin 4”)
          e. exit calculator

       The calculator should be interactive: accept user input, cause the desired function to execute and
       then prompt for more user input. Here’s a prototype usage session:

       --------------------------------------------------------------------------------------
       |>>> minicalc()                                                                      |
       |    mc> help                                                                        |
       |    Sorry, not much help so far                                                     |
       |    The only commands that work so far are: help, add, exit                         |
       |    eventually % and sin will be implemented!                                       |
       |                                                                                    |
       |    mc> add 45 500 5 -111                                                           |
       |    439                                                                             |
       |                                                                                    |
       |    mc> % 9 2                                                                       |
       |    Is that 9 mode 2 you want?                                                      |
       |    OOOH! a mod operation. Wish I had implemented that!                             |
       |                                                                                    |
       |    mc> sin 6                                                                       |
       |    Ok, I haven't implemented that either, but I still have a week!                   |
       |                                                                                    |
       |    mc> exit                                                                        |
       --------------------------------------------------------------------------------------

"""
import math


def help(cmd: str = None) -> str:
    """ Return a help message screen to the user
    :param cmd: command to provide help on (default is None)
    :type cmd: str
    :return: Help message
    :rtype: str

    To run doctest unit tests, execute the following command:
    $ python -m doctest -v minicalc.py
    >>> print(help())
    Minicalc is a mini-calculator that provides functions for add, %, sin, and cos.
    To get help on a specific command, type "help [command name]".
    >>> print(help('add'))
    add: this function adds multiple numbers together.
    Example: add 45 500 5 -111
    The result should be: 439
    >>> print(help('%'))
    %: this function is the modulus function.
    Example: 13 % 10
    The result should be: 3
    >>> print(help('sin'))
    sin: this function is the sine trigonometric function.
    Example: sin 1
    The result should be: 0.841
    >>> print(help('cos'))
    cos: this function is the cosine trigonometric function.
    Example: cos 1
    The result should be: 0.540
    >>> print(help('xyz'))
    xyz: unknown function.
    """

    msg = ""
    if cmd is None:
        msg = 'Minicalc is a mini-calculator that provides functions for add, %, sin, and cos.\n' \
            + 'To get help on a specific command, type "help [command name]".'
    elif cmd == 'add':
        msg = 'add: this function adds multiple numbers together.\n' \
            + 'Example: add 45 500 5 -111\n' \
            + 'The result should be: 439'
    elif cmd == '%':
        msg = '%: this function is the modulus function.\n' \
            + 'Example: 13 % 10\n' \
            + 'The result should be: 3'
    elif cmd == 'sin':
        msg = 'sin: this function is the sine trigonometric function.\n' \
            + 'Example: sin 1\n' \
            + 'The result should be: 0.841'
    elif cmd == 'cos':
        msg = 'cos: this function is the cosine trigonometric function.\n' \
            + 'Example: cos 1\n' \
            + 'The result should be: 0.540'
    else:
        msg = f'{cmd}: unknown function.'

    return msg


def calculate(operator: str, operands: list[float]) -> float:
    """ Calculate a math function using the operator and operands variables
    :param operator: the math operator
    :type operator: str
    :param operands: the operand arguments
    :type operands: float
    :return: the calculated result
    :rtype: float

    To run doctest unit tests, execute the following command:
    $ python -m doctest -v minicalc.py
    >>> calculate(operator='add', operands=[45, 500, 5, -111])
    439
    >>> calculate(operator='%', operands=[9, 2])
    1
    >>> calculate(operator='sin', operands=[6])
    -0.27941549819892586
    >>> calculate(operator='cos', operands=[1])
    0.5403023058681398
    >>> calculate(operator='xyz', operands=[1])
    Traceback (most recent call last):
     ...
    NameError: 'xyz' unknown function.
    >>> calculate(operator='add', operands=[1])
    1
    >>> calculate(operator='%', operands=[9, 0])
    Traceback (most recent call last):
     ...
    ZeroDivisionError: integer division or modulo by zero
    >>> calculate(operator='add', operands=None)
    0
    >>> calculate(operator='add', operands=['blah', 'blah'])
    Traceback (most recent call last):
     ...
    TypeError: unsupported operand type(s) for +=: 'int' and 'str'
    >>> calculate()
    Traceback (most recent call last):
     ...
    TypeError: calculate() missing 2 required positional arguments: 'operator' and 'operands'
    """

    result = 0
    if operator is None:
        msg = 'Minicalc is a mini-calculator that provides functions for add, %, sin, and cos.\n' \
            + 'To get help on a specific command, type "help [command name]".'
    elif operator == 'add':
        if operands is None or len(operands) < 1:
            return 0
        for o in operands:
            result += o
    elif operator == '%':
        result = operands[0] % operands[1]
    elif operator == 'sin':
        result = math.sin(operands[0])
    elif operator == 'cos':
        result = math.cos(operands[0])
    else:
        raise NameError(f"'{operator}' unknown function.")

    if float(result).is_integer():
        result = int(result)
    return result


if __name__ == '__main__':

    while True:
        command = input(f"\nmc> ")
        if command == 'exit':
            raise SystemExit(0)

        argv = command.split()
        cmd = argv[0]
        args = argv[1:]
        if cmd == 'help':
            if len(args) == 0:
                print(help())
            else:
                print(help(cmd=args[0]))
        else:
            args = [float(x) for x in args]
            print(calculate(operator=cmd, operands=args))
