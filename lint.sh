#!/usr/bin/env bash
flake8 .
black -q .
isort -q .
