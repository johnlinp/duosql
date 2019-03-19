import os
import platform
from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='duosql',
    version='0.1.2',
    description='An easy way to demo database transactions.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='johnlinp',
    author_email='johnlinp@gmail.com',
    url='https://github.com/johnlinp/duosql',
    license='New BSD License',
    python_requires='>=3.5',
    scripts=[
        'bin/duosql',
    ],
)
