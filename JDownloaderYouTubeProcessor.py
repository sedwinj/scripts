#!python

"""
Author: Stephen Jones
Created 2022-ish
Last updated 2024-09-05

When downloading YouTube videos, JD2 also downloads other files and stores each
video and its related files in its own folder.

This script copies the videos from each folder in SOURCE to a single folder
designated by OUTPUT.
"""

import os
import shutil

OUTPUT = "./output"
SOURCE = "./input"
MP4 = ".mp4"


def prepareOutput():
    if os.path.exists(OUTPUT):
        shutil.rmtree(OUTPUT)

    os.mkdir(OUTPUT)


def processVideoFolder(folder):
    elements = [e for e in os.listdir(folder)]
    for e in elements:
        if MP4 not in e:
            continue

        shutil.copy2(
            os.path.join(folder, e),
            os.path.join(OUTPUT, ' '.join(e.split()[:-1]) + MP4)
        )


if __name__ == "__main__":
    prepareOutput()

    for name in os.listdir(SOURCE):
        path = os.path.join(SOURCE, name)
        if os.path.isdir(path):
            processVideoFolder(path)
