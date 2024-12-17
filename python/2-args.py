#!/usr/bin/python3
import sys
value = sys.argv
num = len(value) -1
if len(value) < 1:
    print("No Argument passed")
else:
    print(f"{num} Arguments:")
index = 1
while index <= num:
    print(f"{index}: {value[index]}")
    index += 1

