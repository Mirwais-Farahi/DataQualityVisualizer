from setuptools import setup, find_packages
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='DataQualityVisualizer',
    version='0.1',
    packages=find_packages(),
    author='Mirwais Farahi',
    author_email='waisfarahi@example.com',
    description='Python module for automated data quality assurance and visualization to detect outliers and anomalies.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mirwais-farahi/DataQualityVisualizer',
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
    install_requires=["pandas", "numpy"],
)