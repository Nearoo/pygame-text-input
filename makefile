
build: FORCE
	rm -rf build/ dist/ pygame_textinput.egg-info/
	python3 setup.py sdist bdist_wheel
	python3 -m twine check dist/*

upload: FORCE
	python3 -m twine upload dist/*


FORCE: ;