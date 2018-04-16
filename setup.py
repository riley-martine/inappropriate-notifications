from setuptools import setup

from os import name as os_name

def install_requires():
    if os_name == 'nt':
        return ['win10toast']
    return []

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='inappropriate-notifications',
      version='0.1',
      description='Display inappropriate notifications at random intervals',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Topic :: Artistic Software',
      ],
      url='https://github.com/riley-martine/inappropriate-notifications',
      author='Riley Martine', # Can we add multiple authors?
      author_email='riley.martine.0@gmail.com',
      packages=['inappropriate_notifications'],
      install_requires=install_requires(),
      include_package_data=True,
      zip_safe=False)
