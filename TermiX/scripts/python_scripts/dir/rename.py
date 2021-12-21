import os
def rename_files_main(folder_path,new_name,extension):
    cmd = 'python3 /home/richeshgupta/pro/TermiX/TermiX/scripts/python_scripts/dir/renaming_runnable.py --folder-path {folder_path} --new-name {new_name} --ends-with {extension} --suppress-warnings'
    cmd = cmd.format(folder_path=folder_path,new_name=new_name,extension=extension)
    os.system(cmd)

rename_files_main('/home/richeshgupta/test/html','aanjul','.txt')