import os, fnmatch

# https://stackoverflow.com/questions/1724693/find-a-file-in-python
def _find(pattern, path):
    """
    Function that finds files based on pattern in path.

    Args:
    pattern: string
        regex pattern defining files to be found.
    path: string
        path on which to search for files.
    """
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def far_infile(file_pattern="*", path=".", mapping={}):
    """
    Function that replaces text in files based on mapping. 

    Args:
    file_pattern: string
        regex pattern defining files to be found.
    file_path: string
        path on which to search for files.
    mapping: dict{string: string} 
        mapping for in file replacement.
    """
    filenames = _find(pattern=file_pattern, path=path)
    for filename in filenames:
        with open(filename, "r", newline="\n") as f:
            file_contents = f.read()
        for k,v in mapping.items():
            if k in file_contents:
                file_contents = file_contents.replace(k, v)
        with open(filename, "w", newline="\n") as f:
            f.write(file_contents)

def far_filename(file_pattern="*", path=".", mapping={}):
    """
    Function that replaces filenames based on mapping. 

    Args:
    file_pattern: string
        regex pattern defining files to be found.
    file_path: string
        path on which to search for files.
    mapping: dict{string: string} 
        mapping for filename replacement.
    """
    filenames = _find(pattern=file_pattern, path=path)
    for filename in filenames:
        split_filename = filename.split("/")
        temp_filename = split_filename[-1]
        new_filename = temp_filename
        for k,v in mapping.items():
            if k in temp_filename:
                new_filename = temp_filename.replace(k, v)
                # Only replace the first match
                break
        if temp_filename != new_filename:
            split_filename[-1] = new_filename
        os.rename(filename, "/".join(split_filename))
