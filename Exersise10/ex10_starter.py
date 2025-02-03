# os module allows us to interact with the operating system
# glob module finds all the pathnames matching a specified pattern
# sys detects the operating system
import sys, glob, os

# Get the directory name
# if statement - sys.platform checks the operating system
# win32 will retrieve home directory from HOMEPATH and else: MAC
# hdir = home directory
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# print home directory name
print("Your home directory is:", hdir)

# Construct a portable wildcard pattern
# creates a file path depending on the operating system
# * = matches all files and directories inside the home directory
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
# glob.glob function finds all path names matching a specified pattern
list_filenames=glob.glob(pattern)
print(list_filenames)

# TODO: use os.path.getsize to find each file's size
# os.path.getsize() returns size of files in head directory
size_files=os.path.getsize(hdir)
print(size_files)

# TODO: Add a test to only display files that are not zero length
# presents file in list of filenames list and prints files that are more than zero length
# for loop that iterates over the list of file names - then the if statement uses variable size_files to check if each file in the list is greater than zero
for file in list_filenames:
    # if the statement is true, the file name will be printed.
    if size_files>0:
        print(file)

# alternative - gives true/false value but not a list of files thus previous test is preferred
# since the bool is greater than 0, the str is true
# files_notzero = os.path.getsize(hdir) > 0
# print(f"Files that are not zero length:", files_notzero)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

# Get only file names (remove directory path)
# (file) is used to only extract the file names from the directory
# for file in list_names loops through each file path in the list_filenames from the hdir
# [] used to establish a list
# in is a comparison, that means it has boolean values: true or false
# for and in are used together to create loop that iterates over a sequence - for defines the loop and in checks for membership in the sequence
# finds file name in list_filenames - removing the directory name
remove_directory_name=[os.path.basename(file) for file in list_filenames]
print(remove_directory_name)
