#!/usr/bin/env bash
deactivate -d
rm -rdf ./src/venv-fizzbuzz
cd src
python3 -m venv ./venv-fizzbuzz
cd ..
source ./src/venv-fizzbuzz/bin/activate
pip3 install -r ./src/requirement-dev.txt