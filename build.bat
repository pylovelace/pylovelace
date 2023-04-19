:: This script builds the source distribution and wheel for pylovelace.
@echo off

echo "Building source distribution and wheel..."

set PYTHON=py -3.11

:: %PYTHON% setup.py sdist --formats=zip
%$PYTHON% setup.py bdist_wheel

echo "Finished building source distribution and wheel."