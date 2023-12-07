import util

import hashlib


def hash(text: str) -> str:
    return hashlib.md5(text.encode("ascii")).hexdigest()

def firstNzero(hexstr: str, n: int):
    return hexstr[0:n] == "0"*n



def run1():
    key = "ckczppom"
    num = 1
    while True:
        if firstNzero(hash(f"{key}{num}"), 5):
            print(num)
            break
        num += 1

def run2():
    key = "ckczppom"
    num = 1
    while True:
        if firstNzero(hash(f"{key}{num}"), 6):
            print(num)
            break
        num += 1
