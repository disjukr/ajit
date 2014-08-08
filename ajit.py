import os
import sys

def extract_index(func):
    def extractor(code):
        return func(ord(code) - 0xac00)
    return extractor

@extract_index
def get_cho(syllable_code):
    return syllable_code // 588

@extract_index
def get_jung(syllable_code):
    return (syllable_code // 28) % 21

@extract_index
def get_jong(syllable_code):
    return syllable_code % 28

def parse(code):
    result = []
    line = []
    for char in code:
        if char == "\r":
            continue
        elif char == "\n":
            result.append(line)
            line = []
        else:
            line.append(char)
    result.append(line)
    return result

def run(code):
    codespace = parse(code)
    code = codespace[0][0]
    print get_cho(code), get_jung(code), get_jong(code)

def entry_point(argv):
    # filename = argv[0]
    filename = "99dan.aheui"
    fp = os.open(filename, os.O_RDONLY, 0777)
    code = ""
    while True:
        read = os.read(fp, 4096)
        if len(read) == 0:
            break
        code += read
    code = code.decode("utf-8")
    run(code)
    return 0

def target(*args):
    return entry_point, None

if __name__ == "__main__":
    entry_point(sys.argv)
