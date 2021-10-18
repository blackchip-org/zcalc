#!/bin/bash

set -e

cd $(dirname "$0")
source venv/bin/activate
rm -rf dist
python -m build
python -m twine upload dist/*
