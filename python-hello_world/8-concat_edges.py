#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming"
str = str[str.find("object"):str.find("Python") + len("Python")]
print(str)
