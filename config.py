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

def default_dir_fallback():

    system.stdout.write("Unable to make required folder in home directory, falling back to root")
    file_dest = DEFAULT_DIR

    if DEFAULT_DIR == "~" or DEFAULT_DIR is None:
        sys.exit("Unable to use root or default directory, exiting...")

        if not os.path.isdir(file_dest+"/output"):
            try:
                os.mkdir(file_dest)
            except OSError:
                sys.exit("Unable to create output folder in root directory, exiting...")

# path variables

DEFAULT_DIR = os.path.normpath(os.path.expanduser('~'))
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_LOCATION = os.path.normpath(os.path.join(ROOT_DIR, "data/cedict_ts.u8"))

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
    if DEFAULT_DIR == "~" or DEFAULT_DIR is None:
        system.stdout.write("Unable to access home directory falling back to root.")
        file_dest = ROOT_DIR+"/output"
        if not os.path.isdir(file_dest):
            os.mkdir(file_dest)
        is_path_writable(file_dest)
    else:
        file_dest = DEFAULT_DIR
        is_path_writable(file_dest)
elif file_dest is None:
    file_dest = ROOT_DIR+"/output"
    if not os.path.isdir(file_dest):
        # if os.mkdir fails it should raise an OSError
        try:
            os.mkdir(file_dest)
        except OSError:

            sys.stdout.write("Unable to make required directory, falling back to root")
            file_dest = DEFAULT_DIR

elif not os.path.isabs(file_dest):
    file_dest = os.path.join(ROOT_DIR, file_dest)
    is_path_writable(file_dest)
