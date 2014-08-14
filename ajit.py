import os
import sys

class Cursor:
    def __init__(self, codespace, x=0, y=0, dx=0, dy=1):
        self.codespace = codespace
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def line(self):
        try:
            line = self.codespace[self.y]
        except IndexError:
            line = None
        return line

    def code(self):
        return get_code(self.codespace, self.x, self.y)

    def move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        line = self.line()
        width = len(line) if line is not None else 0
        height = len(self.codespace)
        if self.x < 0 and self.dx < 0:
            self.x = width - 1
        elif self.x >= width and self.dx > 0:
            self.x = 0
        if self.y < 0 and self.dy < 0:
            self.y = height - 1
        elif self.y >= height and self.dy > 0:
            self.y = 0

class Stack:
    def __init__(self):
        self.list = []
    def push(self, value):
        self.list.append(value)
    def pop(self):
        return self.list.pop()
    def duplicate(self):
        self.list.append(self.list[-1])
    def swap(self):
        self.list[-1], self.list[-2] = self.list[-2], self.list[-1]
    def send(self, to):
        to.push(self.pop())
    def __len__(self):
        return len(self.list)

class Machine:
    def __init__(self, codespace):
        self.cursor = Cursor(codespace)

def extract_index(func):
    def extractor(code):
        if 0xac00 <= code <= 0xd7a3:
            return func(code - 0xac00)
        return -1
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

def get_code(codespace, x, y):
    try:
        line = codespace[y]
    except IndexError:
        return (-1, -1, -1)
    try:
        code = line[x]
    except IndexError:
        return (-1, -1, -1)
    return code

def parse(code):
    result = []
    line = []
    for char in code:
        if char == u"\r":
            continue
        elif char == u"\n":
            result.append(line)
            line = []
        else:
            charcode = ord(char)
            line.append(
                (get_cho(charcode),
                 get_jung(charcode),
                 get_jong(charcode)))
    result.append(line)
    return result

def run(code):
    machine = Machine(parse(code))
    # TODO: run machine
    storage = Stack()
    storage.push(1)
    storage.push(2)
    storage.swap()
    print storage.pop(), storage.pop()

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
