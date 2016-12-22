### Read and write file
TextfileName = input("What is the name of the file: ")

file = open(TextfileName+".txt", "w")

fileText = input("Text: ")
file.write(fileText)
      
