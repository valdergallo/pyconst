send_package:
    python setup.py sdist bdist_wheel
    twine upload dist/*

clean:
	find . -name '*.pyc' -delete
	ptyhon setup.py clean --all
	rm -rf pyconst.egg-info
	rm -rf dist
