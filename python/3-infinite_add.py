#!/usr/bin/python3
import sys

value = sys.argv

index = 1
summ = 0
while index < len(sys.argv):
    summ += int(value[index])
    index += 1

if __name__=="__main__":
    print(summ)
