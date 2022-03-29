import setuptools

_VERSION = '0.3.2'

REQUIRED_PACKAGES = [
]

DEPENDENCY_LINKS = [
]

setuptools.setup(
    name='warmup_scheduler',
    version=_VERSION,
    description='Fuzzy logic by Bhuy',
    install_requires=REQUIRED_PACKAGES,
    dependency_links=DEPENDENCY_LINKS,
    url='https://github.com/BaHuy15/Fuzzy-function',
    package_dir={},
    packages=setuptools.find_packages(exclude=['tests']),
)
