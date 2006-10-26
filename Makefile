.PHONY: test

test: README
	@echo "[ run unit tests ]"
	python test/test_IPy.py || exit $$?
	@echo
	@echo "[ test README ]"
	python -c "import doctest; doctest.testfile('README', optionflags=doctest.ELLIPSIS)" || exit $$?

egg: clean README
	python setup.py sdist bdist_egg

README: IPy.py
	python -c "import IPy; open('README', 'w').write(IPy.__doc__)"

IPy.html: README
	rst2html README $@ --stylesheet=rest.css

clean:
	rm -rf README IPy.html *.pyc build dist IPy.egg-info

