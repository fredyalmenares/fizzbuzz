#!/usr/bin/env bash
deactivate
rm -rdf ./src/venv-fizzbuzz
python3 -m venv ./src/venv-fizzbuzz
source ./src/venv-fizzbuzz/bin/activate