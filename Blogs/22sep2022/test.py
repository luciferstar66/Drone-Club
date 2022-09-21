import os

#ITSDB
#1,1262
images = []
text = []
for index in range(1,3):
    images.append(os.path.join("ITSDB",str(index)+".jpg"))
    text.append(os.path.join("ITSDB",str(index)+".txt"))

with open(text[0],'r') as file:
    lines = file.readline()
    lines.rstrip('\n')
    print(lines)
