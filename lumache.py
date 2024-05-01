"""
Lumache - Python library for cooks and food lovers.
"""

__version__ = "0.1.0"

import os, sys
import sphinx_rtd_theme

pygments_stype = 'sphinx'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
