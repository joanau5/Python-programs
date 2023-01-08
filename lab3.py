#lab3.py

# Joana Ugarte
# joanau@uci.edu
# 44875730

from pathlib import Path

p1 = Path(".") / "1/12"

if not p1.exists(): # check to see if temp_dir exists
  p1.mkdir() # if temp_dir does not exist, create it

p1 = p1.joinpath("pynote.txt") # append a file name to the current path

if not p1.exists(): # check to see if temp_file.txt exists
  p1.touch() # if temp_file.txt does not exist, create it

print(p1.name) # get the name of the object (file name or directory name)
print(p1.suffix) # get the suffix (.py, .doc, etc) of the file object



