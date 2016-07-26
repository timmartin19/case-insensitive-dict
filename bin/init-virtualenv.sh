#!/usr/bin/env bash -evx

mkvirtualenv "case-insensitive-dict"
workon "case-insensitive-dict"

pip install -e .
pip install -r requirements_dev.txt
