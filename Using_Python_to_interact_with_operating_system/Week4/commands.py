import subprocess 
from IPython.utils.capture import capture_output

def runprocess(command, filename):
    test = subprocess.run([command, filename], capture_output=True, shell=True)
    return "return code is {}, stdout is {}, decoded string is {} and stderr is {}".format(test.returncode, test.stdout, test.stdout.decode().split(), test.stderr)

def runprocess1(command):
    test = subprocess.run([command], capture_output=True, shell=True)
    return "return code is {}, stdout is {}, decoded string is {} and stderr is {}".format(test.returncode, test.stdout, test.stdout.decode().split(), test.stderr)

print(runprocess("rm", "does_not_exist"))

print(runprocess1("atom"))

print(runprocess1("path"))
