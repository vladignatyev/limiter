# coding: utf-8
from setuptools import setup, find_packages

setup(name = "limiter",
    author="Vladimir Ignatev",
    author_email="ya.na.pochte@gmail.com",
    url="https://github.com/vladignatyev/limiter",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    test_suite='nose.collector'
)