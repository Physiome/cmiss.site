from setuptools import setup, find_packages
import os

setup(name='cmiss.plonethemeclassic',
      version='1.0',
      description="CMISS Skin",
      long_description=open("README.rst").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme',
      author='ABI Software Team',
      author_email='webmaster@cmiss.org',
      url='http://www.cmiss.org/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cmiss'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
