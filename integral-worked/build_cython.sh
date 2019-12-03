#! /bin/bash
#
# Helper script to build the Cython integral code...

# Cleanup
#
rm -rf build cpintegral.so

# Build code into current directory (under build)
#
python setup.py build 

#
# Copy resultant library here..
cp build/lib.*/cpintegral.so .

# Tidy up
rm -rf ./build
