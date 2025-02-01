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
# var = os.environ['HOME']
# print home directory name
print(f"Your home directory is:", hdir)

# Construct a portable wildcard pattern to match ALL files in the home directory
# find out why we use the asterisk (the code doesn't work without it)
pattern = os.path.join(hdir, "*")

# glob.glob is used to find all the files
list_filenames = glob.glob(pattern)
# print the list of files
print("List of files", list_filenames)

# get the sizes of the files
size_files = os.path.getsize(hdir)
print("Size of Files", size_files)

remove_dirname = os.path.basename(hdir)
print(list_filenames)