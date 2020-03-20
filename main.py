#!/usr/bin/env python3


import sys


def main():
    """
    The main function takes two command line arguments, converts them to lower case and checks
    if every character in string input 1 uniquely maps to every character in string input 2.
    :return: -
    """
    if len(sys.argv) != 3:
        print("usage: python3 main.py [arg1] [arg2]")
        sys.exit()
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    if len(s1) == len(s2):
        d = {}
        s1 = s1.lower()
        s2 = s2.lower()
        flag = True
        for i in range(len(s1)):
            if s1[i] not in d:
                d[s1[i]] = s2[i]
            else:
                if not s2[i] == d[s1[i]]:
                    flag = False
        print(flag)
    else:
        print(False)


if __name__ == "__main__":
    main()
