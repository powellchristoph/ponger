from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import ponger

setup(name="ponger",
      version=ponger.__version__,
      author="Christopher Powell",
      author_email="powellchristoph@gmail.com",
      py_modules=["ponger"],
      description="A Python library that will compare two semantic version strings.",
      license="MIT",
      )
