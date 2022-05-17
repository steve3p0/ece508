""" ECE 508 Spring 2022
    Dr. Schubert
    Steve Braich sbraich@pdx.edu
    PSU ID: 953378420

    1. Turn in a .py file that includes a function that outputs the area and circumference of a circle on the same line.
       Your function should take a single argument (the radius of the circle).

       Yes, it’s very simple! But remember that the assessment rubric includes code evaluation
       of comment quality, clarity/readability, maintainability, algorithm and code efficiency.

       * Note: There should be one line of output. However, your function’s code should not be a single line!
               It could be (this is such a simple function), but in general, when computing two different
               output values, a multi-line program is likely to be much clearer.

    * Want to do more? Each chapter includes a “try it yourself” section.
"""

from math import pi


def area_and_circumference(radius: float) -> (float, float):
    """ Given the radius, calculate the area and circumference of a circle
    :param radius: the radius of the circle
    :type radius:  float
    :return: the area and circumference of a circle
    :rtype: (float, float)

    To run doctest unit tests, execute the following command:
    $ python -m doctest -v circle.py
    >>> area_and_circumference('XXX')
    Invalid value for the radius of a circle: XXX
    >>> area_and_circumference()
    Traceback (most recent call last):
    TypeError: area_and_circumference() missing 1 required positional argument: 'radius'
    >>> area_and_circumference(radius=-1)
    (3.141592653589793, -6.283185307179586)
    >>> area_and_circumference(radius=0)
    (0.0, 0.0)
    >>> area_and_circumference(radius=1)
    (3.141592653589793, 6.283185307179586)
    >>> area_and_circumference(radius=5)
    (78.53981633974483, 31.41592653589793)
    >>> area_and_circumference(radius=6.28)
    (123.89938770933571, 39.458403729087806)
    """

    try:
        # validate input
        radius = float(radius)

        # calculate the area and circumference
        area = pi * radius * radius
        circumference = 2 * pi * radius

        # return above values
        return area, circumference

    except ValueError:
        print(f"Invalid value for the radius of a circle: {radius}")


if __name__ == '__main__':
    # Get the user input
    r = input("Enter in the radius of a circle: ")

    # Calculate the output
    result = area_and_circumference(r)

    # Display the results and then go home!!
    if result is not None:
        a, c = result
        print(f"The area is {a} and the circumference is {c}.")
