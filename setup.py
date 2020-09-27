#!/usr/bin/env python

import setuptools

LICENSE = 'CC0(/drivers: GPL 3.0)'

if __name__ == "__main__":
    setuptools.setup(
name = "papertty",
        version = "0.1.6",
        author = "Jouko Strömmer",
        author_email = "jouko.strommer@iki.fi",
        description = ("Python module to render a TTY or VNC on e-ink"),
        url='https://github.com/joukos/PaperTTY',
        license=LICENSE,
        
        packages=setuptools.find_packages(),


        classifiers=[
            'Development Status :: 1 - Alpha',
            'License :: OSI Approved ::' + LICENSE,
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
        ],

        zip_safe=True,
        include_package_data=True,
    )
