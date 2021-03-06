help:
	@echo 'Makefile for inori                      '
	@echo '                                        '
	@echo 'Usage:                                  '
	@echo '   make install    install as a package '
	@echo '   make uninstall  uninstall inori      '

requirements:
	pip install -r requirements.txt

requirements-dev:
	pip install -r requirements-dev.txt

develop: requirements requirements-dev
	python setup.py develop
	@echo
	@echo "Install finished"

install: requirements
	python setup.py install --record install.record
	@echo
	@echo "Install finished."

uninstall:
	cat install.record | xargs rm -rf
	@echo
	@echo "Uninstall finished."
