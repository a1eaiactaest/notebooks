#!/usr/bin/env bash

git submodule update

cd lib/ && pip3 install -e .
