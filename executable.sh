#!/bin/bash
# Just type in terminal ./executable.sh
> out.txt
for VAR in 1 2 3 4 5, 6
do  
    python3 engine.py
    grep -i 'Final' gamelog.txt >> out.txt
done