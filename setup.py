import sys
import os
import re 

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

# __version__ = find_version("bin/clearbit")

print(find_version("bin/clearbit"))

# config = {
#     'description': 'use clearbit api from command line.',
#     'author': 'Austin Ogilvie',
#     'keywords': 'clearbit command line tool',
#     'author_email': 'a@yhathq.com',
#     'version': '0.2',
#     'install_requires': ['nose', 'docopt', 'requests', 'clearbit'],
#     'packages': ['clearbitcli'],
#     'include_package_data': True,
#     'scripts': ['bin/clearbit'],
#     'zip_safe': False,
#     'name': 'clearbitcli',
#     'license': 'MIT'
# }

# setup(**config)
