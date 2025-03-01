from cast import *

print(proc.stdout.read().decode())
print(proc.stderr.read().decode())

input("Hit Enter to close...")