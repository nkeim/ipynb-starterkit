#!/usr/bin/python
"""
IPython Notebook startup script, by Nathan Keim

Takes as optional argument a directory where notebooks are stored.
Otherwise uses a default.
"""
import os, sys

## Configuration section

# Choose a default notebook directory, for when none is specified.
# Default default is '~/python-notebooks', i.e.
# the 'python-notebooks' directory inside your home directory.
# If you want it in your Documents folder, try something like
# '~/Documents/Python Notebooks'.
# If this directory doesn't exist, it will be created automatically.
notebook_dir = '~/python-notebooks'

# Name of IPython command. There should be no need to change this unless
# you find that you're starting the wrong version of IPython, e.g. one
# without notebook support.
ipython_command = 'ipython'

# IPython options. Again, experts only.
ipython_options = 'notebook --pylab=inline'

## End configuration section

args = sys.argv[1:]

if args:
    nbdir = args[0]
else:
    nbdir = os.path.expanduser(notebook_dir)
    if not os.path.isdir(nbdir):
        os.mkdir(nbdir)

command = ' '.join([ipython_command, ipython_options, \
                '--notebook-dir=' + nbdir])
print 'Starting IPython Notebook server with the command:'
print command

os.system(command)
