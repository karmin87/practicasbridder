file = open("fruits.txt")
content = file.read()
file.close()
print(content[:90])