#!/usr/bin/env python3

import curses, sys
import hacker


def usage():
    usage_string = (
        f"Usage: {sys.argv[0]} [options] [file]\n"
        "Options:\n"
        "  -h, --help\t\t\tDisplay this help message\n"
    )
    # black/green or default
    # chunk length
    # word list (file)

    print(usage_string)
    exit()


def main():
    if len(sys.argv) > 1:
        second_char = sys.argv[1][1].lower()
        if sys.argv[1][0] != "-":  # no flags
            filename = sys.argv[1]
        elif second_char != "-":  # single letter flags
            if second_char == "h":
                usage()
        elif second_char == "-":  # word flags
            flag_1 = sys.argv[1][2:].lower()
            if flag_1 == "help":
                usage()
            elif flag_1 == "":
                pass
    else:
        filename = "code.txt"

    with open(filename, "r") as f:
        src_file = f.read()
    curses.wrapper(hacker.main, src_file)


if __name__ == "__main__":
    main()
