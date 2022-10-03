#!/usr/bin/env bash

git submodule update --init

cd lib/ && pip3 install -e .
