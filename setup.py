from codecs import open
from os import name as os_name
from os import path

from setuptools import setup

VERSION = "0.3.7"  # using semantic versioning

here = path.abspath(path.dirname(__file__))


def install_requires():
    if os_name == "nt":
        return ["win10toast"]
    return []


def readme():
    with open(path.join(here, "README.rst"), encoding="utf-8") as f:
        return f.read()


with open(path.join(here, "inappropriate_notifications", "version.py"), "w") as f:
    f.write(f"VERSION = '{VERSION}'")

setup(
    name="inappropriate-notifications",
    version=VERSION,
    description="Display inappropriate notifications at random intervals",
    long_description=readme(),
    long_description_content_type="text/x-rst",
    license="MIT",
    entry_points={
        "console_scripts": [
            "inappropriate-notifications=inappropriate_notifications.command_line:main"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Topic :: Artistic Software",
    ],
    keywords="notifications notify inappropriate present",
    url="https://github.com/riley-martine/inappropriate-notifications",
    author="Riley Martine",  # Can we add multiple authors?
    author_email="riley.martine.0@gmail.com",
    packages=["inappropriate_notifications"],
    install_requires=install_requires(),
    python_requires="~=3.6",
    include_package_data=True,
    zip_safe=False,
)
