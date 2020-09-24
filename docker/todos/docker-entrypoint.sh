#!/bin/bash
set -e

cd /usr/src/app

/wait-for-it.sh db:3306

coverage run --source todo --omit *__init__.py -m unittest2 discover -p="*_test.py"