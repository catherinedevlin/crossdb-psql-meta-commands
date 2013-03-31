from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='crossdb_psql_meta_commands',
    version=version,
    description="Cross-RDBMS implementation of psql's meta-commands ("\dt", etc)",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='database postgresql',
    author='Catherine Devlin',
    author_email='catherine.devlin@gmail.com',
    url='https://github.com/catherinedevlin/crossdb-psql-meta-commands',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['crossdb_psql_meta_commands=crossdb_psql_meta_commands:main']
    }
)
