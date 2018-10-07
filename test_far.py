import pytest
import os
import far

@pytest.fixture
test_setup():
    os.mkdir("./test")
    with open("./test/my_first_testfile.txt", "w") as f:
        f.write("I love cake")

def test_far_infile_replace(test_setup):
    mapping = {"love": "hate"}
    far.far_infile(file_pattern=".txt", path="./test", mapping=mapping)
    with open("./test/my_first_testfile.txt", "r") as f:
        file_contents = f.read()

def test_far_inplace_ignore_file_patter(test_setup)
