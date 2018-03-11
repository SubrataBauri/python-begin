file=open("example1.txt", "w")
file.write("Written Line 1\n")

file.write("Line 2")

file.close()

newfile = open("example0.txt", "w")
list=["Line 1", "Line 2", "Line 3"]
for item in list:
    newfile.write(item + "\n")
newfile.close()