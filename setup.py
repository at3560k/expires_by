#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="John Q Doe",
    author_email="github.com@maelstrm.cotse.net",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        # Perhaps later...
        # 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="A dependency that goes bad at a certain time",
    install_requires=requirements,
    # license="GNU General Public License v3",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="expires_by",
    name="expires_by",
    packages=find_packages(include=["expires_by", "expires_by.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/at3560k/expires_by",
    version="0.1.0",
    zip_safe=False,
)
