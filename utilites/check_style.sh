#!usr/bash

#code style checker for linux systems in case of "venv" is virtualenv directory it will be excluded from checks
cd ..
pycodestyle --exclude=venv ./
