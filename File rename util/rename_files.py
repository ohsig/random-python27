import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Python27\prank")
    print(file_list)
    saved_path = os.getcwd()
    os.chdir(r"C:\Python27\prank")
    print("Current working directory is"+saved_path)
    #(2) for each file, rename the file
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
rename_files()
