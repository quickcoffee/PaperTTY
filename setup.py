import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PaperTTY",
    version = "0.1.6",
    author = "Jouko Strömmer",
    author_email = "jouko.strommer@iki.fi",
    description = ("Python module to render a TTY or VNC on e-ink"),
    license = "CC0(/drivers: GPL 3.0)",
    keywords = "raspberry hat eink display driver",
    url = "https://github.com/joukos/PaperTTY",
    packages=['Pillow'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
