#!/usr/bin/python3
for b in range(ord('z'), ord('a') - 1, -2):
    print(f"{b:c}{chr(b-33):s}", end="")
