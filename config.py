# config.py

import os
import sys

def is_path_writable(path):
    if os.path.isdir(path) and os.access(path, os.W_OK):
        sys.stdout.write("Output will be directed to: {} \n".format(path))
        sys.stdout.flush()
    else:
        sys.exit("The directory: {}, either does not exist or lacks write permissions".format(path))
    return False

# path variables

default_dir = os.path.normpath(os.path.expanduser('~'))
root_dir = os.path.dirname(os.path.realpath(__file__))
data_location = os.path.normpath(os.path.join(root_dir, "data/cedict_ts.u8"))

# Assign CLI arguments to values here.
# It should go something like this:
# python main.py www.sampleurl.com [optional destination]

# If sys.argv[x] doesn't exist it should throw an IndexError

c_url = file_dest = None

try:
    c_url = sys.argv[1]
    file_dest = sys.argv[2]
except:
    if (c_url is None):
        sys.exit("Please provide a uri for the second argument \n")
    elif (file_dest is None):
        sys.stdout.write("Using default directory for resultant file location. \n")

# Check to see if the path is writable, exiting via sys.exit() if unable.

if not file_dest is None and os.path.isabs(file_dest):
    is_path_writable(file_dest)
elif file_dest is None:
    if default_dir == "~" or default_dir is None:
        system.stdout.write("Unable to access home directory falling back to root.")
        file_dest = root_dir+"/output"
        if not os.path.isdir(file_dest):
            os.mkdir(file_dest)
        is_path_writable(file_dest)
    else:
        file_dest = default_dir
        is_path_writable(file_dest)

elif not os.path.isabs(file_dest):
    file_dest = os.path.join(root_dir, file_dest)
    is_path_writable(file_dest)

# Variable declarations
