ipynb-starterkit
================

These are some launcher scripts, including a Mac application, to let beginners
easily start the IPython Notebook server. They don't offer much flexibility,
but offer a shortcut to getting started with the Notebook interface, once
you've installed a suitable Python distribution.

If you're not on a Mac, check out the ipnblaunch.py script.

Installation
------------

I recommend you copy the "Start IPython Notebook Server" app to your
Applications folder, or somewhere that it's easy to find. Give it a different
name if you like.

Depending on the way your Mac is configured, you may be prohibited from running
the app when you double-click on it, because it's from an untrusted source.
Instead, right-click and choose "Open" from the menu that appears. This will
give you the option to trust the application. You will not be asked again.

Usage
-----

Notebooks are stored in the "python-notebooks" folder in your home directory.
It is created if it doesn't exist.

The launcher assumes that your IPython command is just "ipython", which should
be true if you installed the Enthought Python Distribution. Otherwise you'll
have to make changes (see below).

Configuration
-------------

If you want to change the default behavior of the launcher (or just see how it
works), you can edit the Python code. Right-click on the application and choose
"Show Package Contents", then navigate to Contents -> MacOS -> startup.command.
Open this in any text editor (e.g. TextEdit, though preferably something like
TextWrangler).


-- Nathan Keim, 12/14/2012
