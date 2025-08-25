import os

file_source = (input("Write You file source: ")) #You can add all file type source to check like xlsx, pdf, doc et. 
if os.path.exists(file_source):
    print("File Exist")
else:
    print("File not found")
