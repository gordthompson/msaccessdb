import os
import re

import setuptools

v = open(os.path.join(os.path.dirname(__file__), 'msaccessdb', '__init__.py'))
VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(v.read()).group(1)
v.close()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="msaccessdb",
    version=VERSION,
    author="Gord Thompson",
    author_email="gord@gordthompson.com",
    license='Apache-2.0',
    description="Create a new empty Access database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gordthompson/msaccessdb",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    keywords='Microsoft Access',
)
