.PHONY: test

test: README
	@echo "[ run unit tests ]"
	python test/test_IPy.py || exit $?
	@echo
	@echo "[ test README ]"
	python -c "import doctest; doctest.testfile('README', optionflags=doctest.ELLIPSIS)" || exit $?

README: IPy.py
	python -c "import IPy; open('README', 'w').write(IPy.__doc__)"

