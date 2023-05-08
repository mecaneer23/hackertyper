#!/usr/bin/env python3

import curses, sys


def usage():
    print(
        f"Usage: {sys.argv[0]} [options] [file]\n"
        "Options:\n"
        "  -h, --help\t\t\tDisplay this help message\n"
        "  -d, --default-colors false\t\tUse default colors\n"
        "  -c, --chunk-length 3\t\tSet chunk length"
    )
    exit()


def main(stdscr, src_file, use_default_colors=True, chunk_length=3):
    curses.start_color()
    curses.noecho()
    if use_default_colors:
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)
    else:
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.scrollok(True)
    word_list = src_file.split(" ")
    CHUNK_LEN = chunk_length
    word_list = [
        src_file[i : i + CHUNK_LEN] for i in range(0, len(src_file), CHUNK_LEN)
    ]
    iterator = 0
    while True:
        try:
            char = stdscr.getch()
        except KeyboardInterrupt:
            break
        if char == 27:
            break
        try:
            stdscr.addstr(word_list[iterator], curses.color_pair(1))
        except curses.error:
            pass
        stdscr.refresh()
        iterator = iterator + 1 if iterator < len(word_list) - 1 else 0
    return iterator


def parse_args():
    use_default_colors = True
    chunk_length = 3
    filename = "code.txt"
    if len(sys.argv) > 1:
        second_char = sys.argv[1][1].lower()
        if sys.argv[1][0] != "-":  # no flags
            filename = sys.argv[1]
        elif second_char != "-":  # single letter flags
            if second_char == "h":
                usage()
            elif second_char == "d":
                try:
                    if sys.argv[2] == "false":
                        use_default_colors = False
                except IndexError:
                    print("Error: No value for flag")
                    exit()
            elif second_char == "c":
                try:
                    chunk_length = int(sys.argv[2])
                except ValueError:
                    print("Invalid chunk length")
                    exit()
                except IndexError:
                    print("Chunk length not specified")
                    exit()
                if chunk_length < 1:
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

    with open(filename, "r") as f:
        src_file = f.read()
    curses.wrapper(main, src_file, use_default_colors=use_default_colors, chunk_length=chunk_length)


if __name__ == "__main__":
    parse_args()
