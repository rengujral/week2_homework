# os module allows us to interact with the operating system
# use either of these to import modules
# sys detects the operating system
import os, sys, glob

# use an if statement to check your operating system
if sys.platform == "win32":
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# or use this if you already know your operating system
# print home directory name
print("Your home directory is:", hdir)

# Construct a portable wildcard pattern to match ALL files in the home directory
pattern = os.path.join(hdir, "*")

# glob.glob is used to find all the files
list_filenames = glob.glob(pattern)
# print the list of files
print("List of files:", list_filenames)

# get the sizes of the files in hdir
size_files = os.path.getsize(hdir)
# print the size of files
print("Size of Files:", size_files)

files_notzero = os.path.getsize(hdir) > 0
print(f"Files that are not zero length:", files_notzero)

# Get only file names (remove directory path)
# (file) is used to only extract the file names from the directory
# for file in list_names loops through each file path in the list_filenames from the hdir
# [] used to establish a list
remove_dirname = [os.path.basename(file) for file in list_filenames]
print("List of files (directory removed):", remove_dirname)