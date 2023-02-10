import pathlib
import os

#print current directly using pathlib module
print(pathlib.Path().absolute())

#using os module
print(os.path.abspath(os.getcwd()))