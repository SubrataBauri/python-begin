with open("example.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.write("\n Line new hahaha")

print(content)