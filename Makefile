.PHONY: tests egg install clean

PYTHON=python

tests:
	@echo "[ run unit tests ]"
	tox -e py{2.7,3.4}
	@echo "[ test README ]"
	tox -e docs
	@echo "[ lint code ]"
	tox -e lint

egg: clean
	$(PYTHON) setup.py sdist bdist_egg

IPy.html: README
	rst2html README $@ --stylesheet=rest.css

install:
	./setup.py install

clean:
	rm -rf IPy.html *.pyc build dist IPy.egg-info

