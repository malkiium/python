def genere (ch: str, e: int) -> str:
    return ch*e

assert genere("abc", 3) == "abcabcabc"
print(genere("abc", 3))
assert genere("abc", 0) == ""
print(genere("abc", 0))
assert genere("abc", 1) == "abc"
print(genere("abc",1))
assert genere("", 3) == ""
print(genere("", 3))