#!/usr/bin/env bash
cd src
python3 -m venv venv-fizzbuzz
source ./venv-fizzbuzz/bin/activate
pip3 install -r ./requirement-dev.txt
