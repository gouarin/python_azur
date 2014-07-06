#!/bin/sh
ipython nbconvert --debug $1 --to slides --post serve --config slides_config.py 

