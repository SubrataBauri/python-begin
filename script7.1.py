file=open('example.txt', 'r')
print(type(file))

content=file.read()
print(content)

contentLines=file.readlines()
print(contentLines)

print(file.seek(0))
contentLines=file.readlines()
print(contentLines)

content=[i.rstrip("\n") for i in contentLines]
print(content)

file.close()