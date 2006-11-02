#!/usr/bin/env python
import doctest
import sys
if hasattr(doctest, "testfile"):
    print "=== Test README ==="
    failure,  tests = doctest.testfile('README', optionflags=doctest.ELLIPSIS)

    print "=== Test IPy ==="
    import IPy
    failure2, tests2 = doctest.testmod(IPy)
    failure += failure2
else:
    sys.stderr.write("WARNING: doctest has no function testfile (before Python 2.4), unable to check README\n")
    failure = 0
if failure:
    sys.exit(1)
else:
    sys.exit(0)

