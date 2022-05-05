"""Define package build and test dependencies."""

from setuptools import setup

setup(
    name = "AYTO Solver",
    description = "A way to solve and keep track of matches in binary AYTO situations.",
    author = "David Hahn",
    author_email="hahnx117@umn.edu",
    url = "https://github.com/hahnx117/ayto_solver",
    packages = [],
    license = "MIT",
    python_requires = ">=3.6",
    install_requires = [
        "pandas",
        "os",
    ],
    tests_require = [],
    test_suite = "tests",
)
