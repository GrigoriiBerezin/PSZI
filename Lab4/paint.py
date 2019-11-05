#!/usr/bin/env python3
import os
import platform


def handle_func():
    KEY = "thatsakey"
    act = ''
    info = '\n'.join(["OS name: " + os.name,
                      "System: " + platform.system(),
                      "Release: " + platform.release(),
                      "Network name: " + platform.node(),
                      "Version: " + platform.version(),
                      "Processor: " + platform.processor()])

    while act != "exit":
        act = input("Write your action (show data, open access, exit): ").lower()

        if act == 'show data':
            key = input("Enter the key: ")
            if key == KEY:
                print(info)
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
