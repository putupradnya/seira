from setuptools import setup, find_packages
import codecs
import os


VERSION = '1.0.0'
DESCRIPTION = 'SEIRA: SEISMIC DATA PROCESSING'
LONG_DESCRIPTION = 'A package that build for seismic refraction tomography and multichannel analysis of surface wave (MASW) data processing'

# Setting up
setup(
    name="seira",
    version=VERSION,
    author="Putu Pradnya Andika & Tedi Yudistira",
    author_email="<putuandhika@hotmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib'],
    keywords=['python', 'seismic refraction tomography', 'masw'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: > 3.7",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)