import os
import sys

# upload to pypi
os.chdir('../../..')
os.system('%s setup.py sdist --formats=gztar --with-cython --fail-on-error' % sys.executable)