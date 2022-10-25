from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='hwctrl',
    version='0.1.0',
    description='Fan control based on temperature sensor',
    url='https://github.com/olekiar/hardware-control',
    author='Ole Kiær',
    author_email='ole.kiar@gmail.com',
    license='MIT',
    scripts=['hwctrl'],
    install_requires=required,
    )