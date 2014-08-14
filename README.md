ajit
===

## How to test

```sh
# just run in python 2
python ajit.py

# translate with pypy, and execute
hg clone https://bitbucket.org/pypy/pypy
python pypy/rpython/bin/rpython ajit.py
./ajit-c
```
