#!/bin/bash
rm -rf dist/*
python3.6 setup.py sdist
python3.6 setup.py bdist_wheel
twine upload dist/*
git push
sudo python3.6 setup.py install
