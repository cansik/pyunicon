#!/usr/bin/env bash

# test
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest

# public
python setup.py register -r pypi
python setup.py sdist upload -r pypi