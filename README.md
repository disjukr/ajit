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

# after pypy translation, run the test suite
./test.sh
```

## See more

 * https://github.com/disjukr/pypy-tutorial-ko
 * http://pypy.readthedocs.org/en/latest/config/commandline.html
