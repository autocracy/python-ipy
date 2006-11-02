import doctest
import sys
if hasattr(doctest, "testfile"):
    failure, tests = doctest.testfile('README', optionflags=doctest.ELLIPSIS)
else:
    sys.stderr.write("WARNING: doctest has no function testfile (before Python 2.4), unable to check README\n")
    failure = 0
if failure:
    sys.exit(1)
else:
    sys.exit(0)

