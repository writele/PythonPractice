import os
def rename_files():
        #1 get file names
        file_list = os.listdir("/Users/elepalmer/Python/prank")
        print(file_list)
        saved_path = os.getcwd()
        print("Current path is: "+saved_path)
        os.chdir("/Users/elepalmer/Python/prank")
        #2 rename files
        for file_name in file_list:
            print("Old Name is "+file_name)
            print("New name is "+file_name.translate(None,"0123456789"))
            os.rename(file_name,file_name.translate(None,"0123456789"))
        os.chdir(saved_path)
rename_files()

