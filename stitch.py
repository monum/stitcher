#!/usr/bin/env python

"""
This script concatenates a series of MP4 files.
"""

import glob
import os
import subprocess

# Create a sorted list of MP4 files in the "files" directory.

file_names = glob.glob("./files/*.mp4")

file_names.sort(key=os.path.basename)

# Create a text file listing all the MP4 files in the "files" directory.

with open("./file_names.txt", "w") as f:
    for i in range(len(file_names)):
        if (i < len(file_names)-1):
            f.write("file '" + file_names[i] + "'\n")
        else:
            f.write("file '" + file_names[i] + "'")

# Concatenate all of the MP4 files found.

subprocess.call(['./ffmpeg', '-f', 'concat', '-safe', '0', '-i', './file_names.txt', '-c', 'copy', './files/final.mp4'])
