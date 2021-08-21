#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="pyScenicWeather",
    version="0.0.3",
    description="A Python wrapper around Scenic REST APIs",
    author='Conor Forde',
    author_email='conor@scenicdata.com',
    url="https://github.com/ScenicWeather/pyScenicWeather",
    packages=find_packages(),
    long_description="""PyScenicWeather is a client Python wrapper library for Scenic REST APIs. It allows quick and easy
     consumption of Scenic weather data from Python applications via a simple object model and in a human-friendly fashion.""",
    include_package_data=True,
    install_requires=['urllib3==1.26.6'],
    python_requires='>=3.7',
    classifiers=["License :: OSI Approved :: MIT License",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Natural Language :: English",
                 "Operating System :: OS Independent",
                 "Intended Audience :: Developers",
                 "Topic :: Software Development :: Libraries"],
    package_data={
        '': ['*.bz2', '*.md', '*.txt', '*.json']
    },
    keywords='scenic weather rest api climate forecast client pollution air-quality darksky',
    license='MIT'
)
