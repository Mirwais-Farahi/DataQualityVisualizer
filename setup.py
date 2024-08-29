from setuptools import setup, find_packages

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

)