#!/usr/bin/env python3

import curses, sys
import hacker


def usage():
    print(
        f"Usage: {sys.argv[0]} [options] [file]\n"
        "Options:\n"
        "  -h, --help\t\t\tDisplay this help message\n"
        "  -d, --default-colors\t\tUse default colors\n"
        "  -c, --chunk-length 3\t\tSet chunk length"
    )
    exit()


def main():
    if len(sys.argv) > 1:
        second_char = sys.argv[1][1].lower()
        if sys.argv[1][0] != "-":  # no flags
            filename = sys.argv[1]
        elif second_char != "-":  # single letter flags
            if second_char == "h":
                usage()
            elif second_char == "d":
                hacker.use_default_colors = True
            elif second_char == "c":
                try:
                    hacker.chunk_length = int(sys.argv[2])
                except ValueError:
                    print("Invalid chunk length")
                    exit()
                except IndexError:
                    print("Chunk length not specified")
                    exit()
                if hacker.chunk_length < 1:
                    print("Chunk length must be greater than 0")
                    exit()
        elif second_char == "-":  # word flags
            flag_1 = sys.argv[1][2:].lower()
            if flag_1 == "help":
                usage()
            elif flag_1 == "default-colors":
                pass
            elif flag_1 == "chunk-length":
                pass
    else:
        filename = "code.txt"

    with open(filename, "r") as f:
        src_file = f.read()
    curses.wrapper(hacker.main, src_file)


if __name__ == "__main__":
    main()
