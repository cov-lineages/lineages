from setuptools import setup, find_packages
import glob
import os
import pkg_resources
# Note: the _program variable is set in __init__.py.
# it determines the name of the package/final command line tool.
from lineages import __version__, _program

setup(name='lineages',
      version=__version__,
      packages=find_packages(),
      scripts=[],
      package_data={'lineages':['data/*']},
      description='hcov-2019 lineage data',
      url='https://github.com/aineniamh/lineages',
      author='Aine OToole, Verity Hill and Andrew Rambaut',
      author_email='aine.otoole@ed.ac.uk',
      entry_points="""
      [console_scripts]
      {program} = lineages.command:main
      """.format(program = _program),
      include_package_data=True,
      keywords=[],
      zip_safe=False)