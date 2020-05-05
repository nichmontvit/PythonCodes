#!/usr/bin/env python3
import os
import subprocess

# we make a copy of the OS environ dictionary containing the current environment variables
my_env = os.environ.copy()

# we add a new directory (/opt/myapp/) to the Path variable 
my_env["Path"] = os.pathsep.join(["/opt/myapp/", my_env["Path"]])

result = subprocess.run(["myapp"], env=my_env)