#!/usr/bin/env python3

import curses


def _get_input(stdscr):
    try:
        char = stdscr.getch()
    except KeyboardInterrupt:
        return None
    if char == 27:
        return None
    return char


def _add_string(string, stdscr):
    try:
        stdscr.addstr(string, curses.color_pair(1))
    except curses.error:
        pass
    stdscr.refresh()


def main(stdscr, src_file):
    curses.start_color()
    curses.noecho()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)
    stdscr.scrollok(True)
    word_list = src_file.split(" ")
    CHUNK_LEN = 3
    word_list = [
        src_file[i : i + CHUNK_LEN] for i in range(0, len(src_file), CHUNK_LEN)
    ]
    iterator = 0
    while True:
        if _get_input(stdscr) is None:
            break
        _add_string(word_list[iterator], stdscr)
        iterator = iterator + 1 if iterator < len(word_list) - 1 else 0
    return iterator


if __name__ == "__main__":
    with open("code.txt", "r") as f:
        src_file = f.read()
    curses.wrapper(main, src_file)
