from setuptools import setup,find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['test*']),
    license="MIT",
    install_requires =['numpy'],
    description="Python package example",
    long_description=open('README.md').read(),
    url='github......',
    author="Andani",
    author_email="alex@gmail.com"

)