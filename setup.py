from setuptools import setup, find_packages

setup(
    name='Andimointestprojekt',
    version='0.1.0',
    packages=find_packages(),
    instsall_requires=[
        'numpy'],
    author='Andivscodemachine',
    description='Andimointestprojekt is a test project for Python package structure and imports.',
    long_description=open('README.md').read(),
    python_requires='>=3.6'
)
