# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='DataQualityVisualizer',
    version='0.1',
    packages=find_packages(),
    author='Mirwais Farahi',
    author_email='waisfarahi@example.com',
    description='Python module for automated data quality assurance and visualization to detect outliers and anomalies.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mirwais-farahi/DataQualityVisualizer',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    packages=["data_quality_visualizer"],
    include_package_data=True,
    install_requires=["pandas","numpy"],
    entry_points={
        'console_scripts': [
            'dataqualityvisualizer=main:main',
        ],
    }
)