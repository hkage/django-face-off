from setuptools import setup, find_packages

exec(open('face_off/version.py').read())

setup(name='django-face-off',
    version=__version__,
    description='A Django application to provide a user switch',
    long_description=read('README.md'),
    author='Henning Kage',
    author_email='<henning.kage@gmail.com>',
    maintainer='Henning Kage',
    maintainer_email='<henning.kage@gmail.com>',
    url='https://github.com/hkage/django-face-off',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=[])
