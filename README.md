ajit
===

## How to test

```sh
# just run in python 2
python ajit.py <aheui_program>

# translate with pypy, and execute
hg clone https://bitbucket.org/pypy/pypy
python pypy/rpython/bin/rpython ajit.py
./ajit-c <aheui_program>
```
