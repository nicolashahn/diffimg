try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
VERSION = "0.2.3"
setup(
    name="diffimg",
    packages=["diffimg"],  # this must be the same as the name above
    version=VERSION,
    description="Get the % difference in images + generate a diff image",
    author="Nicolas Hahn",
    author_email="nicolas@stonespring.org",
    url="https://github.com/nicolashahn/python-image-diff",
    download_url="https://github.com/nicolashahn/python-image-diff/archive/v{}.tar.gz".format(
        VERSION
    ),
    keywords=["diff", "difference", "image", "test", "testing"],
    classifiers=[],
    install_requires=["Pillow>=4.3"],
)
