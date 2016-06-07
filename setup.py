#!python
import sys, os, subprocess

# prepare setuptools environment
try:
    from setuptools import setup, find_packages
except ImportError:
    print "Could NOT import setuptools, try ez_setup..."
    try:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
    except ImportError:
        print "Could NOT import either setuptools or ez_setup, GIVE UP!"
        print "Download ez_setup.py e.g. " \
            "from https://bootstrap.pypa.io/ez_setup.py,"
        print "place it in the same directory as setup.py, and try again... "
        sys.exit(1)

setup(
    # Application name:
    name="MCNPmanager",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Ian Postuma",
    author_email="ian.postuma@gmail.com",

    # Packages
    packages = find_packages(),
    data_files=['MCNPmanager/cards', ["MCNPmanager/cards/alltogetherold.part",
                                "MCNPmanager/cards/alltogether.part",
                                "MCNPmanager/cards/cells.part",
                                "MCNPmanager/cards/materials.part",
                                "MCNPmanager/cards/parameters.part",
                                "MCNPmanager/cards/source.part",
                                "MCNPmanager/cards/surfaces.part",
                                "MCNPmanager/cards/tallies.part",
                                "MCNPmanager/cards/traslations.part"]],
    # Include additional files into the package
    include_package_data=True,

    # Details
    # url="http://pypi.python.org/pypi/MyApplication_v010/",
    url="http://ianpostuma.com",

    #
    # license="LICENSE.txt",
    description="""MCNP file project Manager
    This program aims to help developing and managing an MCNP simulation""",

    scripts=['bin/MCNPmanager'],

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    #  install_requires=[
    #      "shutil", "sys", "argparse", "string", "os"
    #  ],
)
