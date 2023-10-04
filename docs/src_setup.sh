#!/bin/bash

cd /workspaces/Grant_Guide
pip install --upgrade pip setuptools wheel\
	    && pip install -e ".[dev]"
