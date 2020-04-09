# !/usr/bin/env python3

import sys
import subprocess
import shutil


def replace_name(file):
    with open(file, "r") as f:
        contents = f.readlines()
        for line in contents:
            old_line_value = line.strip()
            print(old_line_value)
            line = line.replace("jane", "jdoe")
            # source = "/home/student-00-8598566d49b2/data" + old_line_value
            # dest = "/home/student-00-8598566d49b2/data" + line
            # subprocess.run("mv", command, shell=True)
            shutil.move(old_line_value, line)


if __name__ == "__main__":
    replace_name(sys.argv[1])
