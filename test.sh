#!/bin/bash

if [ -e snippets ]; then
    cd snippets
    git pull
else
    git clone https://github.com/aheui/snippets
fi
cd snippets
AHEUI="../ajit-c" bash test.sh standard
