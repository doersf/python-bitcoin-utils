from setuptools import setup
from bitcoinutils import __version__

with open('README.rst') as readme:
    long_description = readme.read()

setup(name='bitcoin-utils-fork-minimal',
      version=__version__,
      description='Bitcoin utility functions',
      long_description=long_description,
      author='Konstantinos Karasavvas',
      author_email='kkarasavvas@gmail.com',
      url='https://github.com/doersf/python-bitcoin-utils',
      license='AGPLv3',
      keywords='bitcoin library utilities tools',
      install_requires=[
          'base58>=2.1,<2.2',
          'ecdsa==0.18.0',
          'sympy>=1.7,<2.0'
      ],
      packages=['bitcoinutils'],
      zip_safe=False
     )

