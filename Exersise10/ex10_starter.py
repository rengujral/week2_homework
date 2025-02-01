import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
list_filenames=glob.glob(pattern)
print(list_filenames)
# TODO: use os.path.getsize to find each file's size
size_files=os.path.getsize(hdir)
print(size_files)
# TODO: Add a test to only display files that are not zero length
for file in list_filenames:
    if os.path.isfile(file):  # Check if it's a file (not a directory)
        size = os.path.getsize(file)
        if size > 0:  # Only display files with size greater than 0
            print(f"{file}: {size} bytes")
# list_filenames=glob.glob(pattern)>0
# print(list_filenames)
# files_notzero=os.path.getsize(hdir)>0
# print(files_notzero)
# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
remove_directory_name=[os.path.basename(file) for file in list_filenames]
print(remove_directory_name)
