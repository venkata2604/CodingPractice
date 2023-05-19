# web source: module>index>pathlib
# pathlib is a object oriented file system paths
from pathlib import Path
# We can use an absolute of relative path
# absolute starts with root of index. example "c:\Program Files\Microsoft

path = Path("examplepackagedirectory")
print(path.exists())
# we can make a directory by calling "path.mkdir()
for file in path.glob('*'): # we can search files in the directory *.* gives all files *.py gives all python files
    print(file)