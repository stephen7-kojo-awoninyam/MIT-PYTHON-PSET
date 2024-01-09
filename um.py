import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    num = re.findall(r"um\W",s,re.IGNORECASE)

    return len(num)
    




if __name__ == "__main__":
    main()