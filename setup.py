from setuptools import setup, find_packages

exec(open('app_name/version.py').read())
setup(name='app_name',
      version=__version__,
      description='',
      long_description='',
      author='Henning Kage',
      author_email='<henning.kage@gmail.com>',
      url='',
      include_package_data=True,
      classifiers=[],
      packages=find_packages(exclude=['tests']),
      install_requires=['pytest==2.6.1'])
