test:
	coverage run --omit="*/test*"  -m unittest discover -s tests/ -v

report:
	coverage report

dist:
	python setup.py bdist_wheel
