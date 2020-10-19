File_Read = open("Input.txt","r")
File_Write = open("Output.txt","w")

AllData = File_Read.readlines()

for j in AllData:
    text=list(j)
    for i in range(len(text)):
        if text[i] == "(":
            del text[i:len(text)]
            File_Write.write("".join(text) + "\n")
            break



File_Read.close()
File_Write.close()