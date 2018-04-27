
from setuptools import setup, find_packages
import os

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    name = 'scp_CM',
    version = '0.1.0',
    packages = find_packages(exclude=('tests',)),
    entry_points = {'scrapy': ['settings = scp_CM.settings']},
)