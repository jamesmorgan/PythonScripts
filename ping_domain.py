#!/usr/bin/python

####################################
## Used to ping domains in python ##
####################################

import subprocess

host = "www.google.com"

ping = subprocess.Popen(
# Linux    ["ping", "-c", "4", host],
    ["ping", "-n", "4", host],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, error = ping.communicate()
print out