from setuptools import setup

setup(name='brightsign-MRSSMaker',
      version='0.0.1',
      description='given a directory of jpegs, generates a brightsign compatible MRSS feed',
      url='http://github.com/riordan/brightsign-py-mrss-maker',
      author='David Riordan',
      author_email='dr@daveriordan.com',
      license='Apache-2.0',
      packages=['mrssMaker'],
      install_requires=["six"],
      entry_points={
        'console_scripts': [
            'mrssMaker=mrssMaker:generateMRSS',
        ],
    },
      zip_safe=False)
