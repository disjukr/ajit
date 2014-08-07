import os
import sys

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
    print code.encode("utf-8")
    return 0

def target(*args):
    return entry_point, None

if __name__ == "__main__":
    entry_point(sys.argv)
