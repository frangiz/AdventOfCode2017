import os

def get_file_contents(filename):
    inputfilename = os.path.join('inputs', filename)
    contents = []
    with open(inputfilename, 'r') as f:
        for line in f:
            contents.append(line)
    return contents
