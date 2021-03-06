import setuptools
from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='litego',
    packages=['litego'],
    version='0.1.0',
    description='Python library for the litego API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Olexandr Shalakhin',
    author_email='olexandr@shalakhin.com',
    url='https://github.com/litegoio/litego-python',
    download_url='https://github.com/litegoio/litego-python/archive/0.1.0.tar.gz',
    keywords=['testing', 'logging', 'example'],
    requires=['requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
