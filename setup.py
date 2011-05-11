from distutils.core import setup
import py2exe, sys, os

#setup(console=['myapp2.py']) 



sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 3}},
    windows = [{'script': "myapp2.py"}],
    zipfile = None,
)
