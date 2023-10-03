import sys

_3x_version ="Welcome"

_2x_version ="""You are use one of the 2x versions in python.
      Install one of the 3x versions of python for to be able to run the program"""

if sys.version_info.major<3:
    print(_2x_version)
else:
  print(_3x_version)