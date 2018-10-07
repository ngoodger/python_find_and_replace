import os, fnmatch

# https://stackoverflow.com/questions/1724693/find-a-file-in-python
def _find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def far_infile(file_pattern="*", path=".", mapping={}):
    filenames = _find(pattern=file_pattern, path=path)
    for filename in files:
        with open(filename, "r") as f:
            file_contents = f.read()
        for k,v in mapping.items():
            file_contents = file_contents.replace(k, v) 
        with open(file, "w") as f:
            f.write(file_contents)

def far_filename(file_pattern="*", path=".", mapping={})
    filenames = _find(pattern=file_pattern, path=path)
    for filename in filenames:
        for k,v in mapping.items():
            if k in filename:
                temp_filename = filename
                temp_filename.replace(k, v)
                os.rename(filename, temp_filename)

