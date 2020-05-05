#!/usr/bin/env python3

import os

# the os.environ.get method checks the specified environment variable and retrieves its associated value; if it has no value or the specified variable
# was not defined, we return an empty string
print("Path: " + os.environ.get("Path", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

# this defines the FRUIT environment variable and sets Pineapple as its value.
# NOTE: this is done by using the export command and leaving no space between the FRUIT variable, the = sign and the Pineapple value
# the export keyword tells the shell that we want the value we set to be seen by any commands that we call
# export FRUIT=Pineapple
