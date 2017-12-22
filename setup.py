try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(
    name = 'diffimg',
    packages = ['diffimg'], # this must be the same as the name above
    version = '0.1.3',
    description = 'Get the % difference in images + generate a diff image Edit',
    author = 'Nicolas Hahn',
    author_email = 'nicolas@stonespring.org',
    url = 'https://github.com/nicolashahn/python-image-diff',
    download_url = 'https://github.com/nicolashahn/python-image-diff/archive/0.1.3.tar.gz',
    keywords = ['diff', 'difference', 'image'],
    classifiers = [],
    install_requires = ['Pillow>=4.3'],
)
