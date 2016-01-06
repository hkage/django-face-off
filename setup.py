from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


exec(open('face_off/version.py').read())

tests_require = [
    'pytest==2.8.2',
    'pytest-pep8==1.0.6',
    'pytest-cov==2.2.0',
]

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
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(exclude=[
        'tests',
        'example'
    ]),
    include_package_data=True,
    setup_requires=[
        'pytest-runner==2.6.2',
    ],
    install_requires=[
        'Django>=1.6',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
