.PHONY: test
PYTHON=python

test: README
	@echo "[ run unit tests ]"
	PYTHONPATH=$(PWD) $(PYTHON) test/test_IPy.py || exit $$?
	@echo
	@echo "[ test README ]"
	$(PYTHON) test_doc.py || exit $$?

egg: clean README
	$(PYTHON) setup.py sdist bdist_egg

README: IPy.py
	$(PYTHON) -c "import IPy; open('README', 'w').write(IPy.__doc__)"

IPy.html: README
	rst2html README $@ --stylesheet=rest.css

install:
	./setup.py install

clean:
	rm -rf README IPy.html *.pyc build dist IPy.egg-info

