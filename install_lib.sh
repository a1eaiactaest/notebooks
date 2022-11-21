#!/usr/bin/env bash

git submodule update --init --recursive

cd lib/ && pip3 install -e .
