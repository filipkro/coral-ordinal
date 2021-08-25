import setuptools
from setuptools import setup
import os
import sys
from pkg_resources import DistributionNotFound, get_distribution

def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None

_here = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(_here, 'coral_ordinal', 'version.py')) as f:
    exec(f.read(), version)


with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_deps = ['numpy']

if get_dist('tensorflow') is None and get_dist('tensorflow_gpu') is None and get_dist('tensorflow-cpu') is None:
    print('Adding tensorflow>=2.2 to dependencies..')
    install_deps.append('tensorflow>=2.2')
else:
    print('Tensorflow already installed')


setup(
    name = 'coral-ordinal',
    url = 'https://github.com/filipkro/coral-ordinal',
    author = 'Chris Kennedy, Stephen Matthews, (Filip Kronström)',
    author_email = 'filip.kronstrom@gmail.com',
    packages = setuptools.find_packages(),
    install_requires = install_deps,
    version = version['__version__'],
    long_description_content_type = "text/markdown",
    license = 'MIT',
    description = 'Tensorflow Keras implementation of CORAL ordinal regression output layer, loss, activation, and metrics',
    long_description = long_description,
    python_requires = '>=3.6',
)
