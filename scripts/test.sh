#!/usr/bin/env bash

export PATH=env/bin:${PATH}

set -ex

black --check src tests

flake8 src tests

isort -rc -c src tests

mypy src tests
