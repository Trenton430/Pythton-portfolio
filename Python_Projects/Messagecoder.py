decode = ("")
encode = ("")
a = input("welcome to message encoder press a if you want to code a message press b if you want to decode a message").lower()
if a == "b":
    second = input("what would you like to decode")
    for letter in second:
        if "a" in letter:
            decode += "b"
        if "b" in letter:
            decode += "a"
        if "c" in letter:
            decode += "b"
        if "d" in letter:
            decode += "c"
        if "e" in letter:
            decode += "d"
        if "f" in letter:
            decode += "e"
        if "g" in letter:
            decode += "f"
        if "h" in letter:
            decode += "g"
        if "i" in letter:
            decode += "h"
        if "j" in letter:
            decode += "i"
        if "k" in letter:
            decode += "j"
        if "l" in letter:
            decode += "k"
        if "m" in letter:
            decode += "l"
        if "n" in letter:
            decode += "m"
        if "o" in letter:
            decode += "n"
        if "p" in letter:
            decode += "o"
        if "q" in letter:
            decode += "p"
        if "r" in letter:
            decode += "q"
        if "s" in letter:
            decode += "r"
        if "t" in letter:
            decode += "s"
        if "u" in letter:
            decode += "t"
        if "v" in letter:
            decode += "u"
        if "w" in letter:
            decode += "v"
        if "x" in letter:
            decode += "w"
        if "y" in letter:
            decode += "x"
        if "z" in letter:
            decode += "y"
elif a == "a":
    first = input("what do you want to encode")
    for letter in first:
        if "a" in letter:
            encode += "b"
        if "b" in letter:
            encode += "c"
        if "c" in letter:
            encode += "d"
        if "d" in letter:
            encode += "e"
        if "e" in letter:
            encode += "f"
        if "f" in letter:
            encode += "g"
        if "g" in letter:
            encode += "h"
        if "h" in letter:
            encode += "i"
        if "i" in letter:
            encode += "j"
        if "j" in letter:
            encode += "k"
        if "k" in letter:
            encode += "l"
        if "l" in letter:
            encode += "m"
        if "m" in letter:
            encode += "n"
        if "n" in letter:
            encode += "o"
        if "o" in letter:
            encode += "p"
        if "p" in letter:
            encode += "q"
        if "q" in letter:
            encode += "r"
        if "r" in letter:
            encode += "s"
        if "s" in letter:
            encode += "t"
        if "t" in letter:
            encode += "u"
        if "u" in letter:
            encode += "v"
        if "v" in letter:
            encode += "w"
        if "w" in letter:
            encode += "x"
        if "x" in letter:
            encode += "y"
        if "y" in letter:
            encode += "z"
        if "z" in letter:
            encode += "1"
    print("this is your encoded message = " + encode)
print(decode + " is your encoded message")
