#!/usr/bin/python3
import sys
if __name__ == "__main__":
    x = sys.argv[1:]
    sum = 0
for i in x:
    sum += int(i)
print(sum)
