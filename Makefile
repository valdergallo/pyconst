send_package:
	python setup.py sdist bdist_wheel
	twine upload dist/*

clean:
	find . -name '*.pyc' -delete
	python setup.py clean --all
	rm -rf pyconst.egg-info
	rm -rf dist

test:
	pytest tests -vsrx

coverage:
	pytest tests -vsrx --cov=pyconst --cov-report html

