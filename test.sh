#!/usr/bin/env bash

poetry run ansible localhost -M library -m option_py \
    -a size=10 \
    -a filepath=longfilepath \
    -c local


