venv:
	virtualenv venv
	source ./venv/bin/activate; \
	pip install -r requirements.txt; \

clean:
	rm -rf '*.pyc'
	rm -rf '*.pyo'
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf venv

install:
	python setup.py install

.PHONY: venv clean install