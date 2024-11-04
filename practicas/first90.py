with open("fruits.txt") as file:
    content = file.read()
    
    with open("first90.txt", "w") as file:
        file.write(content[:90])
