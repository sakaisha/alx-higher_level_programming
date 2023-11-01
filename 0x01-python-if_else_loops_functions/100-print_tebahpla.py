#!/usr/bin/python3
for i in reversed(range(97, 123)):
    print("{}".format(chr(i)), end="")
    if i % 2 == 0:
        i -= 32
print()
