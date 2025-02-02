import sys, glob, os

# Get the directory name
# sys.platform checks the operating system
# win32 will retrieve home directory from HOMEPATH
# hdir = home directory
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
# creates a file path depending on the operating system
# * = matches all files and directories inside the home directory
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
list_filenames=glob.glob(pattern)
print(list_filenames)
# glob.glob function finds all path names matching a specified pattern

# TODO: use os.path.getsize to find each file's size
size_files=os.path.getsize(hdir)
print(size_files)
# os.path.getsize() returns size of files in head directory

# TODO: Add a test to only display files that are not zero length
# presents file in list of filenames list and prints files that are more than zero length
for file in list_filenames:
    if size_files>0:
        print(file)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
# for and in are use together to create loop that iterates over a sequence - for defines the loop and in checks for membership in the sequence
# finds file name in list_filenames - removing the directory name
remove_directory_name=[os.path.basename(file) for file in list_filenames]
print(remove_directory_name)
