# -dir1
# --a.py
# --<here>
# -b.py

import a

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('__file__'))))
import b
