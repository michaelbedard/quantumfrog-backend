

import re
from sympy import Rational, sqrt, sympify

import re


def parse_latex_to_string(latex_expression):
    """
    Parses a LaTeX quantum state expression and extracts terms as a string.

    Args:
        latex_expression (str): The LaTeX string representing the quantum state.
                                Example: "\\frac{\\sqrt{2}}{2} |0\\rangle + \\frac{\\sqrt{2}}{2} |1\\rangle"

    Returns:
        str: A string representation of the parsed quantum state.
             Example: "1/sqrt(2) |0> + 1/sqrt(2) |1>"
    """
    # Preprocess the LaTeX string to remove whitespace
    latex_expression = latex_expression.replace(" ", "")

    # Pattern to match terms of the form coefficient|state>
    pattern = re.compile(r"(?:(\S+)\s*\|([^|>]+)\\rangle)")

    # Extract terms
    matches = pattern.findall(latex_expression)
    terms = []

    for coeff, state in matches:
        # Convert LaTeX coefficients to readable strings
        if coeff == "1":
            value = "1"
        elif coeff == "0":
            value = "0"
        elif coeff == r"\frac{\sqrt{2}}{2}":
            value = "1/sqrt(2)"
        else:
            value = coeff  # Keep other coefficients as-is

        # Append to terms list
        terms.append(f"{value} |{state}>")

    # Join terms into a single string with proper formatting
    return " + ".join(terms)


