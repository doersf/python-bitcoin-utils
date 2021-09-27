from setuptools import setup
from bitcoinutils import __version__

#with open('requirements.txt') as f:
#    requirements = f.read().splitlines()

#install_reqs = parse_requirements('requirements.txt', session=False)
#requirements = [str(ir.req) for ir in install_reqs]

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
          'base58==2.1.0',
          'ecdsa==0.17.0',
          'sympy==1.3'
      ],
      packages=['bitcoinutils'],
      #package_data={
      #    'bitcoinutils': ['requirements.txt']
      #},
      #include_package_data=True,
      zip_safe=False
     )

