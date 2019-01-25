#!/usr/bin/env python

# Package meta-data.
NAME = 'kafkatool'
DESCRIPTION = 'Command line tool to manage Kafka topics, partitions and consumergroups'
URL = 'https://github.com/lstiebel/kafkatool'
EMAIL = 'l.stiebellehner@gmail.com'
AUTHOR = 'Lukas Stiebellehner'
REQUIRES_PYTHON = '>=3.7.0'
VERSION = '0.0.1'

# What packages are required for this module to be executed?
REQUIRED = [
    'pykafka', 'tabulate', 'argparse'
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    scripts=['kafkatool.py'],
    # $ optional: add publish support via git
    cmdclass={},
)