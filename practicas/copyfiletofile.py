with open("fruits.txt") as file:
    content = file.read()

with open("fruits2.txt", "a") as file:
    file.write(content)