import pytest
import os
import far
import shutil

@pytest.fixture
def test_setup():
    if os.path.exists("./test"):
        shutil.rmtree("./test", ignore_errors=True)
    os.mkdir("./test")
    with open("./test/my_first_testfile.txt", "w") as f:
        f.write("I love cake")

def test_far_infile_replace(test_setup):
    mapping = {"love": "hate"}
    far.far_infile(file_pattern="*.txt", path="./test", mapping=mapping)
    with open("./test/my_first_testfile.txt", "r") as f: file_contents = f.read()
    assert(file_contents == "I hate cake")

def test_far_inplace_ignore_file_pattern(test_setup):
    mapping = {"love": "hate"}
    far.far_infile(file_pattern="*.does_not_exist", path="./test", mapping=mapping)
    with open("./test/my_first_testfile.txt", "r") as f:
        file_contents = f.read()
    assert(file_contents == "I love cake")

def test_far_inplace_ignore_directory(test_setup):
    mapping = {"love": "hate"}
    far.far_infile(file_pattern="*.txt", path="./does_not_exist", mapping=mapping)
    with open("./test/my_first_testfile.txt", "r") as f:
        file_contents = f.read()
    assert(file_contents == "I love cake")

def test_far_inplace_ignore_mapping(test_setup):
    mapping = {"adore": "hate"}
    far.far_infile(file_pattern="*.txt", path="./test", mapping=mapping)
    with open("./test/my_first_testfile.txt", "r") as f:
        file_contents = f.read()
    assert(file_contents == "I love cake")

def test_far_filename_replace(test_setup):
    mapping = {"first": "modified"}
    far.far_filename(file_pattern="*.txt", path="./test", mapping=mapping)
    with open("./test/my_modified_testfile.txt", "r") as f:
        file_contents = f.read()
    assert(file_contents == "I love cake")
    assert(not os.path.exists("./test/my_first_testfile.txt"))

def test_far_filename_ignore_file_pattern(test_setup):
    mapping = {"first": "modified"}
    far.far_filename(file_pattern="*.json", path="./test", mapping=mapping)
    assert(os.path.exists("./test/my_first_testfile.txt"))
    assert(not os.path.exists("./test/my_modified_testfile.txt"))

def test_far_filename_ignore_directory(test_setup):
    mapping = {"first": "modified"}
    far.far_filename(file_pattern="*.txt", path="./does_not_exist", mapping=mapping)
    assert(os.path.exists("./test/my_first_testfile.txt"))
    assert(not os.path.exists("./test/my_modified_testfile.txt"))

def test_far_filename_ignore_mapping(test_setup):
    mapping = {"second": "modified"}
    far.far_filename(file_pattern="*.txt", path="./does_not_exist", mapping=mapping)
    assert(os.path.exists("./test/my_first_testfile.txt"))
    assert(not os.path.exists("./test/my_modified_testfile.txt"))
