# Python library for replacing file contents or filenames by dictionary mapping.

# Requirements 
Python3.6 or above (Requires mapping dictionary to be ordered for deterministic behavior).
Install requirements
pip install -r requirements.txt

# Usage
import far

to replace text in files:
far.far_infile(file_pattern, path, mapping):

to replace filenames:
far.far_filenames(file_pattern, path, mapping):

# Testing
Install requirements
pip install -r requirements_test.txt
run py.test
py.test
