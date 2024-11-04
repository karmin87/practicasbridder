def foo(character, filepath="fruits.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)