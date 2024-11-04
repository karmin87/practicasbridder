myfile = open("fruits.txt")
content = myfile.read()

with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)
myfile.close()