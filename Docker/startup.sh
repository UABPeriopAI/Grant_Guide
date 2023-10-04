#!/bin/sh

#to test the package as you go
python3 -m pip install pip setuptools wheel
python3 -m pip install -e ".[dev]"
