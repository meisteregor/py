import sys

# Handling range and xrange
if sys.version_info.major == 2:
    gen = xrange
else:
    gen = range