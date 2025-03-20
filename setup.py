from setuptools import setup, find_packages

setup(
    name='my_project',  # Name of your project
    version='1.0.0',  # Version of your project
    packages=find_packages(),  # Automatically find your packages
    install_requires=[
        'requests',  # External libraries to install (dependencies)
    ],
    entry_points={
        'console_scripts': [
            'my-script=my_project.main:main',  # Command line scripts
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
