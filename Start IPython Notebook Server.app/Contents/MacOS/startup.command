#!/bin/sh
mkdir -p "$HOME/python-notebooks"
/Library/Frameworks/EPD64.framework/Versions/7.3/bin/ipython notebook --notebook-dir="$HOME/python-notebooks" --pylab=inline
