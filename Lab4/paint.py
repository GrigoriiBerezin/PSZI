#!/usr/bin/env python3
import os


def handle_func():
    KEY = "thatsakey"
    act = ''

    while act != "exit":
        act = input("Write your action (show data, open access, exit): ").lower()

        if act == 'show data':
            key = input("Enter the key: ")
            if key == KEY:
                with open("sys.tat", "r") as file:
                    for line in file.readlines():
                        print(line)
            else:
                print("Wrong key!")
        elif act == 'open access':
            key = input("Enter the key: ")
            if key == KEY:
                os.chmod("sys.tat", 0o666)
            else:
                print("Wrong key!")


if __name__ == '__main__':
    handle_func()
