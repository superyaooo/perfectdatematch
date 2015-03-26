try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Perfect match for dates',
    'author': 'Yao Wang',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'superyaooo@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['perfect_match'],
    'scripts': ['bin/runner.py'],   #installs the script
    'name': 'perfect date match'

}

setup(**config)
