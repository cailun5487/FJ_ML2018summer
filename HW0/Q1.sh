#!/bin/bash

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
read -p "Please enter the absolute path of text file:" FILEPATH

if command -v python3 &>/dev/null; then
	python3 $SCRIPTPATH/Q1.py $FILEPATH
else
	python3 $SCRIPTPATH/Q1.py $FILEPATH
fi

