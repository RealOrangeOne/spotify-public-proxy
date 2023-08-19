#!/usr/bin/env bash

export PATH=env/bin:${PATH}

set -ex

black --check src tests

ruff check src tests

mypy src tests

nose2
