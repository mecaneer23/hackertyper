#!/usr/bin/env python3

import curses


def main(stdscr, src_file, chunk_len):
    curses.start_color()
    curses.noecho()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    stdscr.scrollok(True)
    word_list = src_file.split(" ")
    word_list = [
        src_file[i : i + chunk_len] for i in range(0, len(src_file), chunk_len)
    ]
    iterator = 0
    while True:
        try:
            if stdscr.getch() == 27:
                break
        except KeyboardInterrupt:
            break
        try:
            stdscr.addstr(word_list[iterator], curses.color_pair(1))
        except curses.error:
            pass
        stdscr.refresh()
        iterator = iterator + 1 if iterator < len(word_list) - 1 else 0
    return iterator


def get_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--chunk-length",
        "-c",
        type=int,
        default=3,
        help="Length of a given chunk in characters.",
    )
    parser.add_argument(
        "filename", type=str, nargs="?", default="code.txt", help="Source file"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    with open(args.filename, "r") as f:
        curses.wrapper(main, f.read(), args.chunk_length)
