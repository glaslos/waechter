from setuptools import setup

import waechter

setup(
    packages=["waechter", ],
    name=waechter.__title__,
    version=waechter.__version__,
    author='Blue Coat Norway',
    author_email='lukas.rist@bluecoat.com',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
    ],
    long_description=open('README.md').read(),
    url='https://sharktank.internal.norman-aws.com/asgard/waechter',
    description='Job Scheduling Helper',
    test_suite='nose.collector',
    tests_require="nose",
    zip_safe=False,
    install_requires=open('requirements.txt').read().splitlines(),
)