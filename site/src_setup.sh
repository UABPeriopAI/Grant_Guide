#!/bin/bash

cd /workspaces/Grant_Guide/src
pip install --upgrade pip setuptools wheel\
	    && pip install -e ".[dev]"
