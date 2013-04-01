import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.txt')) as fp:
    README = fp.read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_webassets',
    'waitress',
]

setup(
    name='webassets_demo',
    version='0.0',
    description='webassets_demo',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="webassets_demo",
    entry_points="""\
    [paste.app_factory]
    main = webassets_demo:main
    """,
)
