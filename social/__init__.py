"""
Licensed under a 3-clause BSD style license - see LICENSE.rst
"""

from importlib.metadata import version, PackageNotFoundError

__all__ = []

try:
    __version__ = version("pyaci")
except PackageNotFoundError:
    pass  # package is not installed
