from setuptools import setup, find_packages
import os

version = '1.0b1'

setup(name='collective.js.formvalidation',
      version=version,
      description="",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone zope javascript jquery form validation',
      author='Timo Stollenwerk',
      author_email='contact@timostollenwerk.net',
      url='https://github.com/collective/collective.js.formvalidation',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.js'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
