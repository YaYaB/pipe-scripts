from setuptools import setup
from setuptools import find_packages


setup(name='pipe_scripts',
      version='0.0.1',
      description='Python binding for DeepDetect',
      author='YaYaB',
      author_email='bezzayassine@gmail.com',
      url='https://github.com/YaYaB/pipe-scripts',
      download_url='https://github.com/YaYaB/pipe-scripts',
      license='MIT',
      classifiers=['License :: Apache License v2.0',
                   'Programming Language :: Python',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   ],
      install_requires=[],
      extras_require={},
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'pipe-scripts=pipe_scripts.pipe_scripts:main',
          ]},

      )
