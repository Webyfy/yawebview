from os import path

from setuptools import find_packages, setup

_ROOT = path.abspath(path.dirname(__file__))

with open(path.join(_ROOT, "README.md")) as f:
    long_description = f.read()

setup(
    name="yawebview",
    version="0.2.6",
    description="Yet Another Webview Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Webyfy",
    author_email="info@webyfy.com",
    url="https://gitlab.com/webyfy/iot/e-gurukul/yawebview",
    maintainer="Webyfy",
    maintainer_email="info@webyfy.com",
    packages=find_packages(where="./src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Topic :: Software Development :: User Interfaces",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: User Interfaces",
    ],
)
