from __future__ import with_statement

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="ponger",
      version='0.1.0',
      author="Christopher Powell",
      author_email="powellchristoph@gmail.com",
      py_modules=["ponger"],
      description="A Python library that will compare two semantic version strings.",
      license="MIT",
      install_requires=["flask-restful"],
      )
