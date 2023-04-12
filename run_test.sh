#!/bin/bash
source .env
$PWD/python3-virtualenv/bin/python -m unittest discover -v -s app/tests/