try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
setup(
    name = 'diffimg',
    packages = ['diffimg'], # this must be the same as the name above
    version = '0.1.6',
    description = 'Get the % difference in images + generate a diff image',
    author = 'Nicolas Hahn',
    author_email = 'nicolas@stonespring.org',
    url = 'https://github.com/nicolashahn/python-image-diff',
    download_url = 'https://github.com/nicolashahn/python-image-diff/archive/v0.1.6.tar.gz',
    keywords = ['diff', 'difference', 'image'],
    classifiers = [],
    install_requires = ['Pillow>=4.3'],
)
