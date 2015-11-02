test:
	@coverage run --omit="*/test*"  -m unittest discover -s tests/ -v 2>&1 | sed -e "s/\.\.\. ok/\.\.\. `printf '\033[32mok\033[0m'`/" -e "s/ERROR/`printf '\033[31mERROR\033[0m'`/" -e "/FAILED/!s/FAIL/`printf '\033[31mFAIL\033[0m'`/"

report:
	@coverage report

dist:
	@python setup.py bdist_wheel
