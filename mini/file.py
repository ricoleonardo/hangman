

### Reading
#file = open("FileHandling\doc.txt", "r")

#content = file.read()

#content = file.readline()

#content = file.readlines()
 
#print(content)
### Writing

#file = open("FileHandling\doc.txt", "w")

#file.write("Data") 

### Append
#file = open("FileHandling\doc.txt", "a")

#file.write("\nData 1")

#change the folder

#file = open("doc.txt", "w")

#file.write("\nRerun")

#Reading Writing

#file = open("doc1.txt", "r+") # no existing data

#file.write("\nRerun")

#file = open("doc1.txt", "w+")

#file.write("\nThis is W PLUS")

# Append

#file = open("doc1.txt", "a+")

#file.write("\n New Line")
#file.seek(0) # to read the first line
#content = file.read()

#print(content)


# RECOMMENDATION

#file = open("doc1.txt", "a+")

#file.write("\n New Line")
#file.seek(0) # to read the first line
#content = file.read()

#print(content)

#file.close()

#while open("doc1.txt", "w+") as file:
#    file.write("\n New Line")
#    file.seek(0) # to read the first line
#    content = file.read()
#
#    print(content)

filename = "doc1.txt"
while open(filename, "w+") as file:
    file.write("\n New Line")
    file.seek(0) # to read the first line
    content = file.read()

    print(content)
