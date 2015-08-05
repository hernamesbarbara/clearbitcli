try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'use clearbit api from command line.',
    'author': 'Austin Ogilvie',
    'keywords': 'clearbit command line tool',
    'author_email': 'a@yhathq.com',
    'version': '0.1',
    'install_requires': ['nose', 'docopt', 'requests', 'clearbit'],
    'packages': ['clearbitcli'],
    'include_package_data': True,
    'scripts': ['bin/clearbit'],
    'zip_safe': False,
    'name': 'clearbitcli',
    'license': 'MIT'
}

setup(**config)
