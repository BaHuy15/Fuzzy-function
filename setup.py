from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import setuptools

_VERSION_ = '0.3.2'

REQUIRED_PACKAGES = [
]

DEPENDENCY_LINKS = [
]

setuptools.setup(
    name='warmup_scheduler',
    description='Fuzzy logic by Bhuy',
    install_requires=REQUIRED_PACKAGES,
    dependency_links=DEPENDENCY_LINKS,
    url='https://github.com/BaHuy15/Fuzzy-function',
    package_dir={},
    packages=setuptools.find_packages(exclude=['train']),
)
